class Drug:
    def using(self):
        pass


class Sibutramin(Drug):
    def using(self):
        return "Лекарство сибутрамин\n"\
               "Начальная доза составляет 10 мг/сут.\nПри недостаточной эффективности при применении в этой дозе" \
               " (снижение массы тела менее чем на 2 кг за 4 недели)\n" \
               "и при хорошей переносимости дозу повысить до 15 мг/сут.\n\n"\
               "При отсутствии эффекта при применении в дозе 15 мг/сут" \
               " (снижение массы тела менее 2 кг за 4 недели) лекарство следует отменить."


class Diet(Drug):
    def using(self):
        return "Метод лечения - диета.\nНужна консультация с диетологом"


class Liraglutid(Drug):
    def using(self):
        return "Метод лечения - лираглутид\n" \
               "Необходимы подкожные инъекции 1 раз в сутки\n" \
               "Начальная доза 0,6 мг в день"
