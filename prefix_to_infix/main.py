from collections import Counter


class InvalidExpressionError(Exception):
    pass


def is_valid_expression(expr, operators):
    c = Counter(expr)
    del c[" "]

    operators_number = 0
    for i in operators:
        operators_number += c[i]

    operands_number = c.total() - operators_number
    if operators_number >= operands_number:
        raise InvalidExpressionError("Incorrect expression")


# note: невнимательно прочитал задание, поэтому изначально сделал эту функцию, потом убирать было жалко
def postfix_to_infix(expr, operators):
    is_valid_expression(expr, operators)
    result = []
    l = expr.split()
    for i in l:
        if i not in operators:
            result.append(i)
        else:
            operand1 = result.pop()
            operand2 = result.pop()
            operator = i
            str1 = "(" + operand2 + operator + operand1 + ")"
            result.append(str1)
    return result[0]


def prefix_to_infix(expr, operators):
    is_valid_expression(expr, operators)
    result = []
    l = expr.split()
    for i in l[::-1]:
        if i not in operators:
            result.append(i)
        else:
            operand1 = result.pop()
            operand2 = result.pop()
            operator = i
            str1 = "(" + operand1 + operator + operand2 + ")"
            result.append(str1)
    return result[0]


def main(test_flag=False):
    operators = ["+", "-", "*", "/"]

    # prefix_str1 = "+ - 13 4 55"
    while True:
        user_input = input("Input the expression to evaluate:")
        try:
            res = prefix_to_infix(user_input, operators)
            break
        except InvalidExpressionError as e:
            print("Incorrect expression. Please, try again")
            if test_flag == True:
                return -1

    print(f"Prefix to infix conversion result for {user_input}: {res}")

    # postfix_str1 = "a b c - + d e - f g - h + / *"
    # res = postfix_to_infix(postfix_str1, operators)
    # print(f"Postfix to infix conversion result for {postfix_str1}: {res}")
    return 0


if __name__ == '__main__':
    main()
