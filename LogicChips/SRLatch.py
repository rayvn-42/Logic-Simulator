def calculate(Set, Reset, PrevSet, PrevLatch):
    if Set == 1 and Reset == 0:
        Q = Set
        Q_not = Reset
    elif Set == 0 and Reset == 1:
        Q = Set
        Q_not = Reset
    elif Set == 0 and Reset == 0:
        return "Hold State", [PrevSet, PrevLatch];
    else:
        return "Invalid State", [PrevSet, PrevLatch];
    return f"Q: {Q}\n_Q: {Q_not}", [Q, Q_not];