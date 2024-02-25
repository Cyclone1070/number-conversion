def intToRom(int: int) -> str:
    ans = ''
    roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    val = [1000, 500, 100, 50, 10, 5, 1]
    prefix = [0, 0, 100, 0, 10, 0, 1]
    remain = int
    for i, n in enumerate(val):
        while remain >= n:
            ans = ans + roman[i]
            remain = remain - n
        for index in range(i + 1, len(prefix)): #prefix case
            num = prefix[index]
            if (0 < n - remain <= num):
                ans = ans + roman[index] + roman[i]
                remain = remain - n + num
        if remain < n:
            continue
        if remain == 0:
            break
    return ans