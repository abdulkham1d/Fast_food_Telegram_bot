import sqlite3


def create_users_table():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT
    );
    ''')

    database.commit()
    database.close()


# create_users_table()


def create_carts_table():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id),
        total_price DECIMAL(12, 2) DEFAULT 0,
        total_products INTEGER DEFAULT 0

    );
    ''')
    database.commit()
    database.close()


# create_carts_table()


def create_cart_products_table():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart_products(
            cart_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR(30),
            quantity INTEGER NOT NULL,
            final_price DECIMAL(12, 2) NOT NULL,
            cart_id INTEGER REFERENCES carts(cart_id),

            UNIQUE(product_name, cart_id)
        );
    ''')
    database.commit()
    database.close()


# create_cart_products_table()


def create_categories_table():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name VARCHAR(20) NOT NULL UNIQUE
        );
    ''')
    database.commit()
    database.close()


# create_categories_table()


def insert_categories():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO categories(category_name) VALUES
    ('Cake 🍰'),
    ('Burger 🍔'),
    ('Fries 🍟'),
    ('Hotdog 🌭'),
    ('Taco 🌮'),
    ('Pizza 🍕'),
    ('Donut 🍩'),
    ('Popcorn 🍿'),
    ('Coke 🥤'),
    ('Icecream 🍨'),
    ('Cookie 🍪')
    ''')
    database.commit()
    database.close()


# insert_categories()


def create_products_table():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_name VARCHAR(30) NOT NULL UNIQUE,
        price DECIMAL (12, 2) NOT NULL,
        description VARCHAR(100),
        image TEXT,

        FOREIGN KEY(category_id) REFERENCES categories(category_id)

    );
    ''')
    database.commit()
    database.close()


# create_products_table()


