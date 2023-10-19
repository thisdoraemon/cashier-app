# import module
import json
import os


def load_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def save_data(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=0)


def print_produk(produk_data):
    max_name_length = max(len(name) for name in produk_data)
    print("=" * 16 + " List produk " + "=" * 16, "\n")
    for index, (product, details) in enumerate(produk_data.items(), start=1):
        print(details)  # debugging
        harga = details.get('harga', 0) # pakai default value
        stock_status = "(stok habis)" if "stok" not in details or details["stok"] == 0 else ""
        print(f"{index}. {product.ljust(max_name_length)} = {harga} {stock_status}")
    print("0. untuk keluar")
    print("=" * 45)


def print_pesanan(pesanannya, total):
    print("\n########## Detail Pesanan ##########")
    for product, quantity in pesanannya.items():
        subtotal = quantity * data[product]["harga"]
        print("----------------------------------")
        print("Menu   : ", product)
        print("Jumlah : ", quantity)
        print("Harga  : Rp", subtotal)
        print("----------------------------------")
    print("Total  : Rp", total)
    print("####################################")


file_path = "produk.json"
data = load_data(file_path)

pesanan = {}
total = 0

nama = input("Masukkan nama anda: ")
while True:
    try:
        os.system("cls")
        print("**********************************************")
        print(f"Selamat datang {nama} di rumah makan santuy")
        print("Silahkan pilih menu yang akan di beli")
        print("**********************************************")

        print_produk(data)

        nomer = int(input("Pilih nomer produk: "))
        if nomer == 0:
            break

        product = list(data.keys())[nomer - 1]
        if (data[product["stok"]]) == 1:
            continue

        jumlah = int(input("Berapa banyak? "))
        if jumlah < 1:
            continue

        if data[product]["stok"] < jumlah:
            print(f"Maaf stok {product} kami hanya tinggal: {data[product]['stok']}")
            tetap = input("Ingin tetap membeli dengan stok yang tersisa? (Y/N): ")
            if tetap.upper() == "Y":
                pesanan[product] = data[product]["stok"]
            else:
                continue
        else:
            pesanan[product] = pesanan.get(product, 0) + jumlah

        data[product]["stok"] -= jumlah
        total += data[product]["harga"] * jumlah
        print_pesanan(pesanan, total)

        lanjut = input("\nMau pesan lagi (Y/N)? ")
        if lanjut.upper() != "Y":
            break

    except (IndexError, ValueError):
        continue

if total:
    os.system("cls")
    print("     Proses Pembayaran Pesanan")
    print_pesanan(pesanan, total)

    uang = int(input("Masukkan uang anda: "))
    print("**************************************")
    if uang >= total:
        for product, quantity in pesanan.items():
            data[product]["stok"] -= quantity
        save_data(data, file_path)

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
