import sqlite3

def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT(200) NOT NULL,
            price REAL(10, 2) NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_products(products):

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
    conn.close()

def change_quantity(product_id, new_quantity):

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()

def change_price(product_id, new_price):

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def get_all_products():

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def get_cheap_products(price_limit, quantity_limit):

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price < ? AND quantity > ?", (price_limit, quantity_limit))
    products = cursor.fetchall()
    conn.close()
    return products

def search_products(search_term):

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + search_term + '%',))
    products = cursor.fetchall()
    conn.close()
    return products


create_database()

new_products = [
    ("Молоко", 75.50, 10),
    ("Хлеб", 40.00, 20),
    ("Яйца", 80.00, 30),
    ("Сыр", 150.00, 5),
    ("Сахар", 60.00, 15),
    ("Мука", 55.00, 25),
    ("Масло", 200.00, 2),
    ("Крупа", 90.00, 12),
    ("Чай", 120.00, 8),
    ("Кофе", 250.00, 3),
    ("Соль", 30.00, 50),
    ("Перец", 45.00, 35),
    ("Картофель", 50.00, 100),
    ("Морковь", 60.00, 80),
    ("Лук", 40.00, 70)
]

add_products(new_products)
print("Товары добавлены:")
print(get_all_products())

change_quantity(1, 15)
print("\nКоличество товара с id=1 изменено:")
print(get_all_products())

change_price(2, 45.00)
print("\nЦена товара с id=2 изменена:")
print(get_all_products())

delete_product(3)
print("\nТовар с id=3 удален:")
print(get_all_products())

print("\nВсе товары:")
print(get_all_products())

print("\nДешевые товары (цена < 100, количество > 5):")
print(get_cheap_products(100, 5))

print("\nПоиск по названию 'молоко':")
print(search_products("молоко"))

