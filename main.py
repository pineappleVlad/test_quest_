from PIL import Image

# Размер поля
width, height = 1024, 1024

# Создание пустого поля (белого)
image = Image.new('1', (width, height), 1)

# Начальная позиция муравья и начальное направление (вверх)
x, y = 512, 512
direction = 'up'

# Число черных клеток
black_cell_count = 0

# Маппинг направлений
directions = {
    'up': (0, -1),
    'right': (1, 0),
    'down': (0, 1),
    'left': (-1, 0)
}

# Функция для инвертирования пикселя
def invert_pixel(x, y):
    pixel = image.getpixel((x, y))
    image.putpixel((x, y), 1 - pixel)

# Движение муравья
for _ in range(30000):  # Выполняем большое количество шагов (можно уменьшить)
    # Получаем текущее значение клетки
    current_pixel = image.getpixel((x, y))

    if current_pixel == 1:  # Белая клетка
        direction = {
            'up': 'right',
            'right': 'down',
            'down': 'left',
            'left': 'up'
        }[direction]
        invert_pixel(x, y)
        x += directions[direction][0]
        y += directions[direction][1]
    else:  # Черная клетка
        direction = {
            'up': 'left',
            'left': 'down',
            'down': 'right',
            'right': 'up'
        }[direction]
        invert_pixel(x, y)
        x += directions[direction][0]
        y += directions[direction][1]
        black_cell_count += 1

# Сохранение изображения
image.save("ant_path.bmp")

with open("black_cell_count.txt", "w", encoding="UTF-8") as f:
    f.write(f'Число черных клеток: {black_cell_count}')
print("Число черных клеток:", black_cell_count)
