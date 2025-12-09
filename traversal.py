# ===========================================
# MODULE: Traversal - Người số 4
# BFS + DFS chạy với GraphVisualizer của nhóm
# ===========================================

from collections import deque


# -----------------------
#        BFS
# -----------------------
def bfs(start, adj, node_pos, gui):
    """
    BFS traversal starting from node 'start'
    Compatible with:
    - adj: { node: [(neighbor, weight), ...] }
    - node_pos: { node: (x, y) }
    - gui.highlight_node(x, y, node)
    """

    visited = set()
    q = deque([start])
    order = []

    while q:
        u = q.popleft()

        if u not in visited:
            visited.add(u)
            order.append(u)

            # highlight node on GUI
            x, y = node_pos[u]
            gui.highlight_node(x, y, u)

            # push neighbors
            for (v, _) in adj[u]:
                if v not in visited:
                    q.append(v)

    return order



# -----------------------
#        DFS
# -----------------------
def dfs(start, adj, node_pos, gui):
    """
    DFS traversal starting from node 'start'
    Compatible with:
    - adj: { node: [(neighbor, weight), ...] }
    - node_pos: { node: (x, y) }
    """

    visited = set()
    order = []

    def dfs_visit(u):
        visited.add(u)
        order.append(u)

        # highlight on GUI
        x, y = node_pos[u]
        gui.highlight_node(x, y, u)

        # explore neighbors
        for (v, _) in adj[u]:
            if v not in visited:
                dfs_visit(v)

    dfs_visit(start)
    return order
