import heapq
import os
import asyncio
from socket import socket


input_path = "input/"
output_file_path = "../output/async_sorted_files/async_sorted"
open_files_dict = {}
os.chdir(input_path)
tasks = []

# Create separate tasks for sorting individual files, because those can be sorted simultaneously
def sort():
    loop = asyncio.get_event_loop()

    for file_path in os.listdir():
        current_file = open(file_path, "r")
        tasks.append(asyncio.Task(read_text_file(current_file, file_path)))

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    write_output()


# Read and sort each individual file
async def read_text_file(current_file,file_path):
    column = []
    for line in current_file:
        column.append(int(line.split("\n")[0]))

    column.sort()
    output_file = output_file_path + "_" + file_path.split("_")[1]
    new_file = open(output_file, "a")
    new_file.writelines(map("{}\n".format, column))
    new_file.close()
    current_file.close()




def write_output():
    os.chdir("../output/")
    output_file = "async_sorted.txt"

    sorted_file = open(output_file, 'w+')

    min_heap = []
    heapq.heapify(min_heap)
    os.chdir("async_sorted_files/")

    for file in os.listdir():
        if os.path.isfile(file):
            individual_file = open(file)
            val = individual_file.readline()
            open_files_dict[file] = individual_file
            tup = (int(val), file)
            heapq.heappush(min_heap, tup)


    while (len(min_heap) > 0):
        min_element = heapq.heappop(min_heap)
        sorted_file.write(str(min_element[0]) + '\n')
        next_number = open_files_dict[min_element[1]].readline()
        if next_number:
            heapq.heappush(min_heap, (int(next_number), min_element[1]))
        else:
            open_files_dict[min_element[1]].close()

    sorted_file.close()



sort()