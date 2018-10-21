import re
from datetime import datetime
from xlrd import open_workbook


class ValidationError(Exception):
    pass


class NameValidationError(ValidationError):
    pass


class EmailValidationError(ValidationError):
    pass


class DateValidationError(ValidationError):
    pass


class FileConverter(object):
    def __init__(self, filename, columns, errlogfile, extention):
        self.filename = filename,
        self.columns = columns,
        self.errlogfile = errlogfile,
        self.extention = extention

    @staticmethod
    def name_validation(name):
        for i in name:
            if not bool(re.search('[а-яА-Я]', i)):
                raise NameValidationError

    @staticmethod
    def mail_validation(mail):
        spl_ = mail.split('@')
        if len(spl_) != 2:
            raise EmailValidationError
        spl_dom = len(spl_[1].split('.'))

        if not 2 <= spl_dom <= 3:
            raise EmailValidationError

    @staticmethod
    def date_validation(date):
        try:
            format_str = '%d-%m-%Y'  # The format
            datetime.strptime(date, format_str).date()
        except:
            raise DateValidationError




book = open_workbook(r'D:\python\class_work\book.xlsx')
sheet = book.sheet_by_index(0)

mp ={}
cells = sheet.row_slice(rowx=0,
                        start_colx=0,
                        end_colx=sheet.ncols)
for k,i in enumerate(cells):
    mp.update({i.value:k})


x= [1,2,3,4]
y= ['a','s','b','b']

matrix = []
for i in range(len(x)):
    matrix.append(i)

for i in range(len(x)):
    matrix.append(x[i])

for i in range(len(x)):
    matrix[i] = [matrix[i],y[i]]

for i in range(len(x)):
    matrix[i] = [*matrix[i],y[i]]

for i in range(len(x)):
    matrix[i] = [*matrix[i],y[i]]


print(matrix)
02120
