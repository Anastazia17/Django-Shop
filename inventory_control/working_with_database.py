import sqlite3


def create_tables(db_path: str) -> None:
    """ Создание бд(если нет) и таблиц
    :param db_path: путь до файла бд
    """
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        cursor.executescript('''
        CREATE TABLE IF NOT EXISTS categories 
        (category_name VARCHAR(100) NOT NULL PRIMARY KEY, 
        category_description TEXT NOT NULL);

        CREATE TABLE IF NOT EXISTS units 
        (unit VARCHAR(100) NOT NULL PRIMARY KEY);

        CREATE TABLE IF NOT EXISTS positions 
        (position VARCHAR(100) NOT NULL PRIMARY KEY);
        

        CREATE TABLE IF NOT EXISTS goods 
        (good_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        good_name VARCHAR(100) NOT NULL,
        good_unit VARCHAR(100) NOT NULL,
        good_cat VARCHAR(100) NOT NULL,
        FOREIGN KEY (good_unit) REFERENCES units (unit),
        FOREIGN KEY (good_cat) REFERENCES categories (category_name));
        
        CREATE TABLE IF NOT EXISTS employees 
        (employee_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        employee_fio VARCHAR(255) NOT NULL,
        employee_position TEXT NOT NULL,
        FOREIGN KEY (employee_position) REFERENCES positions (position));
        
        CREATE TABLE IF NOT EXISTS vendors 
        (vendor_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
        vendor_name VARCHAR(100) NOT NULL,
        vendor_ownerchipform VARCHAR(100) NOT NULL,
        vendor_address  VARCHAR(255) NOT NULL,
        vendor_phone VARCHAR(16) NOT NULL,
        vendor_email VARCHAR(255) NOT NULL);
        ''')

        connection.commit()


if __name__ == '__main__':
    create_tables('./inventory_control.db')
