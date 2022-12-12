# class Point:
#     """
#     Класс для представления координат точек на плоскости
#     """
#     x=1
#     y=1
#
#
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
#
#
# p1=Point()
# print(type(p1))
# print(p1.x)
# p1.x=100
# print(p1.x)
# print(Point.x)
# p2=Point()
# p2.x=200
# print(p2.x)
# print(id(p1))
# print(id(p2))
# print(id(Point))
# Point.y=300
# print(id(p1.y))
# print(id(p2.y))
# print(id(Point.y))
#
# class Point:
#     """
#     Класс для представления координат точек на плоскости
#     """
#     x=1
#     y=1
#
# p1=Point()
# print(p1.x,p1.y)
# p1.x=5
# p1.y=10
# print(p1.x,p1.y)
# print(p1.__dict__)
# print(p1.__dir__())
# p1.z=20
# Point.z=50
# print(p1.__dict__)
# print (Point.__dict__)
#
#
# class Point:
#     """
#     Класс для представления координат точек на плоскости
#     """
#     x=1
#     y=1
#
#     def set_coord(self):
#         print("Метод set_coord")
#         print(self.__dict__)
#
#
# p1=Point()
# print(p1.x)
#
# p1.set_coord()
# Point.set_coord(p1)
# p1.x=5
# p1.y=10
# p1.set_coord()
# class Point:
#     """
#      Класс для представления координат точек на плоскости
#      """
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         print("Метод set_coord")
#         print(self.__dict__)
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# p2 = Point()
# p2.set_coord(8, 17)
# print(p2.__dict__)
# print(p2.x)
# Point.set_coord(p2,7,14)
# print(p2.x)

class Humam:
    name='name'
    birthday='day'
    phone='phone'
    country='country'
    city='city'
    adress='ctreet,house'


    def print_info(self):
        print("пЕПерсональные данные".center(40,"*"))
        print(f"Имя {self.name}\nДата рождения {self.birthday}\nНомер телефона{self.phone}\nCтрана{self.country}\nГород{self.city}\nАдресс {self.adress}")


    def input_info(self,first_name,birthday,phone,country,city,adress):
        self.name=first_name
        self.birthday=birthday
        self.phone=phone
        self.country=country
        self.city=city
        self.adress=adress

    def set_name(self,name):
        if isinstance(name,str):
            self.name=name

    def get_name(self):
        return self.name

    def set_birthday(self,birthday):
        self.birthday=birthday

    def get_birthday(self):
        return self.birthday

    def set_phone(self,phone):
        self.phone=phone

    def get_phone(self):
        return self.phone

    def set_country(self,country):
        self.country=country

    def get_country(self):
        return self.country

    def set_city(self,city):
        self.city=city

    def get_city(self):
        return self.city

    def set_adress(self,adress):
        self.adress=adress

    def get_adress(self):
        return self.adress




h1=Humam()
h1.print_info()
h1.input_info("Юля","23.05.1986","45-46-98","Россия","Москва","Чистопрудный бульвар 6 ")
h1.print_info()
h1.set_name("Алевтина")
h1.print_info()
print(h1.get_name())
h1.set_birthday('28:11:1976')
print(h1.get_birthday())



