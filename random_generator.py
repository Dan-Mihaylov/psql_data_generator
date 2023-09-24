import json
import random
from math import ceil


class RandomGenerator:

    def __init__(self):

        with open("data/names.json", "r") as file:
            self.names_info = json.load(file)

        self.male_first_names = self.names_info['male_names']

        self.female_first_names = self.names_info['female_names']

        self.last_names = self.names_info['last_names']

    def generate_first_name(self):

        choices = [self.female_first_names, self.male_first_names]
        current = choices[random.randint(0, 1)]

        return random.choice(current)

    def generate_last_name(self,):
        return random.choice(self.last_names)

    @staticmethod
    def age_generator():
        return random.randint(18, 90)

    def gender_generator(self, last_line: str):
        """
        The last_line we are getting is the temp string we have so far generated, then split it and replace the '('
        since if it is the first argument it will be in this form "\n    ('Peter'....."
        """
        split_list = last_line.split(",")

        for el in split_list:
            el = el.replace("\n", "")
            el = el.strip()
            el = el.replace("(", "")

            if el in self.male_first_names:
                return "'Male'"
            elif el in self.female_first_names:
                return "'Female'"
        else:
            return "NULL"

    @staticmethod
    def country_generator():

        with open("data/countries.json", "r") as file:
            retrieve_info = json.load(file)

        total_population = sum(retrieve_info["population"])
        result = []

        for i in range(len(retrieve_info["country"])):
            curr_country = retrieve_info["country"][i]
            curr_population = retrieve_info["population"][i]
            percentage = ceil(curr_population / total_population * 100)

            [result.append(curr_country) for _ in range(percentage)]

        return random.choice(result)
