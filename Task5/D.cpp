#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long X;
    cin >> X;

    long long bestA = 1, bestB = X;

    for (long long d = 1; d * d <= X; d++) {
        if (X % d == 0) {
            long long a = d;
            long long b = X / d;

            if (std::gcd(a, b) == 1) {
                if (max(a, b) < max(bestA, bestB)) {
                    bestA = a;
                    bestB = b;
                }
            }
        }
    }

    cout << bestA << " " << bestB << "\n";
    return 0;
}