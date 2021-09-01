def SplitInput(user_input):
    split_input = user_input.split()
    n = int(split_input[0])
    wires = []
    split_input[1] = split_input[1].replace('),(', ') (')
    storeys = split_input[1][1:len(split_input[1])-1].split()
    for each in storeys:
        each = each[1:len(each)-1]
        t = each.split(',')
        wires.append((int(t[0]), int(t[1])))
    return n, wires


def Crosses(n, wires):
    cross = 0
    for i in range(len(wires)-1):
        for j in range(i+1, len(wires)):
            if (wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]) or (wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]):
                cross += 1
    return cross

def main():
    m = int(input())
    for i in range(m):
        user_input = input()
        n, wires = SplitInput(user_input)
        print(Crosses(n, wires))
main()
