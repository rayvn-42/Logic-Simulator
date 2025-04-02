from . import Adder

def calculate(InputA1, InputB1, InputC1, InputD1, InputA2, InputB2, InputC2, InputD2, CarryIn):
    result1 = Adder.calculate(InputA1, InputA2, CarryIn)[1]
    result2 = Adder.calculate(InputB1, InputB2, result1[1])[1]
    result3 = Adder.calculate(InputC1, InputC2, result2[1])[1]
    result4 = Adder.calculate(InputD1, InputD2, result3[1])[1]
    return f"Sum: {result4[0]}{result3[0]}{result2[0]}{result1[0]}\nCarry: {result4[1]}", [result1[0], result2[0], result3[0], result4[0], result4[1]];

def PrntTruthTbl():
    return ["Its way too BIG to implement here,",
            "But feel free to do it yourself,",
            "Or if you just want to see it.",
            "You'll be able to find it in the",
            "LogicChips dir under the file 4BitAdder_TruthTable.txt",
            "                 :)"];