from datetime import datetime, timedelta
import dat
# from enum import Enum
import openpyxl

class Schedule:
    def __init__(self):
        self.book = openpyxl.open('Raspisanie.xlsx', read_only=True)
        self.stud = True
        self.list_stud = self.book.worksheets[0]
        self.list_teach = self.book.worksheets[1]

    def num_week(self):
        # надо переделать, но мне лень
        return datetime.now().isocalendar().week + 1

    def num_week_tomorrow(self, i):
        # надо переделать, но мне лень
        return (datetime.now() + timedelta(days=i)).isocalendar().week + 1

    def num_today(self):
        return datetime.now().weekday()

    def num_tomorrow(self, i):
        return (datetime.today() + timedelta(days=i)).weekday()

    def form_schedule_day(self, groop: str, week: int, num: int):
        s = ''
        if self.stud:
            for i in range(7):
                # print(dat.day.get((week, num)))
                # print(dat.groop.get(groop))
                # print(self.list_stud[dat.day.get((week, num))][dat.groop.get(groop)].value)
                temp = self.list_stud[dat.day.get((week, num))+i][dat.groop.get(groop)].value
                if temp != None:
                    s += f'{i+1} пара: ' + str(temp) + '\n\n'

        return s if s else 'Походу пар нет...'

    def form_schedule_today(self):
        return self.form_schedule_day('ИПБ-22-1', self.check_week(), self.num_today())

    def form_schedule_tomorrow(self):
        return self.form_schedule_day('ИПБ-22-1', self.check_week_tomorrow(), self.num_tomorrow())

    # def form_schedule_week(self):
    #     for i in range(7):
    #         return self.form_schedule_day('ИПБ-22-1', self.check_week_tomorrow(i), self.num_tomorrow(i))

    def check_week(self):
        return self.num_week() % 2

    def check_week_tomorrow(self):
        return self.num_week_tomorrow() % 2
