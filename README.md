# VU-Smart-Navigator
# Smart Route Finding System using Dijkstra Algorithm

A Python-based GUI application that finds the shortest route between locations inside a university campus using the Dijkstra Algorithm.

## Project Overview

This project simulates a smart navigation system for a university campus. Users can select a starting location and a destination, and the system calculates the shortest path and total distance between them.

The application provides a graphical user interface (GUI) built with Tkinter and displays a campus map alongside the route information.

## Features

- Shortest path calculation using Dijkstra Algorithm
- User-friendly GUI with Tkinter
- Campus location selection using dropdown menus
- Route visualization in text format
- Animated journey simulation
- Campus map display
- Distance calculation in meters

## Technologies Used

- Python 3
- Tkinter
- Heapq (Priority Queue)
- Pillow (PIL)
- Dijkstra Algorithm

## University Locations

The system currently includes:

- Bus Stand
- Washroom
- Info Desk
- Exit Gate
- Main Gate
- CSE Department
- Garage
- Canteen

## Algorithm

The project uses the Dijkstra Shortest Path Algorithm.

### Steps

1. Initialize all distances as infinity.
2. Set the source distance to 0.
3. Use a priority queue to select the nearest unvisited node.
4. Update neighboring node distances.
5. Repeat until the destination is reached.
6. Reconstruct the shortest route using parent nodes.

## Project Structure

```text
smart-route-finding/
│
├── lab4.py
├── map3.jpeg
├── README.md
└── screenshots/
```

## Sample Output

```text
From: Bus Stand
To: Canteen

Route:
Bus Stand ➜ Washroom ➜ CSE Dept ➜ Canteen

Distance: 75 m
```

## Future Improvements

- Interactive campus map
- Route highlighting on the map
- Animated route visualization
- Multi-floor navigation support
- Voice navigation support
- Database integration for dynamic locations


## Educational Purpose

This project was developed as part of an academic study to demonstrate the practical implementation of graph theory and shortest path algorithms in real-world navigation systems.

## Author

**Maruf Ul Haque**  
Department of Computer Science and Engineering  
Varendra University
