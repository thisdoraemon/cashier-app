# Aplikasi Kasir Rumah Makan Santuy

Aplikasi kasir ini dibuat dengan Python dan menggunakan JSON untuk menyimpan data menu dan pesanan. Aplikasi ini memiliki fitur-fitur berikut:

* Menampilkan daftar menu berdasarkan kategori
* Menambahkan menu ke dalam keranjang
* Mengubah jumlah pesanan
* Menghapus menu dari keranjang
* Menampilkan detail pesanan
* Melakukan pembayaran

## Cara Menggunakan

Untuk menggunakan aplikasi ini, ikuti langkah-langkah berikut:

1. Jalankan file `main.py`.
2. Masukkan nama Anda.
3. Pilih kategori menu yang ingin Anda beli.
4. Pilih menu yang ingin Anda pesan.
5. Masukkan jumlah pesanan.
6. Ulangi langkah 3-5 untuk menambahkan menu lain ke dalam keranjang.
7. Tekan tombol `0` untuk menyelesaikan pemesanan.
8. Masukkan uang Anda.
9. Tunggu proses pembayaran.

## Dokumentasi

### Fungsi `save_data()`

Fungsi ini digunakan untuk menyimpan data ke file JSON.

### Fungsi `load_data()`

Fungsi ini digunakan untuk memuat data dari file JSON.

### Fungsi `print_menu()`

Fungsi ini digunakan untuk mencetak daftar menu berdasarkan kategori.

### Fungsi `print_pesanan()`

Fungsi ini digunakan untuk mencetak detail pesanan.

### Fungsi `main()`

Fungsi ini adalah fungsi utama aplikasi. Fungsi ini akan menjalankan aplikasi dari awal hingga akhir.

## Lisensi

Aplikasi ini dirilis di bawah lisensi MIT.
