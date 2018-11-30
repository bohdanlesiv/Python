import  csv
import  os

class ExceptionProductExists(Exception):
    pass

class CSV_UTIlS():
    def __init__(self,file_name):
        self.file_name =file_name

    def add_product(self,product_name,amount):
        file_exists = os.path.isfile(self.file_name)
        with open(self.file_name, 'a+',newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= ['product_name','amount'])
            if not file_exists:
                writer.writeheader()
            if  self.__product_exis(product_name):
                raise ExceptionProductExists
            writer.writerows([{'product_name':product_name,'amount': amount}])

    def get_full_list(self):
        with open(self.file_name, 'r') as csvfile:
            result =[]
            reader = csv.DictReader(csvfile)
            data = [r for r in reader]
            for  i in  data:
                product_detail ={}
                result.append({'product_name':i.get('product_name'),'amount':i.get('amount')})
            return result

    def __product_exis(self,product_name):
        x =self.get_full_list()
        return   any(d['product_name'] == product_name for d in x)

    def get_product(self,product_name):
        x = self.get_full_list()
        return  [d for d in x if d['product_name'] == product_name]


