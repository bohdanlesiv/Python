import uuid
import os
import shutil

import sys
filename = sys.argv[1]
read_bulk = 2
file_for_process = filename

class InternalProcessException(Exception):
    pass

class FileNotExistsException(Exception):
    pass

def get_tmp_file_nm(file_for_process):
    unique_filename = str(uuid.uuid4())
    path = os.path.split(file_for_process)[0]
    fl_nm = os.path.join(path, unique_filename+'.txt')
    return fl_nm


def reverse_str(read_str):
    return ''.join(reversed(read_str))


with open(file_for_process, 'r+') as f:
    Nextchars = True

    if not os.path.exists(file_for_process):
        raise FileNotExistsException

    fl_tmp = get_tmp_file_nm(file_for_process)
    file_len = len(f.read())
    print(fl_tmp)
    try:
        while Nextchars:
            file_len = file_len - read_bulk
            if file_len <= 0:
                if file_len % read_bulk != 0:
                    read_bulk = read_bulk - 1
                file_len = 0
                Nextchars = False
            f.seek(file_len)
            read_s = f.read(read_bulk)
            rev_str = reverse_str(read_s)

            with open(fl_tmp, 'a') as tmp_f:
                tmp_f.write(rev_str)
    except:
        if os.path.exists(fl_tmp):
            os.remove(fl_tmp)

        raise InternalProcessException

    shutil.move(fl_tmp,file_for_process)
