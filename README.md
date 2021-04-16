# Multi-tasking with Python

This repo contains examples on how to use the threading and multiprocessing builtin modules in Python.

Normal Python code runs in a single-core, single-thread fashion, which might be okay in many cituations, but in some other, it just doesn't make sense to run all code sequentially.

Here comes multi-tasking. We say that someone is multi-tasking when they're doing multiple tasks **at the same time**. So we can say that multi-taskingin Python is when we make our code do multiple tasks at the same time.

Multi-tasking could be achieved in two seemingly similar but different manners:

- **Multi-processing**: We often hear the words "Dual-core", or "Quad-core", ..., whenever we're talking about a CPU. The "Quad-core" for example means that the CPU has 4 physical CPUs inside of it all running at the same time sharing tasks. Multi-processing is the process of optimizing tasks to run simultaneously each on a seperate core. This gives us an advantage in terms of speed(reducing runtime). Beware though of codes that are sharing ressources since the data-transfer between cores should be managed by the programmer(You!).

- **Multi-threading**: Similarly to Multi-processing, we often hear the words "Quad-core, 8 Threads" when talking about CPUs. Threads are virtual Cores(CPUs) that live on a physical Core(CPU). They're used also to speed up processes but in Python, multi-threading doesn't exactly run tasks simultaneously, instead it sequentially jumps between tasks without waiting for one to finish and end up saving idle times. Since multi-threading runs on the same core, the problems of data-transfer between cores that arises in the multiprocessing case isn't present.

---

[Multi-processing VS Multi-threading](https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/)

[Multiprocessing tutorial with RAY(parallel/distributed computing with Python)](https://towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8) 
