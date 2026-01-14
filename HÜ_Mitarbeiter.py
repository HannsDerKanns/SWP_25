class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Employee(Person):
    def __init__(self, name, gender, department):
        super().__init__(name, gender)
        self.department = department
        department.add_employee(self)

class DepartmentHead(Employee):
    def __init__(self, name, gender, department):
        super().__init__(name, gender, department)
        department.set_head(self)

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.head = None

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def set_head(self, head):
        if self.head is not None:
            raise ValueError(f"{self.name} hat schon einen Leiter")
        self.head = head

    def num_employees(self):
        return len(self.employees)

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)

    def all_employees(self):
        employees = []
        for dept in self.departments:
            employees.extend(dept.employees)
        return employees

    def num_employees(self):
        return len(self.all_employees())

    def num_heads(self):
        return sum(1 for dept in self.departments if dept.head)

    def num_departments(self):
        return len(self.departments)

    def largest_department(self):
        if not self.departments:
            return None
        return max(self.departments, key=lambda d: d.num_employees())

    def gender_ratio(self):
        all_genders = [e.gender for e in self.all_employees()]
        total = len(all_genders)
        m_count = all_genders.count("M")
        f_count = all_genders.count("F")
        if total == 0:
            return {"M": 0, "F": 0}
        return {"M": round(m_count/total*100,2), "F": round(f_count/total*100,2)}

def main():
    company = Company("GoonGreen")

    dev = Department("Entwicklung")
    hr = Department("Personal")
    sales = Department("Vertrieb")

    company.add_department(dev)
    company.add_department(hr)
    company.add_department(sales)

    DepartmentHead("Honsä", "M", dev)
    Employee("Lukas Fitz", "F", dev)
    Employee("Andreas", "M", dev)

    DepartmentHead("Julian", "M", hr)
    Employee("Johana", "F", hr)

    DepartmentHead("Sepp-Michinger", "M", sales)
    Employee("Gertrude", "F", sales)
    Employee("Heidi", "F", sales)
    Employee("Christian Biermann", "F", sales)

    print("Az mitarbeiter:", company.num_employees())
    print("Az Abteilungsleiter:", company.num_heads())
    print("Az abteilungen:", company.num_departments())
    largest = company.largest_department()
    print("größte Abteilung:", largest.name if largest else "-")
    print("prozent männer / fraunen:", company.gender_ratio())

if __name__ == "__main__":
    main()
