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

    std::shared_ptr<Node> zero;
    std::shared_ptr<Node> one;
    int val;

    std::shared_ptr<Node> insert(int bit) {
        if (bit) {
            if (one == nullptr) {
                one = make_shared<Node>();
            }
            return one;
        } else {
            if (zero == nullptr) {
                zero = make_shared<Node>();
            }
            return zero;
        }
    }

    std::shared_ptr<Node> itMaxXor(int bit) {
        if (bit) {
            if (zero != nullptr) {
                return zero;
            } else {
                return one;
            }
        } else {
            if (one.get() != nullptr) {
                return one;
            } else {
                return zero;
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

            std::shared_ptr<Node> tree = std::make_shared<Node>();
            
            for (const auto n : v2) {
                std::shared_ptr<Node> it = tree;

                for (std::size_t j = i >> 1; j > 0 ; j >>= 1) {
                    it = it->insert(n & j);
                }

                it->val = n;
            }

            for (const auto n : v1) {
                std::shared_ptr<Node> it = tree;

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

