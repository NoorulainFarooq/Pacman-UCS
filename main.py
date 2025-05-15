import streamlit as st
import heapq
import time

# Grid setup: 0 = normal, 1 = near ghost, 9 = wall
grid = [
    [0, 0, 1, 0, 0],
    [0, 9, 9, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 9, 1, 9, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

cost_map = {
    0: 1,
    1: 5,
    9: float('inf')
}

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def ucs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = [(0, start, [])]  # (cost, position, path)

    while pq:
        cost, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)
        path = path + [current]

        if current == goal:
            return path, cost

        r, c = current
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != 9:
                    next_cost = cost + cost_map[grid[nr][nc]]
                    heapq.heappush(pq, (next_cost, (nr, nc), path))

    return None, float('inf')

def display_grid(grid, path=None, current_pos=None):
    emojis = {
        0: "🟩",  # normal
        1: "🟨",  # near ghost
        9: "⬛",  # wall
    }

    grid_display = ""
    for i, row in enumerate(grid):
        row_display = ""
        for j, cell in enumerate(row):
            if (i, j) == current_pos:
                row_display += "🧠"
            elif path and (i, j) in path:
                row_display += "🔵"
            else:
                row_display += emojis[cell]
        grid_display += row_display + "<br>"  # HTML break per row
    return f"<div style='font-size:30px; line-height:1.2'>{grid_display}</div>"


# Title and Legend
st.title("Pac-Man UCS Pathfinding Game 🧠")

st.markdown("""
Use **Uniform Cost Search (UCS)** to guide Pac-Man from the start `(0, 0)` to the goal `(4, 4)` on a grid with walls and ghost zones.

**Legend**:
- 🟩 Normal path (cost 1)  
- 🟨 Near ghost (cost 5)  
- ⬛ Wall (impassable)  
- 🔵 UCS path  
- 🧠 Pac-Man  
""")

# Run Game Button
if st.button("Run Game"):
    path, total_cost = ucs(grid, start, goal)
    container = st.empty()

    if path:
        st.success("Path found!")
        st.info(f"Total Cost: {total_cost}")

        for idx, pos in enumerate(path):
            grid_html = display_grid(grid, path=path[:idx+1], current_pos=pos)
            container.markdown(grid_html, unsafe_allow_html=True)
            time.sleep(0.5)

    else:
        st.error("No path found!")
