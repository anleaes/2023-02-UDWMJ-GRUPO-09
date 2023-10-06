class Product:
     def __init__(self,name,description,date_fabrication,is_active):
          self.name = name
          self.description = description
          self.date_fabrication = date_fabrication
          self.is_active = is_active

     def check_availability(self):
          if self.is_active == True:
               print("Tem o produto")
          else: 
               print("Não tem o produto")