import glob
import nkf
import os
import shutil

input_dir= './input'
backup_dir= './input_bak'

def get_file_names():
    return glob.glob(input_dir + '/**/*', recursive=True)
    #file_dir_paths = os.listdir(input_dir)
    #return [f for f in file_dir_paths if os.path.isfile(os.path.join(input_dir, f))]

def make_backup():
    shutil.copytree(input_dir, backup_dir)

def make_output_dir():
    if os.path.isdir(backup_dir):
        return
    os.mkdir(backup_dir)
    os.chmod(backup_dir, 0o777)

# 上書き
def write_to_utf8(path):
    f = open(path, 'r')
    str = f.read()
    f.close()

    str_utf8 = nkf.nkf('w', str)
    fout = open(path, 'w')
    fout.write(str_utf8)
    fout.close()

if __name__ == '__main__':
    make_backup()
    #make_output_dir()
    file_names = get_file_names()
    print(file_names)
    for file_name in file_names:
        write_to_utf8(file_name)
