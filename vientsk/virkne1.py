# Teksta faila virkne.dat pirmajā rindā doti divi naturāli skaitļi,
# kas atdalīti ar tukšumsimboliem - kopējais skaitļu daudzums virknē n(n≤500001) un k(1<k<100).
# Katrā no nākošājām n faila rindām dots pa vienam naturālam skaitlim,
# kura vērtība nepārsniedz 2147483647. Skaitlis faila i+1-ajā rindā ir virknes i-tais loceklis.
N, K = map(int, input().split())
counts = dict()
for n in range(N):
    x = int(input())
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

for (key, val) in counts.items():
    if val == 1:
        print(key)
        break


