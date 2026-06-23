class TutoringClass:
    def __init__(self, id, class_name, teacher_name, tuition_fee, student_count, operating_cost):
        self.id = id
        self.class_name = class_name
        self.teacher_name = teacher_name
        self.tuition_fee = tuition_fee
        self.student_count = student_count
        self.operating_cost = operating_cost
        self.total_revenue = 0
        self.revenue_type = ""
        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        self.total_revenue = (self.tuition_fee * self.student_count) - self.operating_cost

    def classify_revenue(self):
        if self.total_revenue < 0:
            self.revenue_type = "Lỗ"
        elif self.total_revenue < 10000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 30000000:
            self.revenue_type = "Ổn định"
        else:
            self.revenue_type = "Tốt"

    def __str__(self):
        return f"{self.id:<10} {self.class_name:<15} {self.teacher_name:<15} {self.tuition_fee:<12} {self.student_count:<10} {self.operating_cost:<15} {self.total_revenue:<15} {self.revenue_type}"

class TutoringClassManager:
    def __init__(self):
        self.classes = []

    def add_class(self):
        print("\n--- Thêm lớp học mới ---")
        id = input("Nhập mã lớp học: ").strip()
        if not id:
            print("Mã lớp học không được rỗng!")
            return
        
        if any(c.id == id for c in self.classes):
            print("Mã lớp học bị trùng!")
            return

        class_name = input("Nhập tên lớp học: ").strip()
        if not class_name:
            print("Tên lớp học không được rỗng!")
            return

        teacher_name = input("Nhập tên giáo viên: ").strip()
        if not teacher_name:
            print("Tên giáo viên không được rỗng!")
            return

        try:
            tuition_fee = float(input("Nhập học phí mỗi học viên: "))
            if tuition_fee < 0: 
                raise ValueError
            student_count = int(input("Nhập số lượng học viên (0-100): "))
            if not (0 <= student_count <= 100): 
                raise ValueError
            operating_cost = float(input("Nhập chi phí vận hành: "))
            if operating_cost < 0: 
                raise ValueError
        except ValueError:
            print("Dữ liệu nhập vào không hợp lệ!")
            return

        new_class = TutoringClass(id, class_name, teacher_name, tuition_fee, student_count, operating_cost)
        self.classes.append(new_class)
        print("Thêm lớp học thành công!")

    def show_all(self):
        if not self.classes:
            print("Danh sách lớp học đang rỗng!")
            return
        
        header = f"{'Mã lớp':<10} {'Tên lớp':<15} {'Giáo viên':<15} {'Học phí':<12} {'Số HV':<10} {'Chi phí':<15} {'Doanh thu':<15} {'Phân loại'}"
        print("-" * len(header))
        for c in self.classes:
            print(c)

    def update_class(self):
        id = input("Nhập mã lớp học cần cập nhật: ")
        found_class = next((c for c in self.classes if c.id == id), None)
        
        if not found_class:
            print("Không tìm thấy lớp học cần cập nhật!")
            return

        try:
            found_class.tuition_fee = float(input(f"Học phí cũ ({found_class.tuition_fee}), nhập mới: "))
            found_class.student_count = int(input(f"Số lượng cũ ({found_class.student_count}), nhập mới: "))
            found_class.operating_cost = float(input(f"Chi phí cũ ({found_class.operating_cost}), nhập mới: "))
            
            found_class.calculate_revenue()
            found_class.classify_revenue()
            print("Cập nhật lớp học thành công!")
        except ValueError:
            print("Dữ liệu nhập vào không hợp lệ!")

    def delete_class(self):
        id = input("Nhập mã lớp học cần xóa: ")
        found_class = next((c for c in self.classes if c.id == id), None)
        
        if not found_class:
            print("Không tìm thấy lớp học cần xóa!")
            return
            
        confirm = input(f"Bạn có chắc muốn xóa lớp {id} không? (Y/N): ").lower()
        if confirm == 'y':
            self.classes.remove(found_class)
            print("Xóa thành công!")
        elif confirm == 'n':
            print("Hủy thao tác.")
        else:
            print("Lựa chọn không hợp lệ!")

    def search_class(self):
        keyword = input("Nhập từ khóa tìm kiếm (Tên lớp hoặc Tên giáo viên): ").lower()
        results = [c for c in self.classes if keyword in c.class_name.lower() or keyword in c.teacher_name.lower()]
        
        if not results:
            print("Không tìm thấy lớp học phù hợp!")
        else:
            for c in results:
                print(c)

def main():
    manager = TutoringClassManager()
    while True:
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách lớp học")
        print("2. Thêm lớp học mới")
        print("3. Cập nhật lớp học")
        print("4. Xóa lớp học")
        print("5. Tìm kiếm lớp học")
        print("6. Thoát")
        print("======================================")
        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case '1':
                manager.show_all()
            case '2':
                manager.add_class()
            case '3':
                manager.update_class()
            case '4':
                manager.delete_class()
            case '5':
                manager.search_class()
            case '6':
                print('Cảm ơn bạn đã sử dụng hệ thống quản lý lớp học thêm!')
                break
            case _:
                print('Lựa chọn không hợp lệ')

if __name__ == "__main__":
    main()