def insert_products_table():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO products(category_id, product_name, price, description, image) VALUES
        (1, 'Chocolate Cake', 15990, 'Delicious chocolate layer cake', 'media/Cake/img.png'),
        (1, 'Vanilla Cake', 12490, 'Classic vanilla cake with creamy frosting', 'media/Cake/img_1.png'),
        (1, 'Red Velvet Cake', 17990, 'Rich red velvet with cream cheese frosting', 'media/Cake/img_2.png'),
        (1, 'Cheesecake', 14990, 'Creamy cheesecake with a graham cracker crust', 'media/Cake/img_3.png'),

        (2, 'Cheeseburger', 9990, 'Juicy beef burger with cheddar cheese', 'media/Burger/img.png'),
        (2, 'Chicken Burger', 8490, 'Grilled chicken patty with lettuce and mayo', 'media/Burger/img_1.png'),
        (2, 'Veggie Burger', 7990, 'Delicious veggie patty with fresh toppings', 'media/Burger/img_2.png'),
        (2, 'Bacon Burger', 10490, 'Beef burger topped with crispy bacon', 'media/Burger/img_3.png'),

        (3, 'French Fries', 3990, 'Crispy golden fries', 'media/Fries/img.png'),
        (3, 'Curly Fries', 4490, 'Seasoned curly fries with a crunchy texture', 'media/Fries/img_1.png'),
        (3, 'Sweet Potato Fries', 5490, 'Healthy and sweet fries', 'media/Fries/img_2.png'),
        (3, 'Cheese Fries', 5990, 'Fries topped with melted cheese', 'media/Fries/img_3.png'),

        (4, 'Classic Hotdog', 4990, 'Hotdog with mustard and ketchup', 'media/Hotdog/img.png'),
        (4, 'Cheese Hotdog', 5490, 'Hotdog with melted cheese and onions', 'media/Hotdog/img_1.png'),
        (4, 'Chili Hotdog', 6490, 'Hotdog topped with spicy chili', 'media/Hotdog/img_2.png'),
        (4, 'BBQ Hotdog', 5990, 'Hotdog with barbecue sauce', 'media/Hotdog/img_3.png'),

        (5, 'Beef Taco', 6990, 'Spicy beef taco with salsa', 'media/Taco/img.png'),
        (5, 'Chicken Taco', 7490, 'Grilled chicken taco with fresh veggies', 'media/Taco/img_1.png'),
        (5, 'Fish Taco', 8990, 'Crispy fish taco with cilantro lime', 'media/Taco/img_2.png'),
        (5, 'Veggie Taco', 6490, 'Vegetarian taco with guacamole', 'media/Taco/img_3.png'),

        (6, 'Margherita Pizza', 12990, 'Classic pizza with tomato and mozzarella', 'media/Pizza/img.png'),
        (6, 'Pepperoni Pizza', 14490, 'Pepperoni pizza with extra cheese', 'media/Pizza/img_1.png'),
        (6, 'Vegetarian Pizza', 13490, 'Pizza with fresh vegetables and cheese', 'media/Pizza/img_2.png'),
        (6, 'Hawaiian Pizza', 15990, 'Pizza with ham and pineapple', 'media/Pizza/img_3.png'),

        (7, 'Glazed Donut', 1990, 'Classic sweet glazed donut', 'media/Donut/img.png'),
        (7, 'Chocolate Donut', 2490, 'Donut covered in rich chocolate', 'media/Donut/img_1.png'),
        (7, 'Strawberry Donut', 2290, 'Donut with strawberry icing', 'media/Donut/img_2.png'),
        (7, 'Cinnamon Donut', 2190, 'Cinnamon-sugar donut', 'media/Donut/img_3.png'),

        (8, 'Butter Popcorn', 3490, 'Popcorn with buttery goodness', 'media/Popcorn/img.png'),
        (8, 'Caramel Popcorn', 4290, 'Sweet caramel-coated popcorn', 'media/Popcorn/img_1.png'),
        (8, 'Cheese Popcorn', 3990, 'Cheese-flavored popcorn', 'media/Popcorn/img_2.png'),
        (8, 'Spicy Popcorn', 4490, 'Hot and spicy popcorn', 'media/Popcorn/img_3.png'),

        (9, 'Coke', 1990, 'Classic Coca-Cola', 'media/Coke/img.png'),
        (9, 'Diet Coke', 1890, 'Sugar-free Coca-Cola', 'media/Coke/img_1.png'),
        (9, 'Coke Zero', 1790, 'Zero-sugar Coca-Cola', 'media/Coke/img_2.png'),
        (9, 'Coke Cherry', 2190, 'Cherry-flavored Coca-Cola', 'media/Coke/img_3.png'),

        (10, 'Vanilla Ice Cream', 4990, 'Classic vanilla ice cream', 'media/Icecream/img.png'),
        (10, 'Chocolate Ice Cream', 5490, 'Rich chocolate ice cream', 'media/Icecream/img_1.png'),
        (10, 'Strawberry Ice Cream', 5290, 'Strawberry-flavored ice cream', 'media/Icecream/img_2.png'),
        (10, 'Mint Chocolate Chip', 5790, 'Mint ice cream with chocolate chips', 'media/Icecream/img_3.png'),

        (11, 'Chocolate Chip Cookie', 1490, 'Soft cookie with chocolate chips', 'media/Cookie/img.png'),
        (11, 'Oatmeal Cookie', 1790, 'Oatmeal cookie with raisins', 'media/Cookie/img_1.png'),
        (11, 'Peanut Butter Cookie', 1990, 'Peanut butter flavored cookie', 'media/Cookie/img_2.png'),
        (11, 'Sugar Cookie', 1290, 'Classic sweet sugar cookie', 'media/Cookie/img_3.png')
    ''')

    database.commit()
    database.close()


# insert_products_table()


def first_select_user(chat_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE telegram_id = ?
    ''', (chat_id,))
    user = cursor.fetchone()
    database.close()
    return user


def first_register_user(chat_id, full_name):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(telegram_id, full_name) VALUES(?, ?)
    ''', (chat_id, full_name))
    database.commit()
    database.close()


def update_user_to_finish_register(chat_id, phone):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
        UPDATE users
        SET phone = ?
        WHERE telegram_id = ?
    ''', (phone, chat_id))
    database.commit()
    database.close()


def insert_to_cart(chat_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(user_id) VALUES
    (
    (SELECT user_id FROM users WHERE telegram_id = ?)
    )
    ''', (chat_id,))
    database.commit()
    database.close()


def get_all_categories():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM categories;
    ''')
    categories = cursor.fetchall()
    database.close()
    return categories


