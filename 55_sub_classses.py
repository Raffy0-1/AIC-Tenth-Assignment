# 55 sub classes for real eh!

# Parent1 with 1 level of inheritance
class Parent1:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent1: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass1_1(Parent1):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass1_1: {self.subclass_info}"

# Parent2 with 2 subclasses for each group
class Parent2A:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent2A: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass2_1A(Parent2A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass2_1A: {self.subclass_info}"

class Subclass2_2A(Parent2A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass2_2A: {self.subclass_info}"

class Parent2B:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent2B: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass2_1B(Parent2B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass2_1B: {self.subclass_info}"

class Subclass2_2B(Parent2B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass2_2B: {self.subclass_info}"

# Parent3 with 3 subclasses for each group
class Parent3A:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent3A: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass3_1A(Parent3A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_1A: {self.subclass_info}"

class Subclass3_2A(Parent3A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_2A: {self.subclass_info}"

class Subclass3_3A(Parent3A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_3A: {self.subclass_info}"

class Parent3B:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent3B: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass3_1B(Parent3B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_1B: {self.subclass_info}"

class Subclass3_2B(Parent3B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_2B: {self.subclass_info}"

class Subclass3_3B(Parent3B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_3B: {self.subclass_info}"

class Parent3C:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent3C: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass3_1C(Parent3C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_1C: {self.subclass_info}"

class Subclass3_2C(Parent3C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_2C: {self.subclass_info}"

class Subclass3_3C(Parent3C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass3_3C: {self.subclass_info}"

# Parent4 with 4 subclasses for each group
class Parent4A:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent4A: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass4_1A(Parent4A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_1A: {self.subclass_info}"

class Subclass4_2A(Parent4A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_2A: {self.subclass_info}"

class Subclass4_3A(Parent4A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_3A: {self.subclass_info}"

class Subclass4_4A(Parent4A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_4A: {self.subclass_info}"

class Parent4B:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent4B: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass4_1B(Parent4B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_1B: {self.subclass_info}"

class Subclass4_2B(Parent4B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_2B: {self.subclass_info}"

class Subclass4_3B(Parent4B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_3B: {self.subclass_info}"

class Subclass4_4B(Parent4B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_4B: {self.subclass_info}"

class Parent4C:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent4C: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass4_1C(Parent4C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_1C: {self.subclass_info}"

class Subclass4_2C(Parent4C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_2C: {self.subclass_info}"

class Subclass4_3C(Parent4C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_3C: {self.subclass_info}"

class Subclass4_4C(Parent4C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_4C: {self.subclass_info}"

class Parent4D:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent4D: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass4_1D(Parent4D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_1D: {self.subclass_info}"

class Subclass4_2D(Parent4D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_2D: {self.subclass_info}"

class Subclass4_3D(Parent4D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_3D: {self.subclass_info}"

class Subclass4_4D(Parent4D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass4_4D: {self.subclass_info}"

# Parent5 with 5 subclasses for each group
class Parent5A:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent5A: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass5_1A(Parent5A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_1A: {self.subclass_info}"

class Subclass5_2A(Parent5A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_2A: {self.subclass_info}"

class Subclass5_3A(Parent5A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_3A: {self.subclass_info}"

class Subclass5_4A(Parent5A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_4A: {self.subclass_info}"

class Subclass5_5A(Parent5A):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_5A: {self.subclass_info}"



# Parent5B with 5 subclasses for each group
class Parent5B:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent5B: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass5_1B(Parent5B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_1B: {self.subclass_info}"

class Subclass5_2B(Parent5B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_2B: {self.subclass_info}"

class Subclass5_3B(Parent5B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_3B: {self.subclass_info}"

class Subclass5_4B(Parent5B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_4B: {self.subclass_info}"

class Subclass5_5B(Parent5B):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_5B: {self.subclass_info}"

# Parent5C with 5 subclasses for each group
class Parent5C:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent5C: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass5_1C(Parent5C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_1C: {self.subclass_info}"

class Subclass5_2C(Parent5C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_2C: {self.subclass_info}"

class Subclass5_3C(Parent5C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_3C: {self.subclass_info}"

class Subclass5_4C(Parent5C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_4C: {self.subclass_info}"

class Subclass5_5C(Parent5C):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_5C: {self.subclass_info}"

# Parent5D with 5 subclasses for each group
class Parent5D:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent5D: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass5_1D(Parent5D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_1D: {self.subclass_info}"

class Subclass5_2D(Parent5D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_2D: {self.subclass_info}"

class Subclass5_3D(Parent5D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_3D: {self.subclass_info}"

class Subclass5_4D(Parent5D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_4D: {self.subclass_info}"

class Subclass5_5D(Parent5D):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_5D: {self.subclass_info}"

# Parent5E with 5 subclasses for each group
class Parent5E:
    def __init__(self, name):
        self.name = name
        
    def get_info(self):
        return f"Parent5E: {self.name}"

    def set_info(self, name):
        self.name = name

class Subclass5_1E(Parent5E):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_1E: {self.subclass_info}"

class Subclass5_2E(Parent5E):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_2E: {self.subclass_info}"

class Subclass5_3E(Parent5E):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_3E: {self.subclass_info}"

class Subclass5_4E(Parent5E):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_4E: {self.subclass_info}"

class Subclass5_5E(Parent5E):
    def __init__(self, name, subclass_info):
        super().__init__(name)
        self.subclass_info = subclass_info
        
    def get_subclass_info(self):
        return f"Subclass5_5E: {self.subclass_info}"
    



# Create objects for Parent1 and its subclass Subclass1_1
parent1_obj = Parent1("RAffy1")
subclass1_1_obj = Subclass1_1("Raffy", "Subclass Info 1")

# Create objects for Parent2A, Subclass2_1A, and Subclass2_2A
parent2A_obj = Parent2A("Raffy2")
subclass2_1A_obj = Subclass2_1A("Raffy", "Subclass Info 2A1")
subclass2_2A_obj = Subclass2_2A("Raffy", "Subclass Info 2A2")

# Create objects for Parent2B, Subclass2_1B, and Subclass2_2B
parent2B_obj = Parent2B("Raffy2 ")
subclass2_1B_obj = Subclass2_1B("Raffy", "Subclass Info 2B1")
subclass2_2B_obj = Subclass2_2B("Raffy", "Subclass Info 2B2")

# Create objects for Parent3A, Subclass3_1A, Subclass3_2A, and Subclass3_3A
parent3A_obj = Parent3A("Raffy2")
subclass3_1A_obj = Subclass3_1A("Raffy", "Subclass Info 3A1")
subclass3_2A_obj = Subclass3_2A("Raffy", "Subclass Info 3A2")
subclass3_3A_obj = Subclass3_3A("Raffy", "Subclass Info 3A3")

# Create objects for Parent3B, Subclass3_1B, Subclass3_2B, and Subclass3_3B
parent3B_obj = Parent3B("Raffy 2 ")
subclass3_1B_obj = Subclass3_1B("Raffy", "Subclass Info 3B1")
subclass3_2B_obj = Subclass3_2B("Raffy", "Subclass Info 3B2")
subclass3_3B_obj = Subclass3_3B("Raffy", "Subclass Info 3B3")

# Create objects for Parent3C, Subclass3_1C, Subclass3_2C, and Subclass3_3C
parent3C_obj = Parent3C("Raffy")
subclass3_1C_obj = Subclass3_1C("Raffy", "Subclass Info 3C1")
subclass3_2C_obj = Subclass3_2C("Raffy", "Subclass Info 3C2")
subclass3_3C_obj = Subclass3_3C("RAffy", "Subclass Info 3C3")

# Create objects for Parent4A, Subclass4_1A, Subclass4_2A, Subclass4_3A, and Subclass4_4A
parent4A_obj = Parent4A("RAffy")
subclass4_1A_obj = Subclass4_1A("RAffy", "Subclass Info 4A1")
subclass4_2A_obj = Subclass4_2A("RAffy", "Subclass Info 4A2")
subclass4_3A_obj = Subclass4_3A("RAffy", "Subclass Info 4A3")
subclass4_4A_obj = Subclass4_4A("RAffy", "Subclass Info 4A4")

# Create objects for Parent4B, Subclass4_1B, Subclass4_2B, Subclass4_3B, and Subclass4_4B
parent4B_obj = Parent4B("RAffy")
subclass4_1B_obj = Subclass4_1B("RAffy", "Subclass Info 4B1")
subclass4_2B_obj = Subclass4_2B("RAffy", "Subclass Info 4B2")
subclass4_3B_obj = Subclass4_3B("RAffy", "Subclass Info 4B3")
subclass4_4B_obj = Subclass4_4B("RAffy", "Subclass Info 4B4")

# Create objects for Parent4C, Subclass4_1C, Subclass4_2C, Subclass4_3C, and Subclass4_4C
parent4C_obj = Parent4C("RAffy")
subclass4_1C_obj = Subclass4_1C("RAffy", "Subclass Info 4C1")
subclass4_2C_obj = Subclass4_2C("RAffy", "Subclass Info 4C2")
subclass4_3C_obj = Subclass4_3C("RAffy", "Subclass Info 4C3")
subclass4_4C_obj = Subclass4_4C("RAffy", "Subclass Info 4C4")

# Create objects for Parent4D, Subclass4_1D, Subclass4_2D, Subclass4_3D, and Subclass4_4D
parent4D_obj = Parent4D("RAffy")
subclass4_1D_obj = Subclass4_1D("RAffy", "Subclass Info 4D1")
subclass4_2D_obj = Subclass4_2D("RAffy", "Subclass Info 4D2")
subclass4_3D_obj = Subclass4_3D("RAffy", "Subclass Info 4D3")
subclass4_4D_obj = Subclass4_4D("RAffy", "Subclass Info 4D4")

# Create objects for Parent5A, Subclass5_1A, Subclass5_2A, Subclass5_3A, and Subclass5_4A
parent5A_obj = Parent5A("RAffy")
subclass5_1A_obj = Subclass5_1A("RAffy", "Subclass Info 5A1")
subclass5_2A_obj = Subclass5_2A("RAffy", "Subclass Info 5A2")
subclass5_3A_obj = Subclass5_3A("RAffy", "Subclass Info 5A3")
subclass5_4A_obj = Subclass5_4A("RAffy", "Subclass Info 5A4")


