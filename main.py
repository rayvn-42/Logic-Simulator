import LogicChips
import subprocess
import os

def main():
    running = True

    
    # Bistable Chips state variables
    SRLatch_Q = 0
    SRLatch_Q_not = 0

    while running:
        user_input = input("\033[92m> \033[0m")

        tokens = user_input.split()

        if user_input.lower() == "quit":
            running = False
            print("Quiting")
        elif user_input.lower() == "list":
            print(LogicChips.AvailableChips)
        elif user_input.lower() == "help":
            print('---Digital Logic Simulator---\n'
                  '      ------Help------\n'
                  'This is a Logical Simulator that\n'
                  'simulates logical gates such as\n'
                  'and gates, not gates and more.\n'
                  '------Logic gates params------\n'
                  'And(InputA, InputB)\n'
                  'Nand(InputA, InputB)\n'
                  'Not(InputA)\n'
                  'Or(InputA, InputB)\n'
                  'Adder(InputA, InputB, CarryIn)\n'
                  '     ------Commands------\n'
                  'list: list available logic gates\n'
                  'quit: quits this program\n'
                  'help: shows this menu\n'
                  'clear: clears the terminal\n'
                  'truth <gate>: shows the truth table of a gate. No output for larger tables\n'
                  'use <gate>: selects a logical gate to use\n'
                  ' ---Supported logic gates---\n'
                  f'{LogicChips.AvailableChips}\n')
        elif user_input.lower() == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif tokens[0].lower() == "!" and len(tokens) > 1:
            command = " ".join(tokens[1:])
            try:
                subprocess.run(command, check=True, shell=True)
            except Exception as e:
                print(f"unknown command: {command}")
        elif len(tokens) == 2:
            if tokens[0].lower() == "use":
                if tokens[1].lower() == "and":
                    inputA = int(input("Input A: "))
                    inputB = int(input("Input B: "))
                    print(LogicChips.And.calculate(inputA, inputB))
                elif tokens[1].lower() == "not":
                    inputA = int(input("Input A: "))
                    print(LogicChips.Not.calculate(inputA))
                elif tokens[1].lower() == "or":
                    inputA = int(input("Input A: "))
                    inputB = int(input("input B: "))
                    print(LogicChips.Or.calculate(inputA, inputB))
                elif tokens[1].lower() == "nand":
                    inputA = int(input("Input A: "))
                    inputB = int(input("input B: "))
                    print(LogicChips.Nand.calculate(inputA, inputB))
                elif tokens[1].lower() == "xor":
                    inputA = int(input("Input A: "))
                    inputB = int(input("input B: "))
                    print(LogicChips.Xor.calculate(inputA, inputB)[0])
                elif tokens[1].lower() == "adder":
                    inputA = int(input("Input A: "))
                    inputB = int(input("input B: "))
                    carryIn = int(input("Carry In: "))
                    print(LogicChips.Adder.calculate(inputA, inputB, carryIn)[0])
                elif tokens[1].lower() == "adder4":
                    inputA1 = int(input("Input A1: "))
                    inputB1 = int(input("Input B1: "))
                    inputC1 = int(input("Input C1: "))
                    inputD1 = int(input("Input D1: "))
                    inputA2 = int(input("Input A2: "))
                    inputB2 = int(input("Input B2: "))
                    inputC2 = int(input("Input C2: "))
                    inputD2 = int(input("Input D2: "))
                    carryIn = int(input("Carry In: "))
                    print(LogicChips.Adder4.calculate(inputA1, inputB1, inputC1, inputD1, inputA2, inputB2, inputC2, inputD2, carryIn))
                elif tokens[1].lower() == "alu":
                    inputA1 = int(input("Input A1: "))
                    inputB1 = int(input("Input B1: "))
                    inputC1 = int(input("Input C1: "))
                    inputD1 = int(input("Input D1: "))
                    inputA2 = int(input("Input A2: "))
                    inputB2 = int(input("Input B2: "))
                    inputC2 = int(input("Input C2: "))
                    inputD2 = int(input("Input D2: "))
                    Sub = int(input("Subtract: "))
                    print(LogicChips.Alu.calculate(inputA1, inputB1, inputC1, inputD1, inputA2, inputB2, inputC2, inputD2, Sub)[0])
                elif tokens[1].lower() == "srlatch":
                    Set = int(input("Set: "))
                    Reset = int(input("Reset: "))
                    print(f"Previous state:\nQ: {SRLatch_Q}\n_Q: {SRLatch_Q_not}")
                    result = LogicChips.SRLatch.calculate(Set, Reset, SRLatch_Q, SRLatch_Q_not)

                    print_val = result[0]
                    SRLatch_Q = result[1][0]
                    SRLatch_Q_not = result[1][1]

                    print("New state:\n" + print_val)
            elif tokens[0].lower() == "truth":
                if tokens[1].lower() == "and":
                    for line in LogicChips.And.PrntTruthTbl():
                        print(line)
                elif tokens[1].lower() == "not":
                    for line in LogicChips.Not.PrntTruthTbl():
                        print(line)
                elif tokens[1].lower() == "or":
                    for line in LogicChips.Or.PrntTruthTbl():
                        print(line)
                elif tokens[1].lower() == "nand":
                    for line in LogicChips.Nand.PrntTruthTbl():
                        print(line)
                elif tokens[1].lower() == "xor":
                    for line in LogicChips.Xor.PrntTruthTbl():
                        print(line)
                elif tokens[1].lower() == "adder":
                    for line in LogicChips.Adder.PrntTruthTbl():
                        print(line)
                elif tokens[1].lower() == "adder4":
                    for line in LogicChips.Adder4.PrntTruthTbl():
                        print(line)
                elif tokens[1].lower() == "alu":
                    for line in LogicChips.Alu.PrntTruthTbl():
                        print(line)
                else:
                    print(f"unknown chip: {tokens[1]}")
            else:
                print(f"unknown command: {tokens[0]}")

        else:
            print(f"unknown command: {user_input}")




if __name__ == "__main__":
    main()
