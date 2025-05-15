# Pac-Man UCS Pathfinding Game

This project demonstrates the **Uniform Cost Search (UCS)** algorithm by guiding Pac-Man through a grid from the start point `(0, 0)` to the goal `(4, 4)`. The grid contains normal cells, ghost zones with higher cost, and walls which are impassable.

## Features

- Grid-based map with:
  - 🟩 Normal cells (cost = 1)
  - 🟨 Near ghost zones (cost = 5)
  - ⬛ Walls (impassable)
- Visual animated pathfinding showing Pac-Man's movement step-by-step.
- Calculation and display of total path cost.
- Built with Python and Streamlit for easy interactive visualization.
