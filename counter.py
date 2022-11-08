# Необходимо реализовать программный компонент-счётчик Counter, который
# сможет считать и не только. У компонента должно быть следующее поведение:
#  init (для установления начального значения внутреннего счётчика; по
# умолчанию счётчик инициализируется с нуля);
#  increment (для увеличения значения внутреннего счётчика на единицу);
#  decrement (для уменьшения значения внутреннего счётчика на единицу);
#  reset (обнуление значения внутреннего счётчика);
#  view или display (для просмотра текущего состояния счётчика).

class Counter:
    def __init__(self, value=0):
        self._value = value
        self._start_with = value

    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1

    def reset(self):
        self._value = self._start_with

    def __str__(self):
        return f"The current state of the counter is {self._value}."


counter1 = Counter()
counter1.increment()
counter1.increment()
print(counter1)

counter2 = Counter(5)
counter2.decrement()
counter2.decrement()
print(counter2)

