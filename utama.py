from toko import database,update_suppyl,insert_supply,insert_user,delete_supplier,show_supplier
db = database()

print("Menu")
print("1. Add suplier")
print("2. Hapus Supplier")
print("3. Show supplier")
print("4. Update data")
print("5. keluar")

def add():
    db = database()
    if db:
        while True:
            user = int(input("Pilih angka yang diatas "))
            if user == 1:
                nama = input("Masukkan nama :")
                barang = input("Masukkan barang :")
                insert_supply(nama,barang)
            elif user == 2:
                id = int(input("Masukkan id :"))
                delete_supplier(id)
            elif user == 3:
                print(show_supplier())
            
            elif user == 4:
                id = int(input("Masukkan ID supplier yang ingin diupdate: "))
                nama = input("Masukkan nama baru: ")
                barang = input("Masukkan barang baru: ")
                update_suppyl(id, nama, barang)
            elif user == 5:
                print("Terima kasih")
                break

if __name__ == "__main__":
    add()