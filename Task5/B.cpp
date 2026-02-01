#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        long long n;
        cin >> n;

        long long a = -1, b = -1, c = -1;

        // find first divisor
        for (long long i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                a = i;
                n /= i;
                break;
            }
        }

        if (a == -1) {
            cout << "NO\n";
            continue;
        }

        // find second divisor
        for (long long i = a + 1; i * i <= n; i++) {
            if (n % i == 0) {
                b = i;
                c = n / i;
                break;
            }
        }

        if (b == -1 || c == a || c == b || c < 2) {
            cout << "NO\n";
        } else {
            cout << "YES\n";
            cout << a << " " << b << " " << c << "\n";
        }
    }

    return 0;
}
