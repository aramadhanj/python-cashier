class Cashier:
    """
    Kelas Cashier digunakan untuk melakukan transaksi pembelian pada cashier
    self-service.

    Fitur yang tersedia:
    1. add_item : menambahkan item baru ke dalam daftar order
    2. update_item_qty : mengubah jumlah item
    3. update_item_name : mengubah nama item
    4. update_item_price : mengubah harga item
    5. reset_transaction : menghapus seluruh daftar order
    6. check_order : menampilkan daftar order
    7. total_price : menghitung total harga yang terdapat dalam daftar order dengan menghitung diskon.

    """
    def __init__(self):
        self.order_list = {} #Inisiasi sebuah list kosong sebagai list untuk menambahkan item
    
    def add_item(self, name, qty, price):
        if name in self.order_list:
            self.order_list[name][0] += qty #apabila nama item terdapat didalam order_list maka jumlah item bertambah
        else:
            self.order_list[name] = [qty, price] #apabila nama item belum terdapat, maka ditambahkan qty dan harga ke dalam list order_list

    def update_item_qty(self, name, new_qty):
        if name in self.order_list:
            self.order_list[name][0] = new_qty #mengubah kuantitas item ketika nama item terdapat dalam list order_list

    def update_item_name(self, old_name, new_name):
        if old_name in self.order_list:
            self.order_list[new_name] = self.order_list.pop(old_name) #mengubah nama item terbaru ketika nama item lama terdapat dalam list order_list dan menghapusnya

    def update_item_price(self, name, new_price):
        if name in self.order_list:
            self.order_list[name][1] = new_price #mengubah harga item ketika nama item terdapat dalam list order_list

    def delete_item(self, name):
        if name in self.order_list:
            self.order_list.pop(name) #menghapus item berdasarkan nama item

    def reset_transaction(self):
        self.order_list.clear() #menghapus daftar order dengan cara menghapus isi list order_list

    def check_order(self):
        print("Item yang dibeli adalah:")
        print("+----+----------------------+--------------+------------+--------------+")
        print("| No |      Nama Item       | Jumlah Item  | Harga/Item | Total Harga  |")
        print("+----+----------------------+--------------+------------+--------------+")
        total_price = 0
        for index, (name, item_info) in enumerate(self.order_list.items(), start=1):
            qty, price = item_info
            total = qty * price
            print("|{:<4}|{:<22}|{:^14}|{:>12,.0f}|{:>14,.0f}|".format(index, name, qty, price, total))
            total_price += total
        print("+----+----------------------+--------------+------------+--------------+")
        return total_price

    def total_price(self, total_harga):
        if total_harga > 500000:
            diskon = 0.1
        elif total_harga > 300000:
            diskon = 0.08
        elif total_harga > 200000:
            diskon = 0.05
        else:
            diskon = 0
        diskon_amount = total_harga * diskon
        total_harga_setelah_diskon = total_harga - diskon_amount #total harga dikurangi diskon
        return total_harga_setelah_diskon #total harga akhir
