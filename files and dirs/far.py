import os

def show_dir_options():
    dir_options = ["List content", "Go to", "Rename", "Create file", "Create directory", "Go back"]
    for i in range (6):
        print(str(i + 1) + ". " + dir_options[i])

def show_file_options():
    file_options = ["Print content", "Rename", "Add content", "Rewrite content", "Delete", "Go back"]
    for i in range (6):
        print(str(i + 1) + ". " + file_options[i])

def sorted_list(path):
    lst = os.listdir(path)
    list_of_dirs = []
    list_of_files = []
    for i in lst:
        if os.path.isdir(os.path.join(path, i)):
            list_of_dirs.append(i)
        else:
            list_of_files.append(i)
    return list_of_dirs + list_of_files

def list_files_and_dirs(path):
    lst = sorted_list(path)
    cnt = 1
    for i in lst:
        print(str(cnt) + ". " + (i.upper() if os.path.isdir(os.path.join(path, i)) else i.lower()))
        cnt += 1

def go_to(path):
    list_files_and_dirs(path)
    lst = sorted_list(path)
    option = int(input())
    name = lst[option - 1]
    path = os.path.join(path, name)
    return path

def create_file(path):
    name = input()
    filename = name + ".txt"
    path = os.path.join(path, filename)
    file = open(path, "w")
    file.close()

def create_directory(path):
    name = input()
    path = os.path.join(path, name)
    os.mkdir(path)

def read_file(path):
    file = open(path, "r")
    print(file.read())
    file.close()

def rename_file(path):
    new_name = input()
    new_name = new_name + ".txt"
    old_path = path
    new_path = os.path.join(path, new_name)
    os.rename(old_path, new_path)
    return new_path

def append_to_file(path):
    add_content = input()
    file = open(path, "a")
    file.write(add_content)
    file.close()

def rewrite_file(path):
    new_content = input()
    file = open(path, "w")
    file.write(new_content)
    file.close()

def delete_file(path):
    os.remove(path)


def main():
    cur_path = "C://"
    while(True):
        if (os.path.isdir(cur_path)):
            show_dir_options()
            option = int(input())
            if (option == 1):
                list_files_and_dirs(cur_path)
            if (option == 2):
                cur_path = go_to(cur_path)
            if (option == 3):
                new_name = input()
                os.rename(os.path.dirname(cur_path), new_name)
            if (option == 4):
                create_file(cur_path)
            if (option == 5):
                create_directory(cur_path)
            if (option == 6):
                cur_path = (cur_path if cur_path == "C://" else os.path.dirname(cur_path))
        else:
            show_file_options()
            option = int(input())
            if (option == 1):
                read_file(cur_path)
            if (option == 2):
                cur_path = rename_file(cur_path)
            if (option == 3):
                append_to_file(cur_path)
            if (option == 4):
                rewrite_file(cur_path)
            if (option == 5):
                path_to_delete = cur_path
                cur_path = os.path.dirname(cur_path)
                delete_file(path_to_delete)
            if (option == 6):
                cur_path = os.path.dirname(cur_path)



if __name__ == "__main__":
    main()