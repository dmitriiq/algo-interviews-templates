#include <iostream>
#include <vector>

using namespace std;


bool isPashaWins(int n) {

    return n % 2 == 0;
}

int main() {
    int n;
    cin >> n;
    if (isPashaWins(n)) {
        cout << "Pasha";
    } else {
        cout << "Mark";
    }
}