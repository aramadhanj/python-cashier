# Project Super Cashier - Pacmann
## Latar Belakang
Pemilik supermarket ingin melakukan perbaikan proes bisnis dengan cara membuat sistem kasir yang self-service di supermarket miliknya.
## Tujuan
Sebuah sistem kasir dengan fitur berikut:
1. Menambahkan item belanja terdiri dari nama, jumlah, dan harga
2. Menghapus item belanja
3. Mengedit nama, jumlah, atau harga item
4. Menampilkan daftar item belanja
5. Menghitung total harga sebelum dan sesudah diskon.
## Feature Requirements
1. Customer dapat menambahkan nama, jumlah, dan harga yang ingin dibeli dengan method `add_item()`
2. Customer dapat mengubah nama, jumlah, atau harga item yang ingin dibeli dengan method `update_item_name()`, `update_item_qty()`, atau `update_item_price()`.
3. Customer dapat menghapus salah satu item belanja dengan method `delete_item()` atau menghapus seluruh item dengan method `reset_transaction()`.
4. Customer dapat mengecek pesanan dengan method `check_order()`.
5. Customer dapat menghitung total belanja dengan method `total_price()`.
## Cara menggunakan program dan alur Program
1. Download file `Cashier.ipynb` dan `supermarket.py`
2. Import file `supermarket.py` ke dalam `Cashier.ipynb` dengan cara `from supermarket import Cashier`
3. Jalankan file `Cashier.ipynb`
4. Customer memilih menu/ fitur yang ingin digunakan

![image](https://user-images.githubusercontent.com/61931377/232290777-2d304403-c18f-4ccf-940b-435b2d7c3f3b.png)

* Pilihan 1 : Customer menambahkan nama, jumlah, dan harga item yang ingin dibeli
* Pilihan 2 : Customer mengedit jumlah item yang ingin dibeli dengan parameter mencocokkan nama item yang diinputkan dengan nama item yang ada di daftar belanja
* Pilihan 3 : Customer mengedit nama item yang ingin dibeli dengan parameter mencocokkan nama item yang diinputkan dengan nama item yang ada di daftar belanja
* Pilihan 4 : Customer mengedit harga item yang ingin dibeli dengan parameter mencocokkan nama item yang diinputkan dengan nama item yang ada di daftar belanja
* Pilihan 5 : Customer menghapus salah satu item yang ada pada daftar belanja
* Pilihan 6 : Customer menampilkan daftar belanja
* Pilihan 7 : Customer mencetak total harga belanjaan
* Pilihan 8 : Customer menghapus seluruh item yang ada pada daftar belanja
* Pilihan 9 : Exit. Pemrograman berhenti

## Hasil Test Case
1. Test 1
Customer ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan sebagai berikut:
  * Nama item: Ayam Goreng, qty: 2, Harga: 20000
  * Nama item: Pasta Gigi, qty: 3, Harga: 
  
![image](https://user-images.githubusercontent.com/61931377/232291685-2cdf6f2d-da68-4232-b5d0-a861e981291e.png)

![image](https://user-images.githubusercontent.com/61931377/232291702-f1df7de4-d07c-4cff-8f9b-662e2ca10bcf.png)

  
2. Test 2
Customer ingin menghapus item `Pasta Gigi` dengan method `delete_item()`.

![image](https://user-images.githubusercontent.com/61931377/232291812-8ac96d74-833e-4274-bca8-0c72c3a96a2e.png)

3. Test 3
Customer ingin menghapus seluruh item dengan method `reset_transaction()`.

![image](https://user-images.githubusercontent.com/61931377/232291914-3018e084-445c-4d54-838e-db754758e34c.png)

![image](https://user-images.githubusercontent.com/61931377/232291962-45e844ab-514e-49e9-a5ea-508c94cfdb2a.png)

4. Test 4
Customer menambahkan item berikut:
  * Nama item: Ayam Goreng, qty: 2, Harga: 20000
  * Nama item: Pasta Gigi, qty: 3, Harga: 15000
  * Nama item: Mainan Mobil, qty: 1, Harga: 200000
  * Nama item: Mi Instan, qty: 5, Harga: 3000
Kemudian menghitung total belanja dengan method `total_price()`

![image](https://user-images.githubusercontent.com/61931377/232292270-b0f4667c-bf0e-4f8f-a83d-6340a36526a9.png)

![image](https://user-images.githubusercontent.com/61931377/232292361-c5dae2ad-10d6-40f9-a858-8baeaaf636e5.png)

