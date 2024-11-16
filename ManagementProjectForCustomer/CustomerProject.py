class Store:
    def __init__(self):
        # Danh sách sản phẩm với tên và giá
        self.products = {
            "Laptop": 15000000,
            "Điện thoại": 8000000,
            "Tai nghe": 500000,
            "Bàn phím": 300000,
            "Chuột": 200000
        }
        self.cart = {}

    def search_product(self, product_name):
        # Tìm kiếm sản phẩm trong danh sách
        if product_name in self.products:
            print(f"Sản phẩm: {product_name}, Giá: {self.products[product_name]} VND")
        else:
            print("Sản phẩm không tồn tại trong cửa hàng.")

    def add_to_cart(self, product_name, quantity):
        # Thêm sản phẩm vào giỏ hàng
        if product_name in self.products:
            if product_name in self.cart:
                self.cart[product_name] += quantity
            else:
                self.cart[product_name] = quantity
            print(f"Đã thêm {quantity} {product_name} vào giỏ hàng.")
        else:
            print("Sản phẩm không tồn tại trong cửa hàng.")

    def view_cart(self):
        # Hiển thị giỏ hàng và tổng tiền
        if not self.cart:
            print("Giỏ hàng của bạn trống.")
            return
        total = 0
        print("Giỏ hàng của bạn:")
        for product, quantity in self.cart.items():
            price = self.products[product] * quantity
            total += price
            print(f"{product} - Số lượng: {quantity}, Giá: {price} VND")
        print(f"Tổng tiền: {total} VND")

    def checkout(self):
        # Thanh toán qua ATM
        if not self.cart:
            print("Giỏ hàng của bạn trống. Vui lòng thêm sản phẩm trước khi thanh toán.")
            return
        self.view_cart()
        print("Vui lòng thanh toán qua ATM.")
        atm_number = input("Nhập số thẻ ATM của bạn: ")
        print(f"Đang xử lý thanh toán từ số thẻ {atm_number}... Thanh toán thành công!")
        self.cart.clear()


# Chạy chương trình
store = Store()

while True:
    print("\nChọn một hành động:")
    print("1. Tìm kiếm sản phẩm")
    print("2. Thêm sản phẩm vào giỏ hàng")
    print("3. Xem giỏ hàng")
    print("4. Thanh toán")
    print("5. Thoát")
    choice = input("Nhập số tương ứng với hành động bạn muốn thực hiện: ")

    if choice == "1":
        product_name = input("Nhập tên sản phẩm bạn muốn tìm: ")
        store.search_product(product_name)
    elif choice == "2":
        product_name = input("Nhập tên sản phẩm bạn muốn thêm vào giỏ hàng: ")
        quantity = int(input("Nhập số lượng: "))
        store.add_to_cart(product_name, quantity)
    elif choice == "3":
        store.view_cart()
    elif choice == "4":
        store.checkout()
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
