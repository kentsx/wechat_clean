from glob import glob
import hashlib
import os
import send2trash
from pathlib import Path
import datetime

## 各一个文件路径，判断它所在文件夹除此文件外是否还有文件，无文件的删除，且从下往上遍历
def del_empty_folder(dir_path):
    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%Y%m%d%H%M%S")
    with open(f'log-folder-{time_string}.log', 'w', encoding='utf-8') as log_f:  # 文件夹删除记录
        for root, dirnames, filenames in os.walk(dir_path, topdown=False):
            if os.listdir(root):
                pass
                # print('有文件', root)
            else:
                # 删除文件夹
                log_f.write('【删除文件夹】')
                log_f.write(root)
                log_f.write('\n')
                os.rmdir(root)



# 遍历所有文件，删除重复文件到回收站
def del_duplicate_file(dir_path, file_type = '*'):

    # 此处用Path转换了一下，否则反斜杠报错
    lookup_path_notype = Path(dir_path) /'**' / '*.'
    lookup_path = str(lookup_path_notype) + file_type

    file_list = glob(lookup_path, recursive=True)
    # return file_list

    # 删除重复文件
        
    md5_list = []
    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%Y%m%d%H%M%S")
    with open(f'log-file-{time_string}.log', 'w', encoding='utf-8') as log_f:  # 文件删除记录

        for file in file_list:
            with open(file, 'rb') as f:
                file_hash = hashlib.md5()
                dir_path, file_name = os.path.split(file)
                while chuck := f.read(8192):  # 处理大型文件，避免内存占用
                    file_hash.update(chuck)
                file_md5 = file_hash.hexdigest()

            if file_md5 not in md5_list:
                md5_list.append(file_md5)
            else:
                send2trash.send2trash(file)
                log_f.write('【删除文件】')
                log_f.write(file)
                log_f.write('\n')
                print('【已删除】', file)


def whole_process(dir_path, file_type = '*'):
    del_duplicate_file(dir_path, file_type=file_type)
    del_empty_folder(dir_path)
