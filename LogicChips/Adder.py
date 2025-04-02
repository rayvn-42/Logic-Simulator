def calculate(InputA, InputB, CarryIn):
    if InputA == 0 and InputB == 0 and CarryIn == 0:
        Sum = 0
        CarryOut = 0
    elif InputA == 1 and InputB == 1 and CarryIn == 0:
        Sum = 0
        CarryOut = 1
    elif InputA == 0 and InputB == 0 and CarryIn == 1:
        Sum = 1
        CarryOut = 0
    elif InputA == 1 and InputB == 1 and CarryIn == 1:
        Sum = 1
        CarryOut = 1
    elif CarryIn == 0:
        Sum = 1
        CarryOut = 0
    else:
        Sum = 0
        CarryOut = 1

    return f"Sum: {Sum}\nCarry: {CarryOut}", [Sum, CarryOut];

def PrntTruthTbl():
    return [" A | B | C | Carry | Sum ",
            " 0 | 0 | 0 |   0   |  0  ",
            " 0 | 1 | 0 |   0   |  1  ",
            " 1 | 0 | 0 |   0   |  1  ",
            " 1 | 1 | 0 |   1   |  0  ",
            " 0 | 0 | 1 |   0   |  1  ",
            " 0 | 1 | 1 |   1   |  0  ",
            " 1 | 0 | 1 |   1   |  0  ",
            " 1 | 1 | 1 |   1   |  1  "];
