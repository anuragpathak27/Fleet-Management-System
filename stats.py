import pygame
import heapq

# Constants
IMAGE_PATH = "3d_ware.jpg"
ROWS, COLS = 10, 18  # Grid Dimensions
CELL_SIZE = 60  # Size of each cell
WINDOW_SIZE = (COLS * CELL_SIZE, ROWS * CELL_SIZE)

# Colors
WHITE, GREEN, BLUE, ORANGE, RED = (
    (255, 255, 255), (0, 255, 0), (0, 0, 255), (255, 165, 0), (255, 0, 0)
)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# Load Warehouse Background
warehouse_image = pygame.image.load(IMAGE_PATH)
warehouse_image = pygame.transform.scale(warehouse_image, WINDOW_SIZE)

# Define Shelves
shelves = {(r, c) for r in [2, 3, 5, 6, 8] for c in range(1, COLS - 1)}
blocked_cells = shelves  # Only shelves are blocked

# A* Pathfinding Algorithm
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal):
    open_set = [(0, start)]
    came_from, g_score, f_score = {}, {start: 0}, {start: heuristic(start, goal)}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if neighbor in blocked_cells or not (0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS):
                continue
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return []

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]

def get_nearest_valid_spot(row, col):
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbor = (row + dr, col + dc)
        if neighbor not in blocked_cells and 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS:
            return neighbor
    return None

# User Input for Destination
while True:
    try:
        pr, pc = int(input("Enter product row (0-9): ")), int(input("Enter product column (0-17): "))
        goal = get_nearest_valid_spot(pr, pc) if (pr, pc) in blocked_cells else (pr, pc)
        if goal:
            break
        print("Invalid input. Try again.")
    except ValueError:
        print("Enter valid numbers within range.")

# Initialize Agent & Compute Path
start, agent = (0, 0), (0, 0)
path, path_index = a_star(start, goal), 0

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Agent Step-by-Step
    if path_index < len(path):
        agent = path[path_index]
        path_index += 1
    
    # Redraw Scene
    screen.blit(warehouse_image, (0, 0))
    for x in range(ROWS):
        for y in range(COLS):
            pygame.draw.rect(screen, GREEN, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    for pos in path:
        pygame.draw.circle(screen, BLUE, (pos[1] * CELL_SIZE + CELL_SIZE//2, pos[0] * CELL_SIZE + CELL_SIZE//2), 5)
    pygame.draw.rect(screen, BLUE, (agent[1] * CELL_SIZE, agent[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, ORANGE, (goal[1] * CELL_SIZE, goal[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()
    clock.tick(5)

pygame.quit()
