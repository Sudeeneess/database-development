from database_kino import engine, Base
import models_kino

def main():
    print("Создаем таблицы в базе данных kino_orm...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")

if __name__ == "__main__":
    main()