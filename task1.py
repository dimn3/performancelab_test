def main():
    import sys
    # Запуск через python task1.py n1 m1 n2 m2
    if len(sys.argv) != 5:
        print("Используйте python task1.py n1 m1 n2 m2")
        return
    
    try:
        n1 = int(sys.argv[1])
        m1 = int(sys.argv[2])
        n2 = int(sys.argv[3])
        m2 = int(sys.argv[4])

        def array(n, m):
            if n <= 0 or m <= 0:
                return "Аргументы должны быть больше 0"
            arr = list(range(1, n + 1))
            path = []
            current_index = 0

            while True:
                path.append(str(arr[current_index]))

                for i in range(m - 1):
                    current_index += 1

                    if current_index >= len(arr):
                        current_index = 0

                if current_index == 0:
                    break
            
            return ''.join(path)
        path1 = array(n1, m1)
        path2 = array(n2, m2)
        result = path1 + path2
        
        print(result)
    except:
        print("Ошибка. проверьте аргументы")

if __name__ == "__main__":
    main()