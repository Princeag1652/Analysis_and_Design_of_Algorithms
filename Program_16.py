
def build_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    n = len(haystack)
    m = len(needle)

    lps = build_lps(needle)

    i = 0  # Haystack index
    j = 0  # Needle index

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == m:
            return i - j

        elif i < n and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


# Example
print(strStr("hello", "ll"))
print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
