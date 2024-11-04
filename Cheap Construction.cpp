#include <bits/stdc++.h>
using namespace std;

class UnionFind {
    vector<int> parent;
public:
    UnionFind(int n) : parent(n) {
        for(int i = 0; i < n; i++) parent[i] = i;
    }
    
    int find(int x) {
        if(parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    void unite(int x, int y) {
        parent[find(x)] = find(y);
    }
    
    int countComponents() {
        unordered_set<int> components;
        for(int i = 0; i < parent.size(); i++) {
            components.insert(find(i));
        }
        return components.size();
    }
};

vector<int> solve(const string& S) {
    int N = S.length();
    vector<int> answer(N, 0);
    
    // For each possible length of T
    for(int len = 1; len <= N; len++) {
        unordered_map<string, vector<int>> patterns;
        
        // Find all patterns of current length and their positions
        for(int i = 0; i <= N - len; i++) {
            patterns[S.substr(i, len)].push_back(i);
        }
        
        // For each unique pattern
        for(const auto& pattern : patterns) {
            // Create UnionFind for this pattern
            UnionFind uf(N);
            
            // Build bridges for all occurrences of this pattern
            for(int pos : pattern.second) {
                for(int i = pos; i < pos + len - 1; i++) {
                    uf.unite(i, i + 1);
                }
            }
            
            // Count components and update answer
            int components = uf.countComponents();
            if(answer[components - 1] == 0 || len < answer[components - 1]) {
                answer[components - 1] = len;
            }
        }
        
        // Early stopping if we have found all possible answers
        bool allFound = true;
        for(int i = 0; i < N; i++) {
            if(answer[i] == 0) {
                allFound = false;
                break;
            }
        }
        if(allFound && len >= *min_element(answer.begin(), answer.end())) {
            break;
        }
    }
    
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string S;
    cin >> S;
    
    vector<int> result = solve(S);
    for(int i = 0; i < result.size(); i++) {
        cout << result[i] << (i == result.size()-1 ? '\n' : ' ');
    }
    
    return 0;
}