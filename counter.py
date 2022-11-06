# Необходимо реализовать программный компонент-счётчик Counter, который
# сможет считать и не только. У компонента должно быть следующее поведение:
#  init (для установления начального значения внутреннего счётчика; по
# умолчанию счётчик инициализируется с нуля);
#  increment (для увеличения значения внутреннего счётчика на единицу);
#  decrement (для уменьшения значения внутреннего счётчика на единицу);
#  reset (обнуление значения внутреннего счётчика);
#  view или display (для просмотра текущего состояния счётчика).

#НЕ ПОЛУЧИЛОСЬ

class Counter:
    def __init__(self, count=0):
        self.count = count

    def increment(self):
        self.count+=1
        return self.count

    def decrement(self):
        self.count -=1
        return self.count

    def reset(self):
        self.count = 0
        return self.count

    def display(self):
        return f"The current state of counter is {self.count}. "


def main():
    counter1 = Counter(5)
    counter1.increment()
    counter1.increment()
    counter1.increment()
    print(counter1.display())
    counter1.decrement()
    print(counter1.display())
    counter1.reset()
    print(counter1.display())

    counter2 = Counter(0)
    counter2.increment()
    counter2.increment()
    print(counter2.display())


main()


