class Factory:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

class Chief(Factory):
    position = 'Директор'

class Secretary(Factory):
    position = 'Бухгалтер'

class Worker(Factory):
    position = 'Рабочий'

director = Chief('Иван Степаныч', 5000)
manager = Secretary('Людмила', 4500)
welder = Worker('Анатолич', 2000)

name_rate_dir = []
name_rate_dir.append(director.name)
name_rate_dir.append(director.rate)
name_rate_man = []
name_rate_man.append(manager.name)
name_rate_man.append(manager.rate)
name_rate_wel = []
name_rate_wel.append(welder.name)
name_rate_wel.append(welder.rate)

position_employe = {}
position_employe[director.position] = name_rate_dir
position_employe[manager.position] = name_rate_man
position_employe[welder.position] = name_rate_wel

