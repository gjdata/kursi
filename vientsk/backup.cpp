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

int main() {
    int N, K;
    cin >> N >> K;
    
    map<int, int> counts;
    for (int n = 0; n<N; n++) {
       int x;
       cin >> x;
       counts[x]++;       
    }

    for (auto const& x : counts) {
        int key = x.first;
        int val = x.second;
        if (val == 1) {
            cout << key;
            break;
        }
    }
}

/*
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
*/

