class Customer:
    def __init__(self, name):
        self.name = name
        self.purchases = {}  # Lưu trữ sản phẩm và số lượng mua

    def add_purchase(self, product, quantity):
        if product in self.purchases:
            self.purchases[product] += quantity
        else:
            self.purchases[product] = quantity

    def display_info(self):
        print(f"Khách hàng: {self.name}")
        print("Các sản phẩm đã mua:")
        for product, quantity in self.purchases.items():
            print(f" - {product}: {quantity} cái")


class Store:
    def __init__(self):
        self.customers = {}

    def add_customer(self, name):
        if name in self.customers:
            print(f"Khách hàng {name} đã tồn tại.")
        else:
            self.customers[name] = Customer(name)
            print(f"Thêm khách hàng {name} thành công.")

    def add_purchase(self, name, product, quantity):
        if name not in self.customers:
            print(f"Không tìm thấy khách hàng {name}.")
        else:
            self.customers[name].add_purchase(product, quantity)
            print(f"Thêm {quantity} cái {product} cho khách hàng {name} thành công.")

    def display_customer_info(self, name):
        if name not in self.customers:
            print(f"Không tìm thấy khách hàng {name}.")
        else:
            self.customers[name].display_info()

    def display_all_customers(self):
        if not self.customers:
            print("Chưa có khách hàng nào.")
        else:
            print("Danh sách khách hàng:")
            for customer in self.customers.values():
                customer.display_info()


# Menu tương tác
store = Store()

def menu():
    while True:
        print("\n--- Quản lý khách hàng ---")
        print("1. Thêm khách hàng")
        print("2. Thêm sản phẩm mua hàng")
        print("3. Hiển thị thông tin khách hàng")
        print("4. Hiển thị tất cả khách hàng")
        print("5. Thoát")
        
        choice = input("Chọn chức năng: ")

        if choice == '1':
            name = input("Nhập tên khách hàng: ")
            store.add_customer(name)
        elif choice == '2':
            name = input("Nhập tên khách hàng: ")
            product = input("Nhập tên sản phẩm: ")
            quantity = int(input("Nhập số lượng: "))
            store.add_purchase(name, product, quantity)
        elif choice == '3':
            name = input("Nhập tên khách hàng: ")
            store.display_customer_info(name)
        elif choice == '4':
            store.display_all_customers()
        elif choice == '5':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

# Khởi động menu
menu()
