import os

filepath = 'Data\portfolio.dat'


def pcost(file):
    cost = 0.0
    lists = []
    with open(file, 'r') as f:
        
        for lines in f:
            lists.append(lines.split())
        
        for items in lists:
            cost += int(items[1]) * float(items[2])
    return cost


if __name__ == "__main__":
    print(pcost(filepath))


# pcost.py solution 2

with open('Data\portfolio.dat', 'r') as f:
    total_cost = sum(int(line.split()[1]) * float(line.split()[2]) for line in f)
print(total_cost)