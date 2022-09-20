import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    with open('/'.join([source_dir, file_name]), 'rb+') as fb:
        with open('/'.join([dest_dir, file_name]), 'wb+') as fw:
            while True:
                file_data = fb.read(1024)
                if file_data:
                    fw.write(file_data)
                else:
                    break


if __name__ == '__main__':
    source_dir = r'D:\BaiduNetdiskDownload\视频-2小时玩转python多线程编程'
    dest_dir = r'C:\Users\LiuHong\Desktop\copyTest'

    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在！")
    source_file_list = os.listdir(source_dir)

    for file_name in source_file_list:
        # copy_file(file_name, source_dir, dest_dir)
        sub_process = multiprocessing.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_process.start()
    print("文件已经全部复制！")
