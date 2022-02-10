// Daniel Lessa - Beecrowd | 1152

#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std; 
    
struct Grafo { 
  int V, E; 
  vector< pair<int, pair<int, int> > > edges; 
  
  Grafo(int V, int E) { 
    this->V = V; 
    this->E = E; 
  } 

  void addEdge(int u, int v, int w) { 
    edges.push_back(make_pair(w, make_pair(u, v))); 
  }   

  int kruskalMST(); 
}; 
  
struct DisjointSets { 
  int *parente, *rnk; 
  int n; 
  
  DisjointSets(int n) { 
    this->n = n; 
    parente = new int[n+1]; 
    rnk = new int[n+1]; 

    for (int i = 0; i <= n; i++) { 
      rnk[i] = 0; 
      parente[i] = i; 
    } 
  } 

  int find(int u) { 
    if (u != parente[u]) parente[u] = find(parente[u]); 
    return parente[u]; 
  } 

  void merge(int x, int y) { 
    x = find(x), y = find(y); 

    if (rnk[x] > rnk[y]) parente[y] = x; 
    else parente[x] = y; 

    if (rnk[x] == rnk[y]) rnk[y]++; 
  } 
}; 
  
int Grafo::kruskalMST() { 
  int mst_peso = 0; 
  sort(edges.begin(), edges.end());  
  DisjointSets ds(V); 

  vector< pair<int, pair<int, int> > >::iterator it; 
  for (it=edges.begin(); it!=edges.end(); it++) { 
    int u = it->second.first; 
    int v = it->second.second; 

    int set_u = ds.find(u); 
    int set_v = ds.find(v); 

    if (set_u != set_v) { 
      mst_peso += it->first;   
      ds.merge(set_u, set_v); 
    } 
  }
  return mst_peso; 
} 
  
int main() { 
  int V, E, s, d, peso; 
  V=1;
  E=1;

  while(true) {
    cin >> V;
    cin >> E;
    
    if (V==0 and E==0) break;
    
    Grafo g(V, E); 
    int peso_total = 0;
    
    for (int i=0;i<E;i++) {
      cin >> s >> d >> peso;
      g.addEdge(s,d,peso);
      peso_total = peso_total + peso;
    }
    
    int mst_peso = g.kruskalMST(); 
    cout << peso_total - mst_peso << endl; 
  }
  
  return 0; 
}