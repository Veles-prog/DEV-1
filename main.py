def main(v_result):
    a = v_result.split()

    if len(a) != 3:
        return "throws Exception"

    if a[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return "throws Exception"

    if a[2] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return "throws Exception"

    if a[1] not in ['+', '-', '/', '*']:
        return "throws Exception"
    if a[1] == '+':
        return(str(int(a[0]) + int(a[2])))
    elif a[1] == '-':
        return(str(int(a[0]) - int(a[2])))
    elif a[1] == '*':
        return(str(int(a[0]) * int(a[2])))
    elif a[1] == '/':
        return(str(int(a[0]) // int(a[2])))

print(main(input()))