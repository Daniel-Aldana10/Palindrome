import sys
import matplotlib.pyplot as plt
from data import execution_time_gathering
def print_results(table):
    print("Size | palindrome (Time, Mem) | palindrome_pointers (Time, Mem) | palindrome_recursive  (Time, Mem)")
    for row in table:
        size, palindrome_time, palindrome_pointers_time, palindrome_recursive_time, palindrome_mem, palindrome_pointers_mem, palindrome_recursive_mem = row
        print(f"{size:<5} | [{palindrome_time}, {palindrome_mem}] | [{palindrome_pointers_time}, {palindrome_pointers_mem}] | [{palindrome_recursive_time}, {palindrome_recursive_mem}]")

def plot_results(table):
    sizes = [row[0] for row in table]
    palindrome_time = [row[1] for row in table]
    palindrome_pointers_time = [row[2] for row in table]
    palindrome_recursive_time = [row[3] for row in table]
    palindrome_mem = [row[4] for row in table]
    palindrome_pointers_mem = [row[5] for row in table]
    palindrome_recursive_mem = [row[6] for row in table]

    # Gráfico de tiempos de ejecución
    plt.figure(figsize=(10,5))
    plt.plot(sizes, palindrome_time, marker='o', label='palindrome')
    plt.plot(sizes, palindrome_pointers_time, marker='s', label='palindrome_pointers')
    plt.plot(sizes, palindrome_recursive_time, marker='^', label='palindrome_recursive')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time (ms)")
    plt.title("Execution Time of Palindrome Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

    # Gráfico de uso de memoria
    plt.figure(figsize=(10,5))
    plt.plot(sizes, palindrome_mem, marker='o', label='palindrome')
    plt.plot(sizes, palindrome_pointers_mem, marker='s', label='palindrome_pointers')
    plt.plot(sizes, palindrome_recursive_mem, marker='^', label='palindrome_recursive')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Memory Usage (bytes)")
    plt.title("Memory Usage of Palindrome Algorithms")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    minimum_size = 10000
    maximum_size = 100000
    step = 10000
    samples_by_size = 7
    table2 = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    print_results(table2)
    plot_results(table2)