#include "solution.h"
#include <vector>

// Comment it before submitting
// struct Node {
//     int val;
//     std::vector<Node*> neighbours;
//     Node(int val_) {
//         val = val_;
//         neighbours = {};
//     }
// };


Node* cloneGraph(Node* node) {
    static std::vector<Node*> visited;

    for (int i = 0; i < visited.size(); ++i) {
        if (visited[i]->val == node->val)
            return visited[i];
    }

    Node* new_node = new Node(node->val);
    visited.push_back(new_node);
    for (int i = 0; i < node->neighbours.size(); ++i) {
        cloneGraph(node->neighbours[i]);
    }

    return new_node;
}

// int main () {
//     return 0;
// }
