AutoRL-Zyara: Warehouse Navigation System
Overview
This project implements an autonomous warehouse navigation system where an agent efficiently moves from a starting position to a goal location while avoiding obstacles (e.g., shelves). The system utilizes the A algorithm* for optimal pathfinding, enhanced by Deep Q-Network (DQN) for adaptive decision-making and Particle Swarm Optimization (PSO) for path refinement. Real-time visualization is provided using Pygame, with potential integration into a 3D warehouse environment.

Key Features
A Pathfinding*: Computes the shortest obstacle-free path using Manhattan distance heuristics.

DQN Reinforcement Learning: Enhances navigation through dynamic learning, improving decision-making over time.

PSO Optimization: Optimizes path selection by minimizing unnecessary movements and avoiding collisions.

Real-Time Visualization: Interactive Pygame-based simulation of the warehouse layout, agent movement, and obstacles.

Technologies Used
Python (Core implementation)

Pygame (Visualization)

NumPy (Numerical computations)

TensorFlow/Keras (DQN model training)

SciPy (PSO optimization)

Installation
Ensure Python is installed (3.7+ recommended).

Install required dependencies:

bash
Copy
pip install pygame numpy tensorflow scipy  
How to Run
Place the warehouse background image (3d_ware.jpg) in the project directory.

Execute the script:

bash
Copy
python warehouse_pathfinding.py  
Input the target product's row and column.

Observe the agent navigating to the destination while avoiding obstacles.

Algorithm Details
A Pathfinding*
Uses a priority queue (Min-Heap) to explore the lowest-cost path.

Heuristic calculation via Manhattan distance.

Obstacle avoidance by treating shelves as blocked cells.

DQN-Based Adaptive Navigation
State Space: Agent position and possible moves.

Reward Function: Penalizes collisions and rewards efficient movement.

Epsilon-Greedy Policy: Balances exploration and exploitation.

PSO-Based Path Optimization
Particles represent potential paths, evolving toward an optimal solution.

Fitness Function: Minimizes path length and collision risk.

Iterative refinement of particle velocities and positions.

Future Enhancements
Dynamic Obstacle Avoidance: Real-time detection and navigation around moving obstacles.

Warehouse Layout Optimization: Improved shelf placement for faster retrieval.

Multi-Agent Coordination: Scalable navigation for multiple autonomous agents.
