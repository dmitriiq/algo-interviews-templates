#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;


struct HistoricalArray {
    int size;
    int currentEra;
    map<int, vector<int>> eras;

    HistoricalArray(int n) : size(n), currentEra(0) {
        // eras.emplace(std::make_pair(0, vector<int>(size, 0)));
    	eras[currentEra] = vector<int>(size, 0);
    }
    
    void beginNewEra(int eraId) {
        // eras.emplace(std::make_pair(eraId, vector<int>(size, 0)));
        // currentEra = eraId;
    	currentEra = eraId;
    	eras[currentEra] = vector<int>(size, 0);
    }

    void set(int index, int value) {
        eras[currentEra][index] = value;
    }

    int get(int index, int eraId) {
        return eras[eraId][index];
    }
};

int main(int argc, char const *argv[]) {
    int n;
    cin >> n;
    HistoricalArray arr(n);
    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        string queryType;
        cin >> queryType;
        if (queryType == "set") {
            int index, value;
            cin >> index >> value;
            arr.set(index, value);
        } else if (queryType == "begin_new_era") {
            int eraId;
            cin >> eraId;
            arr.beginNewEra(eraId);
        } else if (queryType == "get") {
            int index, eraId;
            cin >> index >> eraId;
            cout << arr.get(index, eraId) << endl;
        }
    }
}
