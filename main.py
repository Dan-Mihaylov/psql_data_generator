import create_table, insert_into_table, random_generator
import os


class App:

    def __init__(self):
        self.query = ""

    def start_app(self):
        generator = random_generator.RandomGenerator()

        generators_available = {
            "first_name": generator.generate_first_name,
            "last_name": generator.generate_last_name,
            "age": generator.age_generator,
            "gender": generator.gender_generator,
            "country": generator.country_generator,
        }

        info = ("----      You will be asked to enter number of columns currently 1 <= num <= 5,      ----\n"
                "----      then you can choose your column NAME column TYPE and the random            ----\n"
                "----      generator to use.                                                          ----\n"
                "----      Suggested first column NAME == id, TYPE == SERIAL PRIMARY KEY               ----\n"
                )

        gen_info = (
                "---  Generators Supported  ---\n"
                "----      first_name      ----\n"
                "----      last_name       ----\n"
                "----      age             ----\n"
                "----      gender          ----\n"
                "----      country         ----\n")

        print(info)
        print(gen_info)

        col_num = int(input("Enter number of columns: "))
        col_info = []   # (name, type, generator)

        for _ in range(col_num):
            name = input("Enter column NAME: ").lower()
            type_ = input(f"Enter TYPE for column {name}: ").upper()
            print(f"\n{gen_info}")
            col_generator = input(f"Enter GENERATOR for column {name} (LEAVE BLANK IF TYPE == PRIMARY KEY): ")

            col_info.append((name, type_, generators_available[col_generator] if col_generator in generators_available
                            else None))

        table_name = input("Enter Table NAME: ")
        include_create_table = input(f"Include CREATE TABLE y/n: ").lower() == "y"
        rows = int(input("Amount Rows To Generate: "))

        columns = {}

        for el in col_info:
            col_name, col_type, col_gen = el
            columns[col_name] = (col_type, col_gen)

        if include_create_table:
            self.query += create_table.generate_create_table(table_name, columns)
            self.query += "\n\n"

        self.query += insert_into_table.generate_insert_into_table(table_name, columns, rows, generator)

        self.write_to_file()

    def write_to_file(self):
        home_dir = os.path.expanduser("~")
        desktop_path = os.path.join(home_dir, "Desktop")
        file_path = os.path.join(desktop_path, "query.sql")

        with open(file_path, "a") as file:
            file.writelines(self.query)


if __name__ == "__main__":
    my_app = App()
    my_app.start_app()
