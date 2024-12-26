CREATE TABLE countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL
);

INSERT INTO countries (title) VALUES
('Кыргызстан'),
('Германия'),
('Китай');

CREATE TABLE cities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  area REAL DEFAULT 0,
  country_id INTEGER,
  FOREIGN KEY (country_id) REFERENCES countries(id)
);


INSERT INTO cities (title, area, country_id) VALUES
('Бишкек', 127.3, 1),
('Ош', 127.3, 1),
('Берлин', 891.8, 2),
('Пекин', 16410.5, 3),
('Шанхай', 6340.5, 3),
('Мюнхен', 310.7, 2),
('Кантон', 7434.4, 3);



CREATE TABLE students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  city_id INTEGER,
  FOREIGN KEY (city_id) REFERENCES cities(id)
);


INSERT INTO students (first_name, last_name, city_id) VALUES
('Иван', 'Иванов', 1),
('Петр', 'Петров', 1),
('Мария', 'Сидорова', 2),
('Анна', 'Кузнецова', 2),
('Дмитрий', 'Смирнов', 3),
('Елена', 'Егорова', 3),
('Сергей', 'Соловьев', 4),
('Ольга', 'Белова', 4),
('Алексей', 'Федоров', 5),
('Татьяна', 'Виноградова', 5),
('Андрей', 'Михайлов', 6),
('Наталья', 'Романова', 6),
('Артем', 'Коз', 7),
('Юлия', 'Зава', 7),
('Даниил', 'Волo', 1);


