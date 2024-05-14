"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def _b(s: str) -> str:

    r = []
    first_ctr = 1

    for i in range(len(s)):
        first = s[i]

        # case: a, null
        if i == len(s) - 1:
            r.append(f"{first}{first_ctr}")
            break

        second = s[i+1]

        # case: a, a
        if first == second:
            first_ctr += 1
            # continue

        # case: a, b
        else:
            r.append(f"{first}{first_ctr}")

            # this now applies to b
            first_ctr = 1

    compressed = "".join(r)

    if len(compressed) < len(s):
        return compressed

    return s


def _a(s: str) -> str:
    r = []
    first_ctr = 1

    if len(s) == 1:
        return s

    for i in range(1, len(s)):
        first = s[i - 1]
        second = s[i]

        # case: a, a
        if first == second:
            first_ctr += 1

            # if this is the last iteration, then add to the result
            if i == len(s) - 1:
                r.append(f"{first}{first_ctr}")

            continue

        # case: a, b
        r.append(f"{first}{first_ctr}")

        # this now relates to b for the next iteration
        first_ctr = 1

        if i == len(s) - 1:
            r.append(f"{second}{1}")


    compressed = "".join(r)

    if len(compressed) < len(s):
        return compressed

    return s


def string_compression(*args) -> str:
    return _b(*args)
