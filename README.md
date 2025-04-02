# Autonomous_Fleet_Management_System_for_Route_Optimization_using_Reinforcement_Learning_with_Warehouse_Cameras 

## Overview  
This project implements an intelligent warehouse navigation system where an autonomous agent efficiently moves from a starting position to a goal while avoiding obstacles (e.g., shelves). The system combines:  
- **A* algorithm** for optimal pathfinding.  
- **Deep Q-Network (DQN)** for adaptive reinforcement learning.  
- **Particle Swarm Optimization (PSO)** for path refinement.  

A real-time Pygame visualization simulates the warehouse environment, with potential integration into 3D warehouse systems.  

---

## Key Features  
✅ **A* Pathfinding**  
- Computes the shortest obstacle-free path using Manhattan distance.  
- Avoids static obstacles (shelves) by treating them as blocked cells.  

✅ **DQN Reinforcement Learning**  
- Trains the agent to make dynamic decisions via a state-space model.  
- Reward function penalizes collisions and encourages efficiency.  

✅ **PSO Optimization**  
- Optimizes path smoothness and minimizes detours.  
- Particles evolve iteratively to find collision-free routes.  

✅ **Real-Time Visualization**  
- Interactive Pygame interface displaying the warehouse grid, agent, and obstacles.  

---

## Technologies Used  
- **Python** (Core logic)  
- **Pygame** (Visualization)  
- **TensorFlow/Keras** (DQN implementation)  
- **NumPy & SciPy** (PSO and computations)  

---
