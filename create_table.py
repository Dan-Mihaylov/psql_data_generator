from random_generator import RandomGenerator


def generate_create_table(table_name: str, columns: dict):
    """
    :param table_name: The name of your table in Lowercase or if you need special characters use ""
    :param columns: a dict with the name of the columns and a tuple with their (type, generator).
    :return: str query for creating a table in sql
    """

    create_table = f'CREATE TABLE {table_name}('

    for col_name, col_type in columns.items():
        create_table += f'\n    {col_name} {col_type[0]},'
    else:
        create_table = create_table[:-1] + ');'

    return create_table

