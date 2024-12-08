class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    def get_cpu(self):
        return self.__cpu
    def set_cpu(self, cpu):
        self.__cpu = cpu
    def get_memory(self):
        return self.__memory
    def set_memory(self, memory):
        self.__memory = memory
    def make_computations(self):
        if self.__cpu and self.__memory:
            result = self.__cpu * self.__memory # Example computation
            print(f"Вычисления выполнены: {result}")
        else:
            print("Недостаточно данных для вычислений.")
    def __str__(self):
        return f"Компьютер: CPU - {self.__cpu}, Memory - {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    def get_sim_cards_list(self):
        return self.__sim_cards_list
    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неверный номер сим-карты.")

    def __str__(self):
        return f"Телефон: Список сим-карт - {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Строится маршрут до {location}")

    def __str__(self):
        return f"Смартфон: {Computer.__str__(self)}, {Phone.__str__(self)}"
computer1 = Computer(4, 8)
phone1 = Phone(["Beeline", "MegaCom"])
smartphone1 = SmartPhone(8, 16, ["O!", "Beeline"])
smartphone2 = SmartPhone(16, 32, ["MegaCom"])
print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)
computer1.make_computations()
phone1.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Бишкек")
smartphone2.make_computations()


print(computer1 == smartphone1)
print(computer1 < smartphone1)
print(computer1 > smartphone2)
