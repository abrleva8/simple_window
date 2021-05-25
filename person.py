class Person(object):

    def __init__(self, data):
        self.snils = data[0]
        self.pat = data[1]
        self.mzo = data[2]
        self.ohs = data[3]
        self.lpvp = data[4]
        self.lpnp = data[5]
        self.tg = data[6]
        self.height = data[7]
        self.hips_girph = data[8]
        self.glucose = data[9]
        # self.index_noma = 0
        # self.weight = 0
        # self.waist = 0
        # self.pulse = 0
        # self.insuline = 0
        pass

    def is_good_snils(self):
        try:
            number = float(self.snils)
        except ValueError:
            return False
        return True if number > 0 else False

    def is_good_ohs(self):
        try:
            number = float(self.ohs)
        except ValueError:
            return False
        return True if 2 <= number <= 9 else False

    def is_good_lpvp(self):
        try:
            number = float(self.lpvp)
        except ValueError:
            return False
        return True if 0 <= number <= 3 else False

    def is_good_lpnp(self):
        try:
            number = float(self.lpnp)
        except ValueError:
            return False
        return True if 1.5 <= number <= 5 else False

    def is_good_tg(self):
        try:
            number = float(self.lpnp)
        except ValueError:
            return False
        return True if 0.7 <= number <= 5 else False

    def is_good_height(self):
        try:
            number = float(self.height)
        except ValueError:
            return False
        return True if 150 <= number <= 200 else False

    def is_good_hips_girph(self):
        try:
            number = float(self.hips_girph)
        except ValueError:
            return False
        return True if 80 <= number <= 120 else False

    def is_good_glucose(self):
        try:
            number = float(self.glucose)
        except ValueError:
            return False
        return True if 4 <= number <= 7 else False

    def is_good_data(self):
        return self.is_good_snils() and self.is_good_ohs() and self.is_good_lpvp() and self.is_good_lpnp() \
               and self.is_good_tg() and self.is_good_height() and self.is_good_hips_girph() and self.is_good_glucose()
