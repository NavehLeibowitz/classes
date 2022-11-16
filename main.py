from datetime import date


class Dog:

    def __init__(self, name, size, birth_date, breed="unknown"):
        self.name = name.title()
        self.size = size
        self.breed = breed
        self.birth_date = birth_date

    def bark(self):
        print("woof!")

    def get_name(self):
        return self.name

    # def set_name(self, name):
    #     if 2 < len(name) < 30:
    #         self.name = name.title()
    #     else:
    #         print("Dog name should be between 2 and 30 characters")
    #
    def dog_years(self):
        today = str(date.today()).split("-")
        today = [int(x) for x in today]
        birth_date_list = self.birth_date.split("-")
        birth_date_list = [int(x) for x in birth_date_list]
        years = today[0] - birth_date_list[0]
        months = (today[1] - birth_date_list[1]) * 30
        days = today[2] - birth_date_list[2]
        months_days_part = (months + days) / (30 * 12)
        years_new = (years + months_days_part) * 7
        return years_new


dog1 = Dog("bini", 5, "2000-6-18")
print(dog1.dog_years())