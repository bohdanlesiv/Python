import os
import fnmatch
import shutil
import time
from functools import reduce


class CalculationError(Exception):
    pass


class PathError(Exception):
    def __init__(self, message):
        self.message = message + ' is wrong defined'


def monitor(read_path, write_path, error_path):

    def log_execution_time(func):
        def wrapper():
            start_time = time.time()
            func()
            print('Function name: ' + func.__name__.upper())
            print('Execution time:' + str(time.time()-start_time)+' seconds')
        return wrapper

    def get_files_for_processing():
        """Get list of available txt files by read path """
        all_files = os.listdir(read_path)
        txt_files = list(filter(lambda filename: fnmatch.fnmatch(filename, '*.txt'), all_files))
        return txt_files

    def get_amount_by_file(path):
        """Returns total of numbers inside txt file, raise error in case if file is empty """
        if os.stat(path).st_size == 0:
            raise Exception
        with open(path, 'r') as file:
            items = file.read().split(',')
            total = reduce(lambda x, y: int(x) + int(y), items)
            return total

    def create_procesed_file(msg, filename, path):
        """Creates file in result directory with total amount """
        write_path_txt = os.path.join(path, filename)
        with open(write_path_txt, 'w') as file:
            file.write(str(msg))

    def path_validation():
        isdir = os.path.isdir
        if not isdir(read_path):
            raise PathError('Read path')
        if not isdir(error_path):
            raise PathError('Err path')
        if not isdir(write_path):
            raise PathError('Write path')

    @log_execution_time
    def process():
        for txt_file in get_files_for_processing():
            read_path_txt = os.path.join(read_path, txt_file)
            try:
                try:
                    amount = get_amount_by_file(read_path_txt)
                except Exception:
                    raise CalculationError
                create_procesed_file(amount, txt_file, write_path)
            except CalculationError:
                shutil.copy(read_path_txt, error_path)
            finally:
                os.remove(read_path_txt)

    path_validation()
    process()
