class MyIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        else:
            number = self.current
            self.current += 1
            return number

    def count_down(self):
        for i in range(self.n, -1, -1):
            yield i


    def multiplier(self, m):
        def return_multiplier(y):
            return m * y
        return return_multiplier

def print_result(func):
    def wrapper(a, b):
       print(f"Результат работы декоратора: ", func(a, b))
    return wrapper

#----------------------------------
print("Результат работы итератора")
iterator = MyIterator(5)
for num in iterator:
    print(num)

print("Результат работы генератора")
for num in iterator.count_down():
    print(num)

print("Результат работы замыкания")
multiplier = iterator.multiplier(5)
print(multiplier(6))



@print_result
def add_numbers(a, b):
    return a+b

@print_result
def m_numbers(a, b):
    return a*b

add_numbers(5,10)
m_numbers(5,10)


iterator.count_down()
iterator.multiplier(5)