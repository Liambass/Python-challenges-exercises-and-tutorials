
#longest increasing sequence problem



def plan_route(input):
    peaks_list = [int(i) for i in input.split()]
    lis = [1 for i in peaks_list]
    prevs = [0 for i in peaks_list]
    n = len(peaks_list)
    for i in range(1, n):
        for j in range(0, i):
            if peaks_list[i] > peaks_list[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prevs[i] = j
    maximum = 0
    for i in range(0, n):
        maximum = max(maximum, lis[i])
    i = lis.index(maximum)
    route = [str(peaks_list[i])]
    while len(route) != maximum:
        route.append(str(peaks_list[prevs[i]]))
        i = prevs[i]
    outroute = ' '.join(reversed(route))
    return outroute

print(plan_route('0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15'))