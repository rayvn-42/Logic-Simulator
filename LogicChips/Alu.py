from . import Adder4
from . import Xor

def calculate(InputA1, InputB1, InputC1, InputD1, InputA2, InputB2, InputC2, InputD2, Sub):
    modified_input2 = [Xor.calculate(bit, Sub)[1] for bit in [InputA2, InputB2, InputC2, InputD2]]
    res = Adder4.calculate(InputA1, InputB1, InputC1, InputD1, *modified_input2, Sub)
    Sum = res[1][:4]
    CarryOut = res[1][4]
    Zero_flag = 1 if Sum == [0, 0, 0, 0] else 0
    Sum = Sum[::-1]
    bin_str = ''.join(map(str, Sum))
    dec_val = int(bin_str, 2)
    if Sum[0] == 1:
        dec_val -= 16
    return res[0] + f"\nSubtraction: {Sub}\nZero: {Zero_flag}\n[{bin_str}] ({dec_val})", Sum, {"zero": Zero_flag, "subtraction": Sub, "carry": CarryOut}

def PrntTruthTbl():
    return ["Its way too BIG to implement here,",
            "But feel free to do it yourself,",
            "Or if you just want to see it.",
            "You'll be able to find it in the",
            "LogicChips dir under the file ALU_TruthTable.txt",
            "                 :)"]
