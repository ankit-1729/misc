def printSoln(i, j, k, l, m, n, o, p):
    print([i, j, k, l], [m, n, o, p], [
          a for a in range(11, 22 + 1) if a not in [i, j, k, l, m, n, o, p]])


count = 0

for i in range(11, 22 + 1):
    for j in range(i + 1, 22 + 1):
        for k in range(j + 1, 22 + 1):
            for l in range(k + 1, 22 + 1):
                if (i + j + k + l == 66):
                    for m in range(11, 22 + 1):
                        if (m not in [i, j, k, l]):
                            for n in range(m + 1, 22 + 1):
                                if (n not in [i, j, k, l]):
                                    for o in range(n + 1, 22 + 1):
                                        if (o not in [i, j, k, l]):
                                            for p in range(o + 1, 22 + 1):
                                                if (p not in [i, j, k, l]):
                                                    if (m + n + o + p == 66):
                                                        count += 1
                                                        printSoln(
                                                            i, j, k, l, m, n, o, p)

print('Number of solutions = ', count)
