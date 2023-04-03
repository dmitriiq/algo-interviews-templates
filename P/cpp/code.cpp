#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

struct Vertex {
    int left;
    int right;

    Vertex(int left, int right) : left(left), right(right) {
    }
};


vector<int> getTreeBorder(const vector<Vertex>& tree, int root) {
    // your code goes here
    unordered_set<int> s;
    std::queue<int> q;
    // vector<int> most_left;
    // vector<int> most_right;
    // bool most_left_reached = false;

    for (int i = root; i != -1; i = tree[i].left)
        s.insert(i);

    for (int i = root; i != -1; i = tree[i].right)
        s.insert(i);

    q.push(root);
    int left_cnt = 0, right_cnt = 0;
    
    while(!q.empty()) {
        bool print = false;
        int &t = q.front();
        q.pop();

        // if (left_cnt < most_left.size() && most_left[left_cnt] == t) {
        //     // std::cout << '\n';
        //     // if (left_cnt == most_left.size() - 1)
        //     //     most_left_reached = true;

        //     // std::cout << t << ' ';
        //     print = true;
        //     left_cnt++;
        // }
        
        // if (right_cnt < most_right.size() && most_right[right_cnt] == t) {
        //     // std::cout << t << ' ';
        //     print = true;
        //     right_cnt++;
        // }

        // if (most_left_reached)
        //     print = true;

        // if (print)
        //     std::cout << t << ' ';

        if (tree[t].left != -1) {
            q.push(tree[t].left);
            // print = true;
        }
        if (tree[t].right != -1) {
            q.push(tree[t].right);
            // print = true;
        }

        if (tree[t].left == -1 && tree[t].right == -1) {
            s.insert(t);
        }

        // if (print)
        //     std::cout << t << ' ';
    }

    vector<int> r;
    for (auto it : s)
        r.push_back(it);

    return r;
}

void outputAnswer(const vector<int>& treeBorder) {
    for (int elem : treeBorder) {
        cout << elem << " ";
    }
    cout << endl;
}

vector<Vertex> readTree(int n) {
    vector<Vertex> tree;
    for (int i = 0; i < n; i++) {
        int left, right;
        cin >> left >> right;
        tree.push_back(Vertex(left, right));
    }
    return tree;
}

int main() {
        int n;
        cin >> n;
        int root;
        cin >> root;
        vector<Vertex> tree = readTree( n);
        outputAnswer(getTreeBorder(tree, root));
}

