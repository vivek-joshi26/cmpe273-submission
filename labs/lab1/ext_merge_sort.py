import heapq
import os


input_path = "input/"
output_file_path = "../output/sorted_files/sorted"
open_files_dict = {}
os.chdir(input_path)


def sort():
    read_text_file()
    write_output()


# Read and sort each individual file
def read_text_file():
    for file_path in os.listdir():
        current_file = open(file_path, "r")
        column = []
        for line in current_file:
            column.append(int(line.split("\n")[0]))

        column.sort()
        output_file = output_file_path + "_" + file_path.split("_")[1]
        new_file = open(output_file, "a")
        new_file.writelines(map("{}\n".format, column))
        new_file.close()
        current_file.close()


# Create a min heap to read data from all the files, then remove the min value, and add the second element from the file whose element is removed, implemented k-way sort using min heap
def write_output():
    os.chdir("../output/")
    output_file = "sorted.txt"

    sorted_file = open(output_file, 'w+')

    min_heap = []
    heapq.heapify(min_heap)
    os.chdir("sorted_files/")

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