def times(n):
    out = ""
    j=1
    while j <= n:
        i = 1
        while i <= n:
            out += f"{i*j}\t"
            i += 1
        out += "\n"
        j += 1
    return out

n = int(input("Times tables up to? "))
print(times(n))