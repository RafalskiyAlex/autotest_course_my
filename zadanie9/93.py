# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
a=open('test_file/task_3.txt', encoding='utf-8')
p=a.readlines()
spisok=[]
h=0
for i in p:
    if i[:-1] != '':
        h=h+ int(i[:-1])
    else:
        spisok.append(h)
        h=0
spisok.sort(reverse=True)
three_most_expensive_purchases = sum(spisok[:3])
print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346