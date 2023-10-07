import os
import time

def is_virtualized():
    num_iterations = 5
    cpuid_time = 0
    fyl2xp1_time = 0

    for _ in range(num_iterations):
        start_time = time.perf_counter()
        os.system("cpuid")  # Execute CPUID instruction
        end_time = time.perf_counter()
        cpuid_time += (end_time - start_time) * 1e6  # Convert to microseconds

        start_time = time.perf_counter()
        x = 2.0
        y = 3.0
        result = x * (y + 1.0)
        end_time = time.perf_counter()
        fyl2xp1_time += (end_time - start_time) * 1e6  # Convert to microseconds

    return fyl2xp1_time <= cpuid_time

if __name__ == "__main__":
    if is_virtualized():
        print("Virtualization or sandboxing detected.")
    else:
        print("No virtualization or sandboxing detected.")
