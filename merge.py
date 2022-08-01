import pdb
import os


def read_text(text_path):
    with open(text_path,"rb") as f:
        lines = f.readlines()
    return lines

def write_text(lines, text_path):
    with open(text_path,"ab") as f:
        for line in lines:
            f.write(line.encode())

def filter_lines(lines,part_idx):
    line_num = len(lines)
    for idx in range(line_num):
        lines[idx] = lines[idx].decode()

    idx = lines[0].find("集")

    # 修改开头的标题
    lines[0] = lines[0][idx+2:]
    lines[0] = "第{}章:  ".format(part_idx) + lines[0]

    # 删除最后的注释
    empty_lines = []
    for idx in range(line_num):
        if lines[idx].find("注释") != -1:
            continue
        empty_lines.append(lines[idx])
    
    return empty_lines



def merge_dir(file_lists,merge_path):
    part_idx = 1
    for file_path in file_lists:
        lines = read_text(file_path)
        lines = filter_lines(lines,part_idx)
        part_idx += 1
        write_text(lines,merge_path)

def get_all_files(dir_path):
    file_lists = os.listdir(dir_path)

    files_paths = []
    for file in file_lists:
        files_paths.append(os.path.join(dir_path,file))
    return files_paths


if __name__ == "__main__":
    merge_path = "老友记.txt"
    for season in range(1,11):
        dir_path = "S{:02d}".format(season)
        files = get_all_files(dir_path)
        merge_dir(files,merge_path)