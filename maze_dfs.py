vector<int> adj[N];
bool visited[N]

void dfs(int s) {
 if (visited[s]) return;
 visited[s] = true;
	 	 	 	 // обработать вершину s
 for (auto u: adj[s]) {
 dfs(u);
 }
}
