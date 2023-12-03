
def get_input(input_type, day, year):
    root_path = f"{year}/day-{day}"
    if input_type == 'test_p1':
        file_name = f'{root_path}/sample_input_p1.txt'
    elif input_type == 'test_p2':
        file_name = f'{root_path}/sample_input_p2.txt'
    elif input_type == 'prod':
        file_name = f'{root_path}/input.txt'
    else:
        raise Exception(f"Invalid input type {input_type}.")

    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if line[0] != '#']

    return lines