def get_products_by_category(category_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_id, product_name
    FROM products WHERE category_id = ?
    ''', (category_id,))
    products = cursor.fetchall()
    database.close()
    return products


def get_product_detail(product_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM products
    WHERE product_id = ?
    ''', (product_id,))
    product = cursor.fetchone()
    database.close()
    return product


def get_user_cart_id(chat_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_id FROM carts
    WHERE user_id = (SELECT user_id FROM users WHERE telegram_id = ?)
    ''', (chat_id,))
    cart_id = cursor.fetchone()[0]
    database.close()
    return cart_id


def insert_or_update_cart_product(cart_id, product, quantity, final_price):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()

    try:
        cursor.execute('''
        INSERT INTO cart_products(cart_id, product_name, quantity, final_price)
        VALUES(?, ?, ?, ?)
        ''', (cart_id, product, quantity, final_price))
        database.commit()
        return True
    except:
        cursor.execute('''
        UPDATE cart_products
        SET quantity = ?,
        final_price = ?
        WHERE product_name = ? AND cart_id = ?
        ''', (quantity, final_price, product, cart_id))
        database.commit()
        return False
    finally:
        database.close()


def update_total_product_total_price(cart_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    UPDATE carts
    SET total_products = (
    SELECT SUM(quantity) FROM cart_products
    WHERE cart_id = :cart_id
    ),
    total_price = (
    SELECT SUM(final_price) FROM cart_products
    WHERE cart_id = :cart_id
    )
    WHERE cart_id = :cart_id
    ''', {'cart_id': cart_id})
    database.commit()
    database.close()


def get_cart_products(cart_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_name, quantity, final_price
    FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products


def get_total_products_price(cart_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT total_products, total_price FROM carts WHERE cart_id = ?
    ''', (cart_id,))
    total_products, total_price = cursor.fetchone()  # (4, 120000)
    database.close()
    return total_products, total_price


def get_cart_product_for_delete(cart_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT cart_product_id, product_name
    FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    cart_products = cursor.fetchall()
    database.close()
    return cart_products


def delete_cart_product_from_database(cart_product_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products WHERE cart_product_id = ?
    ''', (cart_product_id,))
    database.commit()
    database.close()


def drop_cart_products_default(cart_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM cart_products
    WHERE cart_id = ?
    ''', (cart_id,))
    database.commit()
    database.close()


def orders_check():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders_check(
        order_check_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cart_id INTEGER REFERENCES carts(cart_id),
        total_price DECIMAL(12, 2) DEFAULT 0,
        total_products INTEGER DEFAULT 0,
        time_order TEXT,
        data_order TEXT
        );
        ''')
    database.commit()
    database.close()


# orders_check()


def order():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_check_id INTEGER REFERENCES orders_check(order_check_id),
        product_name VARCHAR(100) NOT NULL,
        quantity INETEGER NOT NULL,
        final_price DECIMAL(12, 2) DEFAULT 0
    );
    ''')
    database.commit()
    database.close()


# order()


def save_order_check(cart_id, total_products, total_price, time_order, data_order):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders_check(cart_id, total_products, total_price, time_order, data_order)
    VALUES (?, ?, ?, ?, ?)
    ''', (cart_id, total_products, total_price, time_order, data_order))
    database.commit()
    database.close()


def get_order_check_id(cart_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT order_check_id FROM orders_check
    WHERE cart_id = ?
    ''', (cart_id,))
    order_check_id = cursor.fetchall()[-1][0]
    database.close()
    return order_check_id


def save_order(order_check_id, product_name, quantity, final_price):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO orders(order_check_id, product_name, quantity, final_price)
    VALUES (?, ?, ?, ?)
    ''', (order_check_id, product_name, quantity, final_price))
    database.commit()
    database.close()


def get_order_check(cart_id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM orders_check
    WHERE cart_id = ?
    ''', (cart_id,))
    order_check_info = cursor.fetchall()
    database.close()
    return order_check_info


def get_detail_order(id):
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('''
        SELECT product_name, quantity, final_price FROM orders
        WHERE order_check_id = ?
    ''', (id,))
    detail_order = cursor.fetchall()
    database.close()
    return detail_order