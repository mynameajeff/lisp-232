
import lark

class tran(lark.Transformer):

    def signed(self, n):
        return float(n[0])

    def unsigned(self, n):
        return float(n[0][1:-1])

    def operator(self, n):
        return str(n[0])

    def variable(self, n):
        return str(n[0])[1:]

    def string(self, n):
        return ("str_const::", str(n[0][1:-1]))

    expr = tuple
    
    operand_single = lambda _, n: n[0]

    putln   = lambda self, _: "putln"
    put     = lambda self, _: "put"
    defvar  = lambda self, _: "var"

    operand = lambda _, n: n[0]
    num     = lambda _, n: n[0]


with open("grammar.g") as file:
    script_grammar = r''.join([line for line in file])

script_parser = lark.Lark(
    script_grammar,
    start  = "expr",
    parser = "lalr"
)


def get_parse_tree(file_path):

    with open(file_path) as file:
        script_code = [
            line
                .replace("\\~", chr(0x4))
                .replace("~", "\n~")
                .split("~")[0]
                .replace(chr(0x4), "~")

            for line in file
        ]

    expression_list = []

    for line in script_code:

        if line != "\n":
            parse = script_parser.parse(line)
            expression_list.append(parse)
            # print(parse.pretty())

    return expression_list


def get_data(parse_tree):

    cleaned_tree = []

    local_transformer = tran()

    for item in parse_tree:

        cleaned_tree.append(local_transformer.transform(item))

    return cleaned_tree
