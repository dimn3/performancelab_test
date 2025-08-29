import sys

def main():
    if len(sys.argv) < 2:
        print("Запуск python task4.py nums.txt")
        exit()

    with open(sys.argv[1]) as f:
        nums = [int(line.strip()) for line in f if line.strip()]

    if not nums:
        print(0)
        exit()

    # находим медиану
    nums.sort()
    n = len(nums)
    median = nums[n // 2]

    # Считаем ходы
    moves = sum(abs(x - median) for x in nums)

    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()