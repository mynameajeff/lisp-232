# lisp-232
A small lisp-like language which would be transpiled to C code using Python3/LARK.

For example, this in the new lisp-like language:

```lisp
(defvar $basic_calculation_1 (+ 2 (* 1.5 3)))
(defvar $basic_calculation_2 (+ 4 -6))
(defvar $basic_calculation_3 (/ 4 -6))
(defvar $basic_calculation_4 5)

(putln $basic_calculation_1)
(put "Hello, World!\n")

(putln "Hello, World!")

(putln 5)

(put (+ (* 2 2) (/ 3 5)))
```
Would transpile to this in C:
```c

#include <stdio.h>

int main() {

    float basic_calculation_1 = 2 + (1.5 * 3);
    int basic_calculation_2 = 4 + -6;
    float basic_calculation_3 = 4 / -6;
    int basic_calculation_4 = 5;
    printf("%f\n", basic_calculation_1);
    printf("Hello, World!\n");
    printf("Hello, World!\n");
    printf("%d\n", 5);
    printf("%f", (2 * 2) + (3 / 5));

    return 0;
}

```
Which once compiled, would output this:
```
6.500000
Hello, World!
Hello, World!
5
6.500000
```
