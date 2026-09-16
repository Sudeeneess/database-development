import psycopg2
from psycopg2.extras import RealDictCursor

class Group:
    def __init__(self, conn):
        self.conn = conn
        self.id = 0
        self.title = 'Не указано'

    def get_all(self):
        """Возвращает список всех групп."""
        sql = 'SELECT id, title FROM groups ORDER BY id;'
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def create(self, title: str):
        """Создает новую группу."""
        sql = 'INSERT INTO groups (title) VALUES (%s) RETURNING id;'
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, (title,))
                new_id = cursor.fetchone()[0]
                self.id = new_id
                self.title = title
                return new_id

class Student:
    def __init__(self, conn):
        self.conn = conn
        self.id = 0
        self.name = 'Не указано'
        self.surname = 'Не указана'
        self.patronymic = 'Не указано'
        self.group_id = 0
        self.group_name = 'Не указано'

    def get_by_id(self, student_id: int) -> bool:
        """Получает данные студента по ID."""
        sql = '''SELECT s.id, s.name, s.surname, s.patronymic, g.id AS group_id, g.title AS group_name
                 FROM students AS s 
                 JOIN groups AS g ON s.group_id = g.id 
                 WHERE s.id = %s'''
        
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sql, (student_id,))
            student = cursor.fetchone()
            
            if student:
                self.id = int(student['id'])
                self.name = student['name']
                self.surname = student['surname']
                self.patronymic = student['patronymic']
                self.group_id = student['group_id']
                self.group_name = student['group_name']
                return True
            return False

    def create(self, student_id: int, name: str, surname: str, patronymic: str, group_id: int):
        """Добавляет нового студента."""
        self.id = student_id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group_id = group_id

        sql = 'INSERT INTO students (id, name, surname, patronymic, group_id) VALUES (%s, %s, %s, %s, %s)'
        
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, (self.id, self.name, self.surname, self.patronymic, self.group_id))

    def update(self, student_id: int, name: str, surname: str, patronymic: str, group_id: int):
        """Редактирует данные существующего студента."""
        self.id = student_id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group_id = group_id

        sql = 'UPDATE students SET name=%s, surname=%s, patronymic=%s, group_id=%s WHERE id = %s'
        
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, (self.name, self.surname, self.patronymic, self.group_id, self.id))

    def delete(self, student_id: int):
        """Удаляет студента по ID."""
        sql = 'DELETE FROM students WHERE id = %s'
        
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, (student_id,))

    def __str__(self):
        return f"| ID: {self.id} | {self.surname} {self.name} {self.patronymic} | Группа: {self.group_name} |"