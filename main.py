import psycopg2
import config
from models import Student, Group

def main():
    try:
        conn = psycopg2.connect(
            dbname=config.DB_NAME,
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            port=config.DB_PORT,
            sslmode='prefer'
        )
    except Exception as e:
        print(f"Ошибка БД: {e}")
        return

    student = Student(conn)
    group = Group(conn)

    while True:
        print("\n1 - Информация о студенте")
        print("2 - Добавить студента")
        print("3 - Редактировать студента")
        print("4 - Удалить студента")
        print("5 - Показать список групп")
        print("6 - Создать новую группу")
        print("0 - Выход")
        
        action = input("Выберите действие: ")
        
        if action == '0':
            break

        try:
            if action == '1':
                s_id = int(input("ID студента: "))
                print(student if student.get_by_id(s_id) else "Студент не найден")

            elif action == '2':
                s_id = int(input("ID студента: "))
                name = input("Имя: ")
                surname = input("Фамилия: ")
                patronymic = input("Отчество: ")
                group_id = int(input("ID группы: "))
                student.create(s_id, name, surname, patronymic, group_id)
                print("Студент добавлен")

            elif action == '3':
                s_id = int(input("ID студента: "))
                name = input("Новое имя: ")
                surname = input("Новая фамилия: ")
                patronymic = input("Новое отчество: ")
                group_id = int(input("Новый ID группы: "))
                student.update(s_id, name, surname, patronymic, group_id)
                print("Данные студента обновлены")

            elif action == '4':
                s_id = int(input("ID студента: "))
                student.delete(s_id)
                print("Студент удален")

            elif action == '5':
                groups = group.get_all()
                if groups:
                    for g in groups:
                        print(f"ID: {g['id']} | Группа: {g['title']}")
                else:
                    print("Список групп пуст")

            elif action == '6':
                title = input("Название новой группы: ")
                new_id = group.create(title)
                print(f"Группа создана (ID: {new_id})")

            else:
                print("Неверная команда")

        except ValueError:
            print("Ошибка: в поля ID нужно вводить только числа")
        except Exception as e:
            print(f"Ошибка: {e}")

    conn.close()

if __name__ == "__main__":
    main()