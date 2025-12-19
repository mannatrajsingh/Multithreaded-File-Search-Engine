# Multithreaded File Search Engine

A high-performance multithreaded file search engine implemented in C, designed to efficiently search for target keywords across large directory trees.

## Features
- Parallel file scanning using POSIX threads
- Thread-safe shared work queue using mutexes
- Supports searching in text and PDF files
- Real-time search progress and results display
- Optional Python-based frontend for user interaction

## Tech Stack
- **C** (POSIX Threads, Mutex Synchronization)
- **Python** (Frontend Interface)
- **Operating Systems Concepts**: Concurrency, Synchronization, Parallelism

## How It Works
1. Files are dynamically assigned to worker threads from a shared queue.
2. Mutex locks ensure safe access to shared resources.
3. PDF files are converted to text before keyword matching.
4. Results are streamed live as files are processed.

## Usage
```bash
gcc multithread_file_search.c -o multithread_file_search -lpthread
./multithread_file_search <directory_path> <keyword>
For GUI-based interaction:

python3 frontend.py

Learning Outcomes

Practical understanding of multithreading and synchronization

Experience with real-world concurrency challenges

Performance comparison between single-threaded and multithreaded execution
