import csv
import json
import os
import pickle
import re
from datetime import datetime
import shelve
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

    def __init__(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError
        self.book = open_workbook(filename)

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
            format_str = '%Y-%m-%d'
            datetime.strptime(date, format_str).date()
        except:
            raise DateValidationError

    def columns_processing(self, columns):
        self.list_xls = []
        self.columns = columns
        sheet = self.book.sheet_by_index(0)
        data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
        for row in range(1, sheet.nrows):
            dict_xls = {}
            for col in columns:
                idx = data.index(col)
                dict_xls.update({col: sheet.cell_value(row, idx)})
            self.list_xls.append(dict_xls)

    def validation(self):
        registry = {'FileConverter': FileConverter}
        self.val_list = []
        for idx, row in enumerate(self.list_xls):
            for col in self.columns:
                line = row.get(col)
                val_fn = self.columns.get(col)
                try:
                    getattr(registry['FileConverter'], val_fn)(str(line))
                except ValidationError:
                    # print(row)
                    # print(val_fn)
                    self.val_list.append({'row': row, 'rule': val_fn, 'index': idx})
                    # val_dict.update({'row': row, 'rule': val_fn, 'index': idx})
                    # try:
                    #     self.list_xls.remove(row)
                    # except ValueError:
                    #     pass
                except Exception as e:
                    pass

        for vrow in self.val_list:
            try:
                self.list_xls.remove(vrow.get('row'))
            except Exception:
                pass

    def save_err_log(self, errfilenm='errors.log'):
        with open(os.path.join(os.curdir, errfilenm), 'w') as flog:
            for row in self.val_list:
                flog.write(str(row) + '\n')

    def save_to_json(self, flnm='output.json'):
        with open(os.path.join(os.curdir, flnm), 'w') as fjson:
            json.dump(self.list_xls, fjson, ensure_ascii=False)

    def save_to_csv(self, flnm='output.csv'):
        with open(os.path.join(os.curdir, flnm), 'w') as fcsv:
            w = csv.DictWriter(fcsv, self.columns.keys())
            w.writeheader()
            for rows in self.list_xls:
                w.writerow(rows)

    def save_to_bin(self, flnm='output.bin'):
        with open(os.path.join(os.curdir, flnm), 'wb') as fbin:
            pickle.dump(self.list_xls, fbin)

    def save_to_shelve(self, flnm='output.shlv'):
        sh = shelve.open(os.path.join(os.curdir, flnm))
        sh['data_xls'] = self.list_xls
        sh.close()




#
#
# dict2 = {}
# book = open_workbook(r'D:\python\class_work\book.xlsx')
# sheet = book.sheet_by_index(0)
#
# print(sheet.ncols)
# print(sheet.name)
# print(sheet.col_slice(0))
#
# data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
# print(data)
#
#
# for index, value in enumerate(data):
#     print('Index {} Value {}'.format(index,value))
#
#
#
#
# for i in range(1,sheet.nrows):
#      x.append(sheet.cell_value(i,1))
#
#
# with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
#      w = csv.writer(f)
#      w.writerow(dict2.keys())
#      w.writerow(dict2.values())
