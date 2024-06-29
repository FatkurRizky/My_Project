import mysql.connector
from mysql.connector import Error

def database():
    try:
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "toko_online"
        )
        return db
            
    except Error as e:
        print(f"Error : {e}")

def table_supply():
    db = database()
    try:
        cursor = db.cursor()
        cursor.execute (
            """CREATE TABLE IF NOT EXISTS supplier(
                id INT(12) AUTO_INCREMENT PRIMARY KEY,
                nama VARCHAR(255),
                barang VARCHAR(255)
            ) 
            
            """
            )
        print("Table berhasil dibuat")
    except Error as e:
        print(f"Error {e}")

def table_user():
    db = database()
    try:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user(
                id_user INT AUTO_INCREMENT PRIMARY KEY,
                nama VARCHAR(255)
                
                )""")
        print("Tabel sudah terbuat")
    except Error as e:
        print(f"Error : {e}")

def insert_supply(nama, barang):
    db = database()
    try:
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO supplier(
                nama, barang)
                VALUES (%s, %s)
            
            """,(nama, barang))
        db.commit()
    except Error as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        db.close()
        
def insert_user():
    db = database()
    try:
        cursor = db.cursor()
        nama = input("Masukkan nama: ")
        sql = "INSERT INTO user(nama = %s)"
        values = (nama,)
        cursor.execute(sql, values)
        db.commit()
        print("Data berhasil ditambahkan ke tabel user")
    except Error as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        db.close()

def update_suppyl(id, nama, barang):
    try:
        db = database()
        cursor = db.cursor()
        sql = "UPDATE supplier SET nama = %s, barang = %s WHERE id = %s"
        values = (nama, barang, id)
        cursor.execute(sql, values)
        db.commit()
        print(f"Data berhasil di update")
    except Error as e:
        print(f"Error : {e}")
    
    finally:
        cursor.close()
        db.close()
    
def delete_supplier(id):
    db = database()
    try:
        cursor = db.cursor()
        sql = "DELETE FROM supplier WHERE id = %s"
        cursor.execute(sql, (id,))
        db.commit()
        print(f"Data supplier dengan ID {id} berhasil dihapus")
    except Error as e:
        print(f"Error : {e}")

def show_supplier():
    db = database()
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM supplier")
        save = cursor.fetchall()
        for row in save:
            print(row)
    except Error as e:
        print(f"Error : {e}")
    finally:
        cursor.close()
        db.close()

