import tkinter as tk
from tkinter import ttk, messagebox
import heapq
from PIL import Image, ImageTk
import os
# =========================
# University Locations
# =========================
places = [
    "Bus Stand",
    "Washroom",
    "Info Desk",
    "Exit Gate",
    "Main Gate",
    "CSE Dept",
    "Garage",
    "Canteen"
]
# =========================
# Graph (Distance in Meter)
# =========================
graph = {
    0: [(1, 10), (2, 8), (3, 23)],
    1: [(0, 10), (2, 10), (5, 30)],
    2: [(0, 8), (1, 10), (4, 20), (3, 25)],
    3: [(0, 23), (2, 25), (4, 15)],
    4: [(2, 20), (5, 35), (6, 30), (3, 15)],
    5: [(1, 30), (4, 35), (7, 35)],
    6: [(4, 30)],
    7: [(5, 35)]
}
# =========================
# Dijkstra Algorithm
# =========================

def dijkstra(source, destination):
    n = len(places)
    distance = [float('inf')] * n
    parent = [-1] * n

    distance[source] = 0
    pq = [(0, source)]

    while pq:
        dist, current = heapq.heappop(pq)

        if dist > distance[current]:
            continue

        for neighbor, weight in graph[current]:
            new_distance = distance[current] + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current
                heapq.heappush(pq, (new_distance, neighbor))

    return distance, parent


# =========================
# Path Reconstruction
# =========================

def get_path(parent, destination):
    route = []

    while destination != -1:
        route.append(places[destination])
        destination = parent[destination]

    route.reverse()
    return route


# =========================
# Animation
# =========================

def animate_route(route, index=0):
    if index < len(route):
        result_area.insert(tk.END, f"🚶 Moving To: {route[index]}\n")
        result_area.see(tk.END)
        root.after(800, lambda: animate_route(route, index + 1))
    else:
        result_area.insert(tk.END, "\n✅ Destination Reached!\n")


# =========================
# Find Route
# =========================

def find_route():
    source = source_box.current()
    destination = destination_box.current()

    if source == destination:
        messagebox.showwarning("Warning", "Select different locations!")
        return

    distance, parent = dijkstra(source, destination)

    if distance[destination] == float('inf'):
        result_area.delete(1.0, tk.END)
        result_area.insert(tk.END, "No Route Found!")
        return

    route = get_path(parent, destination)

    result_area.delete(1.0, tk.END)
    result_area.insert(
        tk.END,
        "SMART ROUTE RESULT\n\n"
        f"From: {places[source]}\n"
        f"To: {places[destination]}\n"
        f"Distance: {distance[destination]} m\n\n"
        "Route:\n" + " ➜ ".join(route) + "\n\nJOURNEY:\n\n"
    )

    animate_route(route)


def clear_result():
    result_area.delete(1.0, tk.END)


# =========================
# GUI WINDOW
# =========================

root = tk.Tk()
root.configure(bg="#F5F7FA")
root.title("Smart Route Finder - Varendra University (1st Floor)")
root.geometry("1300x780")
root.resizable(False, False)

# =========================
# MAIN FRAME
# =========================

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

right_frame = tk.Frame(main_frame, width=350)
right_frame.pack(side="right", fill="y")

# =========================
# TITLE
# =========================

tk.Label(
    left_frame,
    text="VU Smart Navigator",
    font=("Segoe UI", 24, "bold"),
    fg="#1E3A8A"
).pack(pady=10)

# =========================
# INPUT
# =========================

frame = tk.Frame(left_frame)
frame.pack(pady=10)

tk.Label(frame, text="From:").grid(row=0, column=0, padx=5, pady=5)
source_box = ttk.Combobox(frame, values=places, state="readonly", width=25)
source_box.grid(row=0, column=1)
source_box.current(0)

tk.Label(frame, text="To:").grid(row=1, column=0, padx=5, pady=5)
destination_box = ttk.Combobox(frame, values=places, state="readonly", width=25)
destination_box.grid(row=1, column=1)
destination_box.current(1)

tk.Button(frame, text="Find Route", command=find_route).grid(row=2, column=0, pady=10)
tk.Button(frame, text="Clear", command=clear_result).grid(row=2, column=1, pady=10)

# =========================
# RESULT BOX
# =========================

result_area = tk.Text(left_frame, width=50, height=25, font=("Consolas", 11))
result_area.pack(pady=10)

# =========================
# IMAGE FIX (IMPORTANT PART)
# =========================

try:
    img_path = os.path.join(os.path.dirname(__file__), "map7.jpeg")
    img = Image.open(img_path)

    img = img.resize((600, 650))
    map_img = ImageTk.PhotoImage(img)

    map_label = tk.Label(right_frame, image=map_img)
    map_label.pack(padx=5, pady=10)

    map_label.image = map_img  # keep reference

except Exception as e:
    tk.Label(
        right_frame,
        text="Map image not found!\nPut map7.jpeg\nin same folder.",
        fg="red",
        font=("Arial", 10)
    ).pack(pady=20)

# =========================
# RUN
# =========================

root.mainloop()