from random_generator import RandomGenerator


def generate_insert_into_table(table_name: str, columns_info: dict, num_rows: int, generator: RandomGenerator):

    result = f"INSERT INTO {table_name} \n    ("

    # Create the INSERT INTO (COLUMNS) Query
    for col_name, col_values in columns_info.items():
        if "SERIAL" not in col_values[0]:
            result += f"{col_name}, "
    else:
        result = result[:-2] + ")\nVALUES"

    # INSERT THE RANDOM VALUES
    for _ in range(num_rows):

        temp = f"\n    ("
        # change if key == gender to check the first name and if it is in male names to give male gender

        for key, col_values in columns_info.items():
            if col_values[1] == generator.gender_generator:
              temp += f"{col_values[1](temp)}, "
            elif "SERIAL" not in col_values[0]:
                temp += f"{col_values[1]()}, "
        else:
            result += temp[:-2] + f"),"
    else:
        result = result[:-1] + f";"

    return result
