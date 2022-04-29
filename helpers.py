def map_list(func, iterable):
    return list(map(func, iterable))


def read_input(file_name, func=str, sep='\n'):
    file_name = f"{file_name:02d}" if isinstance(file_name, int) else file_name
    with open(f"data/{file_name}.txt") as f:
        data = f.read().strip().split(sep)
        return map_list(func, data)
