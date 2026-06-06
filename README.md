# VU-Smart-Navigator
Smart Route Finding System using Dijkstra Algorithm

A Python-based GUI application that finds the shortest route between locations inside a university campus using the Dijkstra Algorithm.

Project Overview

This project simulates a smart navigation system for a university campus. Users can select a starting location and a destination, and the system calculates the shortest path and total distance between them.

The application provides a graphical user interface (GUI) built with Tkinter and displays a campus map alongside the route information.

Features
Shortest path calculation using Dijkstra Algorithm
User-friendly GUI with Tkinter
Campus location selection using dropdown menus
Route visualization in text format
Animated journey simulation
Campus map display
Distance calculation in meters
Technologies Used
Python 3
Tkinter
Heapq (Priority Queue)
Pillow (PIL)
Dijkstra Algorithm
University Locations

The system currently includes:

Bus Stand
Washroom
Info Desk
Exit Gate
Main Gate
CSE Department
Garage
Canteen
Algorithm

The project uses the Dijkstra Shortest Path Algorithm.

Steps:

Initialize all distances as infinity.
Set source distance to 0.
Use a priority queue to select the nearest unvisited node.
Update neighboring node distances.
Repeat until the destination is reached.
Reconstruct the shortest route using parent nodes.
