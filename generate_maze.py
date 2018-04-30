import maze
from random import randint


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    # TODO: Implement create_dfs
    history = []
    cell = randint(0, m.total_cells - 1)    # Starting index
    visited_cells = 1

    while visited_cells < m.total_cells:
        unvisited = m.cell_neighbors(cell)
        neighbor_len = len(unvisited)
        if(neighbor_len > 0):
            neighbor = unvisited[randint(0, neighbor_len - 1)]
            new_cell = neighbor[0]
            compass = neighbor[1]
            m.connect_cells(cell, new_cell, compass)

            history.append(cell)
            cell = new_cell
            visited_cells += 1

        else:
            cell = history.pop()

        m.refresh_maze_view()
    m.state = 'solve'

def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
