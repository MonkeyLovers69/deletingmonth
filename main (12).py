months = ["jan,", "fab,", "march,", "apr,", "may,", "june,", "july,", "august,", "sept,", "octob,", "novem,", "dec"]
print(months)

index = int(input("Введите индекс элемента, который нужно удалить"))
del months[index]

print(months)
