def calculate(InputA, InputB):
    if InputA == 1 and InputB == 1:
        return "Output: 0";
    else:
        return "Output: 1";

def PrntTruthTbl():
    return [" A | B | Out ",
            " 0 | 0 |  1  ",
            " 0 | 1 |  1  ",
            " 1 | 0 |  1  ",
            " 1 | 1 |  0  "];