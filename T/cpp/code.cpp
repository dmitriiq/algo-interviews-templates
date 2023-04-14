#include <algorithm>
#include <iostream>
#include <vector>
#include <memory>

using namespace std;

class Node {
public:
    Node() :
        zero(nullptr),
        one(nullptr),
        val(0)
    { }

    std::unique_ptr<Node> zero;
    std::unique_ptr<Node> one;
    int val;

    Node* insert(int bit) {
        if (bit) {
            if (one.get() == nullptr) {
                one = make_unique<Node>();
            }
            return one.get();
        } else {
            if (zero.get() == nullptr) {
                zero = make_unique<Node>();
            }
            return zero.get();
        }
    }

    Node* itMaxXor(int bit) {
        if (bit) {
            if (zero.get() != nullptr) {
                return zero.get();
            } else {
                return one.get();
            }
        } else {
            if (one.get() != nullptr) {
                return one.get();
            } else {
                return zero.get();
            }
        }
    }
};

long long getMaxXOR(const vector<int>& list) {
    int r = 0;

    for (std::size_t i = 0x40000000; i > 0; i >>= 1) {
        int len1 = 0;
        int len2 = 0;
        for (const auto n : list) {
            if (n & i) {
                len1++;
            } else {
                len2++;
            }
        }

        if (len1 > 0 && len2 > 0) {
            std::vector<int> v1;
            std::vector<int> v2;

            // std::cout << len1 << ' ' << len2 << '\n';
            for (const auto n : list) {
                if (n & i) {
                    v1.push_back(n);
                } else {
                    v2.push_back(n);
                }
            }

            Node tree;
            
            for (const auto n : v2) {
                Node *it = &tree;

                for (std::size_t j = i >> 1; j > 0 ; j >>= 1) {
                    it = it->insert(n & j);
                }

                it->val = n;
            }

            for (const auto n : v1) {
                Node *it = &tree;

                for (std::size_t j = i >> 1; j > 0; j >>= 1) {
                    it = it->itMaxXor(n & j);
                }

                r = std::max(r, n ^ it->val);
            }

            break;
        }
    }


    return r;
}

vector<int> readList() {
    int n;
    cin >> n;
    vector<int> res(n);
    for (int i = 0; i < n; i++) {
        cin >> res[i];
    }
    return res;
}

int main() {
    vector<int> list = readList();
    cout << getMaxXOR(list);
}

