#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;


struct Building {
    int needCapital;
    int addedCapital;

    Building(int c, int p) {
        needCapital = c;
        addedCapital = p;
    }
};


long long getMaxFinalCapital(vector<Building>& buildings, int startCapital, int maxNumberOfBuildings) {
    // your code goes here
    long long capital = startCapital;

    std::sort(buildings.begin(), buildings.end(),
            [](const Building &a, const Building &b) {
                return a.needCapital < b.needCapital;
    });

    std::priority_queue<int> added;
    for (int i = 0; maxNumberOfBuildings > 0;) {
        // std::cout << "need cap: " << buildings[i].needCapital << '\n';
        if (i < buildings.size() && buildings[i].needCapital <= capital) {
            added.push(buildings[i].addedCapital);
            ++i;
        } else {
            if (added.size() > 0) {
                capital += added.top();
                added.pop();
                --maxNumberOfBuildings;
            } else {
                break;
            }
        }
    }

    return capital;
}


vector<Building> readBuildings(int n) {
    vector<Building> buildings;
    for (int i = 0; i < n; i++) {
        int c, p;
        cin >> c >> p;
        buildings.push_back(Building(c, p));
    } 
    return buildings;
}

int main() {
        int n;
        cin >> n;
        int k;
        cin >> k;
        vector<Building> buildings = readBuildings(n);
        int M;
        cin >> M;
        cout << getMaxFinalCapital(buildings, M, k) << endl;
}




