import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading
import queue

# Thread-safe queue
q = queue.Queue()
searching = False

def run_search():
    global searching
    searching = True

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "Searching...\n")

    t = threading.Thread(target=execute_backend, daemon=True)
    t.start()

    root.after(100, process_queue)

def execute_backend():
    directory = dir_entry.get()
    word = word_entry.get()

    process = subprocess.Popen(
        ["./multithread_file_search"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    process.stdin.write(f"{directory}\n{word}\n")
    process.stdin.flush()
    process.stdin.close()

    for line in process.stdout:
        q.put(line)

    q.put("<<DONE>>")

def process_queue():
    global searching

    while not q.empty():
        msg = q.get()

        if msg == "<<DONE>>":
            searching = False
            return

        if searching:
            output_box.delete(1.0, tk.END)
            searching = False

        output_box.insert(tk.END, msg)
        output_box.see(tk.END)

    root.after(100, process_queue)

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Multithreaded File Search")

tk.Label(root, text="Directory Path:").pack(pady=(10, 0))
dir_entry = tk.Entry(root, width=60)
dir_entry.pack()

tk.Label(root, text="Search Word:").pack(pady=(10, 0))
word_entry = tk.Entry(root, width=30)
word_entry.pack()

tk.Button(root, text="Search", command=run_search).pack(pady=10)

output_box = scrolledtext.ScrolledText(root, width=90, height=20)
output_box.pack(padx=10, pady=10)

root.mainloop()
