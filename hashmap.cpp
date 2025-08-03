#include <iostream>
#include <list>
#include <vector>
#include <string>

using namespace std;

class HashMap {
private:
    static const int TABLE_SIZE = 10; // Size of the hashmap
    vector<list<pair<string, int>>> table;

    int hashFunction(string key) {
        int hash = 0;
        for (char ch : key) {
            hash = (hash + int(ch)) % TABLE_SIZE;
        }
        return hash;
    }

public:
    HashMap() {
        table.resize(TABLE_SIZE);
    }

    void insert(string key, int value) {
        int index = hashFunction(key);
        for (auto& item : table[index]) {
            if (item.first == key) {
                item.second = value;
                return;
            }
        }
        table[index].push_back({key, value});
    }

    bool get(string key, int &value) {
        int index = hashFunction(key);
        for (auto& item : table[index]) {
            if (item.first == key) {
                value = item.second;
                return true;
            }
        }
        return false;
    }

    void remove(string key) {
        int index = hashFunction(key);
        auto& chain = table[index];
        for (auto it = chain.begin(); it != chain.end(); ++it) {
            if (it->first == key) {
                chain.erase(it);
                return;
            }
        }
    }

    void display() {
        for (int i = 0; i < TABLE_SIZE; ++i) {
            cout << "Bucket " << i << ": ";
            for (auto& item : table[i]) {
                cout << "[" << item.first << ": " << item.second << "] ";
            }
            cout << endl;
        }
    }
};

int main() {
    HashMap h;

    h.insert("Mars", 1);
    h.insert("Earth", 2);
    h.insert("Venus", 3);

    h.display();

    int val;
    if (h.get("Earth", val)) {
        cout << "Value for 'Earth': " << val << endl;
    }

    h.remove("Earth");
    h.display();

    return 0;
}
