def print_number() -> None:
        for i in range(8):
            for j in range(i + 1, 9):
                for k in range(j + 1, 10):
                        print(f"{i}{j}{k}")

print_number()