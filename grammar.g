
expr: "(" operator operand_placeholder operand ")"
    | "(" keywords_single operand_single ")"

operator: calculation
        | keywords_nest
        | variable_name

operand_single: (variable_name 
              | string
              | num)

?calculation: /(\+|-|\/|\*)/

?keywords_nest: "defvar" -> defvar

?keywords_single: "put"   -> put
                | "putln" -> putln

operand_placeholder: operand
                   | variable_name

?variable_name: /\$[A-Za-z_][A-Za-z0-9_]*/ -> variable

operand: (expr 
       | num)

num: signed 

string: STR_CONST
STR_CONST: /\"[A-Za-z0-9\\\/\.!?~, ]+\"/

signed: SIGNED_NUMBER

%import common.SIGNED_NUMBER
%import common.WS
%ignore WS
