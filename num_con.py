import re


def numberToRoman(input: int) -> str:
    if not isinstance(input, int) or input not in range(1, 4000):
        return "invalid number, please enter a number from 1 to 3999"
    ans = ""
    roman = ["M", "D", "C", "L", "X", "V", "I"]
    val = [1000, 500, 100, 50, 10, 5, 1]
    prefix = [0, 0, 100, 0, 10, 0, 1]
    remain = input
    for current_index, current_val in enumerate(val):
        roman_repeat = int(remain / current_val)
        if roman_repeat > 0:
            ans = ans + roman[current_index] * roman_repeat
            remain = remain - val[current_index] * roman_repeat
        for prefix_index in range(current_index + 1, len(prefix)):  # prefix case
            prefix_val = prefix[prefix_index]
            if 0 < current_val - remain <= prefix_val:
                ans = ans + roman[prefix_index] + roman[current_index]
                remain = remain - current_val + prefix_val
        if remain == 0:
            break
    return ans


def romanToNumber(input: str) -> int:
    if re.search(r"(.)\1{3,}|[^MDCLXVI]", input):
        return "invalid Roman numeral"
    ans = 0
    roman_val = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    for i, current_char in enumerate(input):
        if i < len(input) - 1 and roman_val[current_char] < roman_val[input[i + 1]]:
            prev_char = input[i - 1]
            next_char = input[i + 1]
            if (
                not current_char in ["C", "X", "I"]
                or roman_val[current_char] >= roman_val[prev_char]
                or roman_val[next_char] / 10 > roman_val[current_char]
            ):
                ans = "invalid Roman numeral"
                break
            ans = ans - roman_val[current_char]
        else:
            ans = ans + roman_val[current_char]
    return ans
