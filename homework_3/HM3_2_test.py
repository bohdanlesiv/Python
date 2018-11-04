from HM3_2 import FileConverter

flc = FileConverter(r'D:\python\class_work\book.xlsx')
x = flc.columns_processing({'UserName': 'name_validation', 'Email': 'mail_validation', 'joined': 'date_validation'})
flc.validation()
flc.save_err_log()
flc.save_to_json()
flc.save_to_csv()
flc.save_to_bin()
flc.save_to_shelve()