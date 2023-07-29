from psycopg2 import connect

with connect('postgresql://anna23:password@127.0.0.1:5432/anndb') as conn:
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS categories(
                id SERIAL PRIMARY KEY,
                name VARCHAR(24) NOT NULL UNIQUE
                );
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY,
                title VARCHAR(36) NOT NULL,
                description VARCHAR(140),
                category_id INTEGER NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id)
                );
            ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(24) NOT NULL,
                email VARCHAR(24) NOT NULL UNIQUE
                );
            ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS statuses(
                id SERIAL PRIMARY KEY,
                name VARCHAR(10) NOT NULL UNIQUE
                );
            ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS orders(
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                status_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (status_id) REFERENCES statuses(id)
                );
            ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS order_items(
                id SERIAL PRIMARY KEY,
                order_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(id),
                FOREIGN KEY (product_id) REFERENCES products(id)
                );
            ''')
        conn.commit()
