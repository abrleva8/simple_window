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
        self.sex = data[10]
        self.weight = data[11]
        self.waist = data[12]
        self.pulse = data[13]
        self.insuline = data[14]
        self.set_index_noma()

    def is_good_snils(self):
        if len(self.snils) != 14:
            return False

        if self.snils.count('-', 0, len(self.snils) - 1) != 2 or self.snils.count(' ', 0, len(self.snils) - 1) != 1:
            return False

        def snils_csum(snils):
            k = range(9, 0, -1)
            try:
                pairs = zip(k, [int(x) for x in snils.replace('-', '').replace(' ', '')[:-2]])
            except ValueError:
                return -1
            return sum([k * v for k, v in pairs])

        csum = snils_csum(self.snils)
        if csum == -1:
            return False
        else:
            while csum > 101:
                csum %= 101
            if csum in (100, 101):
                csum = 0

        return csum == int(self.snils[-2:])

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

    # def is_good_index_noma(self):
    #     try:
    #         number = float(self.index_noma)
    #     except ValueError:
    #         return False
    #     return True if 2 <= number <= 23 else False

    def is_good_weight(self):
        try:
            number = float(self.weight)
        except ValueError:
            return False
        return True if 70 <= number <= 160 else False

    def is_good_waist(self):
        try:
            number = float(self.waist)
        except ValueError:
            return False
        return True if 85 <= number <= 150 else False

    def is_good_pulse(self):
        try:
            number = float(self.pulse)
        except ValueError:
            return False
        return True if 50 <= number <= 100 else False

    def is_good_insuline(self):
        try:
            number = float(self.insuline)
        except ValueError:
            return False
        return True if 72 <= number <= 335 else False

    def set_index_noma(self):
        if self.is_good_insuline() and self.is_good_glucose():
            self.index_noma = float(self.insuline) * float(self.glucose) / 22.5

    def is_good_data(self):
        return self.is_good_snils() and self.is_good_ohs() and self.is_good_lpvp() and self.is_good_lpnp() \
               and self.is_good_tg() and self.is_good_height() and self.is_good_hips_girph() and self.is_good_glucose() \
               and self.is_good_weight() and self.is_good_waist() and self.is_good_pulse() \
               and self.is_good_insuline()

    def data_to_save(self):
        return f'??????????: {self.snils}\n' \
               f'??????: {self.sex}\n' \
               f'??????: {self.pat}\n' \
               f'??????/??????: {self.mzo} \n' \
               f'??????: {self.ohs} ??????????/??\n' \
               f'????????: {self.lpvp} ??????????/??\n' \
               f'????????: {self.lpnp} ??????????/??\n' \
               f'??????????????????????????: {self.tg} ????/????\n' \
               f'????????: {self.height} ????\n' \
               f'???????????? ??????????: {self.hips_girph} ????\n' \
               f'??????????????: {self.glucose} ??????????/??\n' \
               f'??????: {self.weight} ????\n' \
               f'???????????? ??????????: {self.waist} ????\n' \
               f'??????????: {self.pulse} ????/??????\n' \
               f'??????????????: {self.insuline} ????????/????\n' \
               f'????????????-????????: {round(self.index_noma, 2)} \n'

    def resulting_weight(self, num_per):
        return round(float(self.weight) * num_per / 100, 2)
