def calculate(a: int, b: str, op_type):
    if op_type == "+":
        print(a + int(b))
    elif op_type == "-":
        print(a - int(b))
    elif op_type == "/":
        if int(b) == 0:
            print('На ноль делить нельзя!')
        else:
            print(a / int(b))
    elif op_type == "*":
        print(a * int(b))


calculate(5, "1", '/')
