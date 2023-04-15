#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void outputAnswer(const vector<string>& sequences) {
    for (const string& sequence : sequences) {
        cout << sequence << " ";
    }
}

class Bracer {
    static const std::vector<char> braces;

    std::vector<std::string> result;
    // std::vector<char> stack;

    static bool updateStack(char c, std::vector<char> &stack) {

        if (c == '(') {
            if (std::find(stack.begin(), stack.end(), '[') != stack.end())
                return false;
            stack.push_back(c);
        } else if (c == '[') {
            stack.push_back(c);
        } else if (c == ')') {
            if (stack.size() == 0)
                return false;
            else if (stack.back() == '(') {
                stack.pop_back();
            } else {
                return false;
            }
        } else if (c == ']') {
            if (stack.size() == 0)
                return false;
            else if (stack.back() != '[') {
                return false;
            } else {
                stack.pop_back();
            }
        }

        return true;
    }

public:


    void addBrace(int n, std::string str = "", std::vector<char> stack = {}) {
        // std::cout << "n = " << n;
        // for (char c : stack)
        //     std::cout << c << ' ';
        // std::cout << '\n';
        if (n > 0) {
            for (const auto& b : braces) {
                auto updatedStack = stack;
                if (updateStack(b, updatedStack)) {
                    addBrace(n - 1, str + b, updatedStack);
                }
            }
        } else {
            if (stack.size() == 0)
                result.push_back(str);
        }
        // for (char c : stack)
        //     std::cout << c << ' ';
        // std::cout << '\n';
    }

    std::vector<std::string> getResult() {
        return result;
    }
};

const std::vector<char> Bracer::braces = {'(', '[', ')', ']'};

vector<string> generateSequences(int n) {
    // std::vector<std::string> result;
    Bracer bracer;
    bracer.addBrace(n);
    return bracer.getResult();
}

int main() {
    int n;
    cin >> n;
    outputAnswer(generateSequences(n));
}