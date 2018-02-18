
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


def get_eval_type(evaluated_ph, literal_type = False):

    if literal_type:
        types_local = ["int", "float"]

    else:
        types_local = ["%d", "%f"]

    if   isinstance(evaluated_ph, int):   return types_local[0]

    elif isinstance(evaluated_ph, float): return types_local[1]


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

    elif isinstance(contents[1], float):
        
        if contents[1].is_integer():
            contents_final = int(contents[1])
            format_value = "%d"
        else:
            contents_final = contents[1]
            format_value = "%f"

        line_of_code = "\n{0:s}printf(\"{1:s}{2:s}\", {3});".format(
            get_indent(),
            format_value,
            end_char,
            contents_final
        )

    elif isinstance(contents[1], tuple):

        if contents[1][0] == "str_const::":

            line_of_code = "\n{0:s}printf(\"{1:s}\");".format(
                get_indent(), 
                contents[1][1] + end_char
            )

        else:

            place_holder = stack.stringify(stack.gpt(contents[1]))
            
            type_var = get_eval_type(eval(place_holder))

            line_of_code = "\n{0:s}printf(\"{1:s}{2:s}\", {3:s});".format(
                get_indent(),
                type_var,
                end_char,
                place_holder
            )

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

        if isinstance(place_holder, str):
            type_var = eval(place_holder)
        
        else:
            type_var = place_holder

        type_var = get_eval_type(type_var, literal_type = True)

        stored_values.variables[contents[1]] = type_var

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

