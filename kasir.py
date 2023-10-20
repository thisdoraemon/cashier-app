import json
import os


# Fungsi untuk menyimpan data ke file JSON
def save_data(data, file_path):
    with open(file_path, "w") as outfile:
        json.dump(data, outfile)


# Fungsi untuk memuat data dari file JSON
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as infile:
            data = json.load(infile)
        return data
    else:
        return {}

def extract_category_name(category):
    if category.startswith("menu_"):
        return category[5:]  # Slice the string to remove "menu_"
    else:
        return category

# Fungsi untuk mencetak menu berdasarkan kategori
def print_menu(menu, jenis_menu):
    print("===================================")
    print(f"           Menu {extract_category_name(jenis_menu)}")
    print("===================================")
    for idx, item in enumerate(menu, 1):
        print(f"{idx}. {item} - Rp{menu[item]['harga']} - Stok: {menu[item].get('stok', 'Tidak ada info stok')}")
    print("0. Selesai Memesan")


# Fungsi untuk mencetak detail pesanan
def print_pesanan(pesanan, total, new_menu_data, kategori_menu):
    print("\n########## Detail Pesanan ##########")
    for item, quantity in pesanan.items():
        subtotal = quantity * new_menu_data[kategori_menu][item]["harga"]
        print("----------------------------------")
        print("Menu   : ", item)
        print("Jumlah : ", quantity)
        print("Harga  : Rp", subtotal)
        print("----------------------------------")
    print("Total  : Rp", total)
    print("####################################")


# Fungsi utama
def main():
    file_path = "produk.json"
    menu = load_data(file_path)
    new_menu_data = {}

    for key, value in menu.items():
        # Check if the key starts with "menu_"
        if key.startswith("menu_"):
            # Extract the part after "menu_"
            new_key = key[5:]
            # Store the value with the new key in the new menu_data dictionary
            new_menu_data[new_key] = value
        else:
            # If the key doesn't start with "menu_", keep it as is in the new dictionary
            new_menu_data[key] = value

    pesanan = {}
    total = 0

    nama = input("Masukkan nama anda: ")

    while True:
        os.system("cls")  # Ganti dengan "clear" jika menggunakan Linux/Mac

        print("**********************************************")
        print(f"Selamat datang {nama} di rumah makan santuy")
        print("Silahkan pilih menu yang akan dibeli")
        print("**********************************************")

        # Memilih kategori menu (menu_makanan atau menu_minuman)
        kategori_menu = input("Pilih kategori menu (makanan/minuman): ")
        if kategori_menu not in new_menu_data:
            print("Kategori menu tidak valid. Silakan coba lagi.")
            continue

        print_menu(new_menu_data[kategori_menu], kategori_menu)

        try:
            nomor = int(input("Pilih nomor menu: "))
            if nomor == 0:
                break
            elif nomor < 1 or nomor > len(new_menu_data[kategori_menu]):
                print("Nomor menu tidak valid. Silakan coba lagi.")
                continue

            item = list(new_menu_data[kategori_menu].keys())[nomor - 1]

            if "stok" not in new_menu_data[kategori_menu][item]:
                print("Maaf, stok untuk menu ini tidak tersedia.")
                continue

            stok = new_menu_data[kategori_menu][item].get("stok", 0)
            if stok == 0:
                print(f"Maaf, {item} sudah habis.")
                continue

            jumlah = int(input(f"Berapa banyak {item} yang akan dipesan? (Stok tersisa: {stok}): "))

            if jumlah < 1:
                print("Jumlah pesanan harus lebih dari 0.")
                continue
            elif jumlah > stok:
                print(f"Maaf, stok tidak mencukupi untuk pesanan ini.")
                continue

            pesanan[item] = pesanan.get(item, 0) + jumlah
            new_menu_data[kategori_menu][item]["stok"] -= jumlah
            total += new_menu_data[kategori_menu][item]["harga"] * jumlah

            print_pesanan(pesanan, total, new_menu_data, kategori_menu)

            lanjut = input("\nMau pesan lagi (Y/N)? ")
            if lanjut.upper() != "Y":
                break

        except (ValueError, IndexError):
            print("Input tidak valid. Silakan coba lagi.")

    if total > 0:
        os.system("cls")  # Ganti dengan "clear" jika menggunakan Linux/Mac
        print("     Proses Pembayaran Pesanan")
        print_pesanan(pesanan, total, new_menu_data, kategori_menu)

        uang = int(input("Masukkan uang anda: "))
        print("**************************************")
        if uang >= total:
            for item, quantity in pesanan.items():
                new_menu_data[kategori_menu][item]["stok"] -= quantity
            save_data(new_menu_data, file_path)

            print("Transaksi berhasil")
            if uang - total == 0:
                print("Uang anda pas")
            else:
                print(f"Kembalian anda adalah {uang - total}")
        else:
            print("Oops, uang yang anda miliki\ntidak cukup untuk membeli pesanan")
            print("Coba lain kali")
        print("**************************************")
        print("Terima kasih telah mengunjungi warung kami :)")
        print("Silahkan datang kembali\n")


if __name__ == "__main__":
    main()
