
CREATE TABLE countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL
);


INSERT INTO countries (title) VALUES
('Kyrgyzstan'),
('Germany'),
('China'),
('USA'); --Added for more data variety



CREATE TABLE cities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  area REAL DEFAULT 0,
  country_id INTEGER,
  FOREIGN KEY (country_id) REFERENCES countries(id)
);


INSERT INTO cities (title, area, country_id) VALUES
('Bishkek', 127.3, 1),
('Osh', 127.3, 1),
('Berlin', 891.8, 2),
('Beijing', 16410.5, 3),
('Shanghai', 6340.5, 3),
('Munich', 310.7, 2),
('New York', 783.8, 4);



CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  city_id INTEGER,
  FOREIGN KEY (city_id) REFERENCES cities(id)
);


INSERT INTO students (first_name, last_name, city_id) VALUES
('Ivan', 'Ivanov', 1),
('Petr', 'Petrov', 1),
('Maria', 'Sidorova', 2),
('Anna', 'Kuznetsova', 2),
('Dmitriy', 'Smirnov', 3),
('Elena', 'Egorova', 3),
('Sergey', 'Solovyov', 4),
('Olga', 'Belova', 4),
('Alexey', 'Fedorov', 5),
('Tatiana', 'Vinogradova', 5),
('Andrey', 'Mikhailov', 6),
('Natalia', 'Romanova', 6),
('Artem', 'Kozlov', 7),
('Yulia', 'Zaytseva', 7),
('Daniil', 'Volkov', 1);



import sqlite3

def show_students():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже. "
          "Для выхода из программы введите 0:")

    cursor.execute("""
        SELECT 
            ci.id,
            ci.title,
            c.title
        FROM cities ci
        INNER JOIN countries c ON ci.country_id = c.id
    """)
    cities = cursor.fetchall()
    for city_id, city_name, country_name in cities:
        print(f"{city_id}. {city_name}, {country_name}")

    while True:
        city_id_input = input("\nВведите id города (0 для выхода): ")
        if city_id_input == '0':
            break

        try:
            city_id = int(city_id_input)
            cursor.execute("""
                SELECT 
                    s.first_name, 
                    s.last_name,
                    c.title,
                    ci.title,
                    ci.area
                FROM students s
                INNER JOIN cities ci ON s.city_id = ci.id
                INNER JOIN countries c ON ci.country_id = c.id
                WHERE s.city_id = ?
            """, (city_id,))
            students = cursor.fetchall()
            if students:
                print("\nСписок учеников в этом городе:")
                for first_name, last_name, country, city, area in students:
                    print(f"Имя: {first_name}, Фамилия: {last_name}, Страна: {country}, Город: {city}, Площадь города: {area}")
            else:
                print("\nВ этом городе нет учеников.")
        except ValueError:
            print("Некорректный ввод. Введите числовое значение id.")
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    conn.close()

if __name__ == "__main__":
    show_students()



