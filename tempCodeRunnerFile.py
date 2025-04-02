import pygame
import heapq
import random

GRID_SIZE = (20, 20)
CELL_SIZE = 30
WINDOW_SIZE = (GRID_SIZE[0] * CELL_SIZE, GRID_SIZE[1] * CELL_SIZE)

WHITE, BLACK, RED, GREEN, BLUE, ORANGE, GRAY, CYAN, GOLD, BROWN, PURPLE = (
    (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 165, 0), (200, 200, 200), (0, 255, 255), (255, 215, 0), (139, 69, 19), (160, 32, 240)
)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

def generate_obstacles():
    return {(random.randint(1, GRID_SIZE[0] - 2), random.randint(1, GRID_SIZE[1] - 2)) for _ in range(40)}
obstacles = generate_obstacles()

def generate_goal():
    return random.randint(0, GRID_SIZE[0] - 1), random.randint(0, GRID_SIZE[1] - 1)
goal = generate_goal()

def generate_checkpoints(num=3):
    return {(random.randint(1, GRID_SIZE[0] - 2), random.randint(1, GRID_SIZE[1] - 2)) for _ in range(num)}
checkpoints = generate_checkpoints()

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if neighbor in obstacles or not (0 <= neighbor[0] < GRID_SIZE[0] and 0 <= neighbor[1] < GRID_SIZE[1]):
                continue
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(open_set, (g_score[neighbor] + heuristic(neighbor, goal), neighbor))
    return []

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]

def draw_chessboard():
    for x in range(GRID_SIZE[0]):
        for y in range(GRID_SIZE[1]):
            color = WHITE if (x + y) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_obstacles():
    for obs in obstacles:
        pygame.draw.circle(screen, BROWN, (obs[0] * CELL_SIZE + CELL_SIZE // 2, obs[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

def draw_checkpoints():
    for checkpoint in checkpoints:
        pygame.draw.rect(screen, PURPLE, (checkpoint[0] * CELL_SIZE, checkpoint[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def display_message(message, color):
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(message, True, color)
    screen.blit(text, (10, 10))

def main():
    start = (0, 0)
    agents = [(0, 0), (GRID_SIZE[0] - 1, 0), (0, GRID_SIZE[1] - 1)]
    optimal_paths = [a_star(agent, goal) for agent in agents]

    path_indices = [0] * len(agents)
    agents_reached_goal = [False] * len(agents)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        for i, agent in enumerate(agents):
            if not agents_reached_goal[i]:
                if path_indices[i] < len(optimal_paths[i]):
                    agents[i] = optimal_paths[i][path_indices[i]]
                    path_indices[i] += 1
                else:
                    agents_reached_goal[i] = True

        draw_chessboard()
        draw_obstacles()
        draw_checkpoints()

        for path in optimal_paths:
            for pos in path:
                pygame.draw.rect(screen, GREEN, (pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, BLUE, (start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GOLD, (goal[0] * CELL_SIZE, goal[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        for agent in agents:
            pygame.draw.rect(screen, RED, (agent[0] * CELL_SIZE, agent[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if all(agents_reached_goal):
            display_message("🎯 All Agents Reached the Goal!", GREEN)

        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()