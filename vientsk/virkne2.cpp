// Teksta faila virkne.dat pirmajā rindā doti divi naturāli skaitļi,
// kas atdalīti ar tukšumsimboliem - kopējais skaitļu daudzums virknē n(n≤500001) un k(1<k<100).
// Katrā no nākošājām n faila rindām dots pa vienam naturālam skaitlim,
// kura vērtība nepārsniedz 2147483647. Skaitlis faila i+1-ajā rindā ir virknes i-tais loceklis.


#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <map>

using namespace std;
typedef long long big;

int main() {
    big N, K;
    cin >> N >> K;
    
    map<big, big> counts;
    for (big n = 0; n<N; n++) {
       big x;
       cin >> x;
       counts[x]++;       
    }

    for (auto const& x : counts) {
        big key = x.first;
        big val = x.second;
        if (val == 1) {
            cout << key;
            break;
        }
    }
}

/*
N, K = map(big, input().split())
counts = dict()
for n in range(N):
    x = big(input())
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

for (key, val) in counts.items():
    if val == 1:
        prbig(key)
        break
*/

