
from state import *

import par

class Transpiler:

    def __init__(self, file):

        self.file_data = par.get_data(
            par.get_parse_tree(file)
        )

        self.file_name = file.split(".")[0] + ".c"

        self.counter = 1

        self.inner_loop()


    def write_transpiled_code(self):

        #expects name(.lisp)
        with open(self.file_name, "w") as file:

            for header in stored_values.headers:

                if stored_values.headers[header]:
                    file.write("\n#include %s" % header)

            file.write("\n")

            for contents in stored_values.new_file_data:
                file.write(contents)


    def inner_var(self, contents):

        stored_values.new_file_data.insert(
            self.counter, 
            get_val_line(contents)
        )

        self.counter += 1


    def inner_put(self, contents, end_char = ""):

        stored_values.new_file_data.insert(
            self.counter, 
            get_put_line(contents, end_char)
        )

        self.counter += 1


    def inner_loop(self):

        for self.line,  contents in enumerate(self.file_data):

            if contents[0] == "var":

                self.inner_var(contents)

            elif contents[0] == "put":

                self.inner_put(contents)

            elif contents[0] == "putln":

                self.inner_put(contents, end_char = "\\n")

        self.write_transpiled_code()


Transpiler("example.lisp")
