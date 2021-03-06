#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def suma(self, operando1, operando2):
        return operando1 + operando2

    def resta(self, operando1, operando2):
        return operando1 - operando2


if __name__ == "__main__":
    calculadora = Calculadora()

    try:
        operando1 = int(float(sys.argv[1]))
        operando2 = int(float(sys.argv[3]))
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = calculadora.suma(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadora.resta(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
