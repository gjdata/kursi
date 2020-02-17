def printMaxActivities(sf):
    n = len(sf)

    # The first activity is always selected
    i = 0

    count = 1

    # Consider rest of the activities
    for j in range(1, n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if sf[j][0] > sf[i][1]:
            i = j
            count += 1

    print(f'{count}')


N = int(input())
# start = []
# finish = []
fs = []
for n in range(N):
    datestring1, datestring2 = input().split()
    d1, m1, y1 = datestring1.split('.')
    d2, m2, y2 = datestring2.split('.')
    date1 = y1 + m1 + d1
    date2 = y2 + m2 + d2
    pair = date1, date2
    fs.append(pair)

fs.sort(key=lambda x: x[1])

printMaxActivities(fs)
