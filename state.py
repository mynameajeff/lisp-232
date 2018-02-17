
import stack

class stored_values:

    indent_level = 1

    variables = {}

    headers = {
        "<stdio.h>" : False
    }

    new_file_data = [
        "\nint main() {\n",
        "\n\n    return 0;",
        "\n}\n"
    ]


def get_indent():

    return stored_values.indent_level * "    "


def get_put_line(contents, end_char):

    if not stored_values.headers["<stdio.h>"]:
        stored_values.headers["<stdio.h>"] = True    
    
    if isinstance(contents[1], str):

        if contents[1] in stored_values.variables:
            
            if stored_values.variables[contents[1]] == "int":
                format_value = "%d"

            if stored_values.variables[contents[1]] == "float":
                format_value = "%f"

        else:
            raise ValueError("Invalid variable \"%s\" passed to put keyword." % contents[1])

        line_of_code = "\n{0:s}printf(\"{1:s}{2:s}\", {3:s});".format(
            get_indent(),
            format_value,
            end_char, 
            contents[1]
        )

    else:

        line_of_code = "\n{0:s}printf(\"{1:s}\");".format(get_indent(), contents[1][1] + end_char)

    return line_of_code


def get_val_line(contents):

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
            stored_values.variables[contents[1]] = "int"
            type_var = "int"

        elif isinstance(evaluated_ph, float):
            stored_values.variables[contents[1]] = "float"
            type_var = "float"

        stack.empty()

        line_of_code = "\n{0:s}{1:s} {2:s} = {3:s};".format(
            get_indent(),
            type_var,
            contents[1], 
            str(place_holder)
        )

        return line_of_code

    else:
        raise ValueError("Invalid variable name given.")

