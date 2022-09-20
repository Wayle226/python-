import threading
import os


def copy_file(file_name, source_dir, destination_dir):
    if file_name:
        with open('/'.join([source_dir, file_name]), 'rb') as fb:
            with open('/'.join([destination_dir, file_name]), 'wb') as fw:
                while True:
                    source_data = fb.read(1024)
                    if source_data:
                        fw.write(source_data)
                    else:
                        break




if __name__ == '__main__':
    source_dir = r'D:\BaiduNetdiskDownload\视频-2小时玩转python多线程编程'
    destination_dir = r'C:\Users\LiuHong\Desktop\copy_thread'
    source_file_name = os.listdir(source_dir)
    try:
        os.mkdir(destination_dir)
    except Exception as e:
        print("目标文件夹已经存在！")

    for file_name in source_file_name:
        sub_thread = threading.Thread(target=copy_file, args=(file_name, source_dir, destination_dir))
        sub_thread.start()