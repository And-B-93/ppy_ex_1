from Accounting.Application.db.people import *

def calculated_salary():
    work_day = int(input('Введите количество рабочих дней за месяц: '))
    for position, name_rate in position_employe.items():
        if work_day == 22 and work_day <= 31:
            salary = work_day * name_rate[1] * 0.87
            print(f' {position} {name_rate[0]} получил {salary}')
        elif work_day > 22 and work_day <= 31:
            salary = (work_day * name_rate[1] + ((22 - work_day) * name_rate[1]*0.5) * 0.87)
            print(f'{position} {name_rate[0]} получил {salary}, включая премию за переработку {((work_day - 22) * name_rate[1] * 0.5) * 0.87}')
        elif work_day < 22:
            if name_rate[0] == director.name or name_rate[0] == manager.name:
                salary = work_day * name_rate[1] * 0.87
                print(f'{position} {name_rate[0]} получил {salary}')
            else:
                salary = (work_day * name_rate[1]) * 0.87 * 0.90
                print(f'{position} {name_rate[0]} получил {salary}, включая вычет за прогулы {salary - ((work_day * name_rate[1]) * 0.87)}')
        else:
            return 'error'