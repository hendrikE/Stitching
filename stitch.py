import os
import sys
import csv


def stitching(directory):
    files = os.listdir(directory)
    files = [file for file in files if file.endswith(".txt")]
    lines = []
    for file in files:
        with open(os.path.join(directory, file), "r") as loaded_file:
            for line in loaded_file:
                elements = line.split("\t")
                time = float(elements[0])
                value = float(elements[1].replace("\n", ""))
                lines.append((time, value))

    sorted_lines = sorted(lines, key=lambda x: x[0])

    with open(os.path.join(directory, "results.csv"), "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(("time", "energy"))
        for line in sorted_lines:
            writer.writerow(line)


if __name__ == "__main__":
    try:
        dir_name = sys.argv[1]
    except IndexError:
        dir_name = "model_1"
    stitching(dir_name)
