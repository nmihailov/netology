
# coding: utf-8

# In[4]:


class Animal():
    voice = ''
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight #Кг
            
    def to_feed(self, feed):  #Корм в килограммах 
        self.weight += feed

    def say_something(self):
        print(self.voice)
        
        
class Bird(Animal):
    def give_me_x_eggs(self, x):
        if x <= 3:
            self.weight -= 0.1 * x
        else:
            self.weight -= 0.1 * 3
            print('У меня нет столько яиц братан, держи {} и заходи в другой раз'.format(3))
    
    def give_me_egg(self): 
        self.weight -= 0.1


class Milking_animals(Animal): 
    
    def milking(self):
        self.weight -= 5

        
class Goose(Bird):
    voice = 'ШШШШШШшшшшшшш!!'

    
class Cow(Milking_animals):
    voice = 'Мууууу!!!'
        

class Sheep(Animal):
    voice = 'Бeee!!'
    
    def shearing(self):
        self.weight -= 5
        
        
class Chicken(Bird):
    voice = 'Ко-ко-ко!'
    
    
class Goat(Milking_animals):
    voice = 'Мееее!!'
    
    
class Duck(Bird):
    voice = 'Кря-кря!'
    
    
        
goose1 = Goose('Серый', 10)
goose2 = Goose('Белый', 5)
cow = Cow('Манька', 450)
sheep1 = Sheep('Барашек', 45)
sheep2 = Sheep('Кудрявый', 50)
chiken1 = Chicken('Ко-Ко', 1)
chiken2 = Chicken('Кукареку', 1.2)
goat1 = Goat('Рога', 30)
goat2 = Goat('Копыта', 35)
duck = Duck ('Кряква', 1)


#Пример, демонстрирующий успешное наследование всех процедур
print('Сейчас {} весит {}Кг'.format(duck.name, duck.weight))
print('И говорит:')
duck.say_something()
x = int(input('Введите количество яиц:'))
print('')
duck.give_me_x_eggs(x)
print('После сбора яиц {} весит {}Кг'.format(duck.name, duck.weight))
print('')

#Кормежка
goose1.to_feed(1.5)
goose2.to_feed(1.5)
cow.to_feed(10)
sheep1.to_feed(5) 
sheep2.to_feed(5)
chiken1.to_feed(1)
chiken2.to_feed(1)
goat1.to_feed(3) 
goat2.to_feed(3)
duck.to_feed(1)

#Процедуры
goose1.give_me_egg()
goose2.give_me_egg()
cow.milking()
sheep1.shearing()
sheep2.shearing()
chiken1.give_me_egg()
chiken2.give_me_egg()
goat1.milking()
goat2.milking()


our_farm = {goose1.name: goose1.weight, goose2.name: goose2.weight, cow.name: cow.weight, sheep1.name: sheep1.weight, 
        sheep2.name: sheep2.weight, chiken1.name: chiken1.weight,  chiken2.name: chiken2.weight, goat1.name: goat1.weight,
        duck.name: duck.weight}
print('Наша ферма', our_farm)

#Подсчёт веса
wt = 0
for key in our_farm.keys():
    wt += our_farm[key]

print('Общий вес зверей = {}Кг'.format(wt))
print('')

#Максимум веса
maximum = 0
for key in our_farm.keys():
    if our_farm[key] > maximum:
        name = key
        maximum = our_farm[key]

print('Самого тяжелого персонажа на ферме зовут', name)


