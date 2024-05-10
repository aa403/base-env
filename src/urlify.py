"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)
"""


def _a(s: str) -> str:
    return s.replace(" ", "%20")


def _b(s: str) -> str:

    spaces = []
    U = "%20"

    for i in range(len(s)):
        if s[i].isspace():
            spaces.append(i)

    # repeat memory dumps ... not great.
    # but going backwards is the right intuition
    for i in spaces[::-1]:
        s = s[:i] + U + s[i+1:]

    return s


def _c(s: str) -> str:

    spaces = 0
    for i in range(len(s)):
        if s[i].isspace():
            spaces += 1

    final_length = len(s) + spaces*2

    padded_array = list(s) + [" "] * (spaces * 2)

    # index of the padded array
    p_i = final_length - 1

    # index of the string
    s_i = len(s) - 1

    while s_i >= 0:

        if s[s_i].isspace():
            padded_array[p_i] = "0"
            padded_array[p_i-1] = "2"
            padded_array[p_i-2] = "%"

            # jump back 3 in the padded array
            p_i -= 3

        else:
            if p_i > s_i:
                padded_array[p_i] = s[s_i]
            p_i -= 1

        s_i -= 1

    return "".join(padded_array)


def urlify(s: str) -> str:
    return _c(s)
