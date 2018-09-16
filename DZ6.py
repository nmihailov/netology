
# coding: utf-8

# In[1]:


def get_dict(filename):
    '''Запись из файла в словарь'''
    dish = []
    count_dishes = []
    list1 = ['ingredient', 'count', 'measure']
    with open(filename) as f:
        for line in f:
            if line == '\n':
                dish.append(f.readline().strip())
                count = int(f.readline())
                count_dishes.append([dict(zip(list1, next(f).strip().split(' | '))) for x in range(count)])
                
    cook_book = dict(zip(dish, count_dishes))
    return cook_book



def get_shop_list_by_dishes(dishes:list, person_count:int):
    dictionary = get_dict('dz.txt')
    ingredients = []
    meas_quan = []
    for meal in dishes:
        for key in dictionary.keys():
            if key == meal:
                for element in dictionary[key]:
                    ingredients.append(element['ingredient'])
                    meas_quan.append({'measure': element['measure'], 'quantity':int(element['count']) * person_count})
                
    shop_list = dict(zip(ingredients, meas_quan))
    return shop_list
        
            
get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2)

