import sys
# Запускать прогу через python task2.py ellipse.txt points.txt
def main():
    file1, file2 = sys.argv[1], sys.argv[2]

    with open(file1) as f:
        x0, y0 = map(float, f.readline().split())
        a, b = map(float, f.readline().split())

    with open(file2) as f:
        for line in f:
            if line.strip():
                x, y = map(float, line.split())
                v = ((x-x0)/a)**2 + ((y-y0)/b)**2
            
                if v == 1:
                    print(0)
                elif v < 1:
                    print(1)
                else:
                    print(2)

if __name__ == "__main__":
    main()