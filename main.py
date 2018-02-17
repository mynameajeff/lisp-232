
import stack
import par

class Transpiler:

    def __init__(self, file):

        self.file_data = par.get_data(
            par.get_parse_tree(file)
        )

        self.headers = {
            "<stdio.h>" : False
        }

        self.file_name = file.split(".")[0] + ".c"

        self.counter = 1

        self.new_file_data = [
            "\nint main() {\n",
            "\n\n    return 0;"
            "\n}\n"
        ]

        self.variables = {}

        self.inner_loop()


    def write_transpiled_code(self):

        #expects name(.lisp)
        with open(self.file_name, "w") as file:

            for header in self.headers:

                if self.headers[header]:
                    file.write("\n#include %s" % header)

            file.write("\n")

            for contents in self.new_file_data:
                file.write(contents)


    def inner_var(self, contents):

        if isinstance(contents[1], str):

            if isinstance(contents[2], tuple):
                place_holder = stack.stringify(stack.gpt(contents[2]))
                evaluated_ph = eval(place_holder)
            else:
                place_holder = contents[2]

                if place_holder.is_integer():
                    place_holder = int(place_holder)
                    
                evaluated_ph = place_holder

            if isinstance(evaluated_ph, int):
                self.variables[contents[1]] = "int"
                type_var = "int"

            elif isinstance(evaluated_ph, float):
                self.variables[contents[1]] = "float"
                type_var = "float"

            stack.empty()

            line_of_code = "\n    {0:s} {1:s} = {2:s};".format(
                type_var,
                contents[1], 
                str(place_holder)
            )

            self.new_file_data.insert(
                self.counter, 
                line_of_code
            )

            self.counter += 1

        else:
            raise ValueError("Invalid variable name given.")


    def inner_put(self, contents, end_char = ""):

        if not self.headers["<stdio.h>"]:
            self.headers["<stdio.h>"] = True    
        
        if isinstance(contents[1], str):

            if contents[1] in self.variables:
                
                if self.variables[contents[1]] == "int":
                    format_value = "%d"

                if self.variables[contents[1]] == "float":
                    format_value = "%f"

            else:
                raise ValueError("Invalid variable \"%s\" passed to put keyword." % contents[1])

            line_of_code = "\n    printf(\"{0:s}{1:s}\", {2:s});".format(
                format_value,
                end_char, 
                contents[1]
            )

        else:

            line_of_code = "\n    printf(\"{0:s}\");".format(contents[1][1] + end_char)

        self.new_file_data.insert(
            self.counter, 
            line_of_code
        )

        self.counter += 1


    def inner_loop(self):

        for self.line,  contents in enumerate(self.file_data):

            if contents[0] == "var":

                self.inner_var(contents)

            if contents[0] == "put":

                self.inner_put(contents)

            if contents[0] == "putln":

                self.inner_put(contents, end_char = "\\n")

        self.write_transpiled_code()


Transpiler("example.lisp")
