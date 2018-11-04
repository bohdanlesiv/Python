import sys
filename = sys.argv[1]


with open(filename, 'r+') as fl:
    end_position = fl.seek(0, 2) - 1
    start_position = 0
    while True:
        fl.seek(end_position)
        smbl_fr = fl.read(1)

        if ord(smbl_fr) == 10:
            end_position -= 1
            continue
        fl.seek(start_position)
        smbl_s = fl.read(1)

        if ord(smbl_s) == 10:
            start_position += 1
            continue

        fl.seek(end_position)
        fl.write(smbl_s)
        fl.seek(start_position)
        fl.write(smbl_fr)

        start_position += 1
        end_position -= 1

        if end_position - start_position <= 1:
            break
