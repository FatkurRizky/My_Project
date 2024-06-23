import datetime 
import time



# Menu makanan
daftarMakanan = [
    ["Burger Cheese", 25000],
    ["Burger Extra Beef", 30000],
    ["Burger Big Extra Cheese", 35000],
    ["Fried Chicken", 25000],
    ["Nasi Goreng", 15000]
]
# Menu minuman
daftarMenuMinuman = [
    ["Matcha", 10000],
    ["Vanilla Late", 10000],
    ["Coffe", 10000],
    ["Thai Tea", 10000],
    ["Green Tea", 10000]
]



for index, menu in enumerate(daftarMakanan,start = 1):
    print(f"{index}. {menu[0]} -Rp.{menu[1]}")
    
for index, menu in enumerate(daftarMenuMinuman, start = len(daftarMenuMinuman) +1):
    print(f"{index}. {menu[0]} -Rp.{menu[1]}")
print("\n")
print("Jika anda VIP anda mendapat free Burger Cheese dan Fried Chicken \nTapi anda di kenakan biaya tambahan sebesar 10%")




# Menu Tambahan Makanan
print("\n")
print("Menu Tambahan Makanan\n")
menuTambahanMakanan = [
    ["Ayam Geprek" , 10000],
    ["Ayam Katsu", 10000],
    ["Penyet Ayam", 10000]
]

for index, menu in enumerate(menuTambahanMakanan,start = 11):
    print(f" {index}. {menu[0]} -Rp.{menu[1]}")

# Menu Tambahan Minuman
print("\n")
print("Menu Tambahan Minuman\n")
menuTambahanMinuman = [ ["Es Teh",10000],
                        ["Teh panas", 10000],
                        ["Es Jeruk",1000],
                        ["Jeruk Hangat",10000],]
for index, menu in enumerate(menuTambahanMinuman,start = len(menuTambahanMakanan)+11):
    print(f"{index}. {menu[0]} -Rp.{menu[1]}\n")



# Pesanan dan pelanggan
pelanggan = 1
riwayatPesanan = []
while True:
    # Waktu untuk Riwayat
    waktupesan = datetime.datetime.now()
    waktu_Buka = waktupesan.time()
    waktuTutup = datetime.time(0,43,59)
    # Layanan Vip
    print(f"hai pelanggan ke {pelanggan}")
    TamuVIP = str(input("apakah anda ingin menjadi tamu VIP??? (y/n) : "))
                
    pesan = []
    while True:
        
        pilihMenu = int(input("Masukkan kode menu : (ketik '0' untuk selesai memesan) : "))
        if pilihMenu == 0:
            break
        elif 1 <= pilihMenu <= len(daftarMakanan) + len(daftarMenuMinuman) + len(menuTambahanMakanan) + len(menuTambahanMinuman):
            for index,menu in enumerate(daftarMakanan + daftarMenuMinuman + menuTambahanMakanan + menuTambahanMinuman,start = 1):
                if index == pilihMenu:
                    pesan.append(menu)
                    print(f"Menu yang anda pilih {menu[0]} ")
                    break
        else:
            print("Kode yang anda masukkan salah")
    

# Total
    if pesan:
        print("\nBerikut adalah pesanan anda !!!")
        total = 0
        for item in pesan:
            print(f"{item[0]} -Rp.{item[1]}")
            total += item[1]
        print(f"\nRiwayat Pesanan")
        print(f"{waktupesan}")
        total = 0
        for riwayatPesanan in pesan:
            total += riwayatPesanan [1]
            print(f"pelanggan ke-{pelanggan} memesan {riwayatPesanan[0]} memesan {riwayatPesanan[1]}")
        print(f"TOTAL HARGA : Rp.{total}")
    
    else:
        print("Anda belum memesan !!!")
    
    
    if TamuVIP == "y":
        print("\nAnda adalah tamu VIP!")
        biayaTambahan = total * 0.1
        total_vip = total + biayaTambahan
        diskon = total * 0.05
        print(f"Total Harga (Biaya Tambahan sebesar 10%): Rp.{total_vip}")
    
        free_items = ["Burger Cheese" , "Fried Chicken"]
        for item in pesan:
            if item in free_items:
                print()
        print(f"Anda mendapat free {''.join(free_items[0])} dan {''.join(free_items[1])}")
        print(f"{waktupesan}")
    
    else:
        print(f"")


    print("Terima kasih sudah berkunjung di Burger King")
    print("\n")
    
    if waktu_Buka >= waktuTutup:
        print("TOKO KAMI TELAH TUTUP !!!")
        break    
    
    pelanggan+=1
    print("\n")           




