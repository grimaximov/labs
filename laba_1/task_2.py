# TODO Найдите количество книг, которое можно разместить на дискете

size = 1.44*1024*1024
symbols = 4*25*50*100
final_size = size//symbols


print("Количество книг, помещающихся на дискету:", int(final_size))
