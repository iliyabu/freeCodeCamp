def arithmetic_arranger(problems, result=False):
    too_many_problems = False
    appropriate_operators = True
    operands_contain_only_digits = True
    operands_have_max_four_digits = True

    output = ""
    arranged_problems = [[] for _ in range(4)]

    if len(problems) > 5:
        too_many_problems = True

    for index, problem in enumerate(problems):
        problems[index] = problem.split()

        if problems[index][1] in ('*', '/'):
            appropriate_operators = False

        if problems[index][0].isdigit() and problems[index][2].isdigit():

            if len(problems[index][0]) > len(problems[index][2]):
                len_of_longest_operand = len(problems[index][0])
            else:
                len_of_longest_operand = len(problems[index][2])

            if len_of_longest_operand > 4:
                operands_have_max_four_digits = False
            else:
                arranged_problems[0].append(problems[index][0].rjust(len_of_longest_operand + 2))
                arranged_problems[1].append(problems[index][1] + problems[index][2].rjust(len_of_longest_operand + 1))
                arranged_problems[2].append("-" * (len_of_longest_operand + 2))

                calculation = eval(problems[index][0] + problems[index][1] + problems[index][2])
                calculation = str(calculation).rjust(len_of_longest_operand + 2)
                arranged_problems[3].append(calculation)
        else:
            operands_contain_only_digits = False

    if not too_many_problems and appropriate_operators and operands_contain_only_digits and operands_have_max_four_digits:
        range_length = 4 if result else 3

        for i in range(range_length):
            output += "    ".join(arranged_problems[i]) + "\n"

        output = output.rstrip()

    elif too_many_problems:
        output = "Error: Too many problems."
    elif not appropriate_operators:
        output = "Error: Operator must be '+' or '-'."
    elif not operands_contain_only_digits:
        output = "Error: Numbers must only contain digits."
    elif not operands_have_max_four_digits:
        output = "Error: Numbers cannot be more than four digits."

    return output


print(arithmetic_arranger(['3801 - 2', '123 + 49']))
