def main(v_result):
    a = v_result.split()

    if len(a) != 3:
        print('throws Exception')
        return

    if a[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print('throws Exception')
        return

    if a[2] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        print('throws Exception')
        return

    if a[1] not in ['+', '-', '/', '*']:
        print('throws Exception')
        return

    if a[1] == '+':
        print(int(a[0]) + int(a[2]))
    elif a[1] == '-':
        print(int(a[0]) - int(a[2]))
    elif a[1] == '*':
        print(int(a[0]) * int(a[2]))
    elif a[1] == '/':
        print(int(int(a[0]) / int(a[2])))

main(input())