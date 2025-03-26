import math
import datetime

diskon_kategori = {
    "Member": 0.10,  # 10% diskon
    "VIP": 0.20,  # 20% diskon
    "Umum": 0.05  # 5% diskon
}

harga_awal = float(input("Masukkan harga barang: Rp"))
kategori = input("Masukkan kategori (Member/VIP/Umum): ")

if kategori in diskon_kategori:
    diskon = diskon_kategori[kategori]
    harga_akhir = harga_awal - (harga_awal * diskon)
    harga_akhir = math.ceil(harga_akhir)  # Pembulatan ke atas
    print(f"Harga setelah diskon: Rp{harga_akhir}")
else:
    print("Kategori tidak valid!")

waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Waktu transaksi: {waktu}")
