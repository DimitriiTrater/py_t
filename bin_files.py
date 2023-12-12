from typing import List, Tuple, Any


def get_data_from_txt(name_of_input_file: str) -> List[Tuple[str, int, bool]]:
    result: List[Tuple[Any[str, int, bool]]] = []
    with open(name_of_input_file, "r") as file:
        temp: List[str] = file.read().split()
        while (len(temp)):
            name: str = str(temp[0])
            cost: int = int(temp[1])
            promotion: bool = bool(temp[2])

            result.append((name, cost, promotion))

            temp.remove(temp[0])
            temp.remove(temp[0])
            temp.remove(temp[0])

    return result


def get_data_from_bin(name_of_input_file: str) -> List[Tuple[str, int, bool]]:
    result: List[Tuple[Any[str, int, bool]]] = []
    with open(name_of_input_file, "rb") as file:
        for line in file:
            temp_line: List[str] = line.decode()[:-1].split()
            name: str = str(temp_line[0])
            cost: int = int(temp_line[1])
            promotion: bool = bool(temp_line[2])
            result.append((name, cost, promotion))
    return result


if __name__ == "__main__":
    list_of_tuples: List[Tuple[str, int, bool]] = \
        get_data_from_txt("input.txt")

    print("From txt")
    print(list_of_tuples)
    print("Sorted from bin")
    list_of_tuples.sort()
    print(list_of_tuples)

    with open("text_first.txt", "w") as file:
        for tuple_of_items in list_of_tuples:
            for item in tuple_of_items:
                file.write(f"{str(item)} ")
            file.write("\n")

    with open("bin_file.bin", "wb") as file:
        for tuple_of_items in list_of_tuples:
            for item in tuple_of_items:
                file.write(f"{str(item)} ".encode())
            file.write("\n".encode())

    list_of_tuples = get_data_from_bin("bin_file.bin")

    print("From bin")
    print(list_of_tuples)
    print("Sorted from bin")
    list_of_tuples.sort(key=lambda x: x[1])
    print(list_of_tuples)

    with open("text_second.txt", "w") as file:
        for tuple_of_items in list_of_tuples:
            for item in tuple_of_items:
                file.write(f"{str(item)} ")
            file.write("\n")
