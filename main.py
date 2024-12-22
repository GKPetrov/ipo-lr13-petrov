from handlers.imagehandler import ImageHandler
from handlers.imageprocessor import ImageProcessor

def main_menu():
    # Функция для отображения меню и получения выбора пользователя
    print()
    print(" Меню работы с изображением ".center(80,"="))
    print("1. Изменить размер изображения на 200х200")
    print("2. Сохранить уменьшенное изображения")
    print("3. Применить фильтр")
    print("4. Добавить тест к изображению")
    print("5. Показать изображение")
    print("6. Выход")
    return input("Выберите действие: ")

def main():
    # Основная функция программы
    # Исходное изображение передаётся в коде
    initial_image_path = "image_4.jpg"  # Укажите путь к вашему изображению
    handler = ImageHandler(initial_image_path)
    handler.load_img()  # Загрузка изображения
    processor = ImageProcessor(handler.get_img())  # Создание процессора изображений

    print("Изображение успешно загружено из пути:", initial_image_path)

    while True:
        choice = main_menu()  # Отображение меню и получение выбора пользователя

        if choice == "1":
            if handler.img:
                temp_img =handler.size_img()
            else:
                print("Изображение не загружено.")

        elif choice == "2":
            if handler.img:
                handler.save_img(temp_img, 'new_image.jpg')
            else:
                print("Изображение не загружено.")

        elif choice == "3":
            if processor.img:
                processor.apply_filter()
                print("Фильтр применён.")
            else:
                print("Изображение не загружено.")

        elif choice == "4":
            # Добавление рамки к изображению
            if processor.img:
                processor.apply_text()
                print("Текст добавлен.")
            else:
                print("Изображение не загружено.")

        elif choice == "5":
            # Показ изображения
            if processor.img:
                processor.img.show()
            elif handler.img:
                handler.img.show()
            else:
                print("Изображение не загружено.")

        elif choice == "6":
            # Выход из программы
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()