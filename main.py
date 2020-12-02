import cv2
import os


if __name__ == "__main__":
    # TODO: Have to processing russian sumbols in the path of files
    directory = r'D:/OPISI/opisiF/F112_2'
    # print(directory.encode('utf8').decode('cp1251'))
    list_of_files = os.listdir(directory)
    length_of_list = len(list_of_files)
    if list_of_files[0] == 'Thumbs.db':
        os.remove(directory + '/' + list_of_files[0])
        list_of_files.pop(0)
    elif list_of_files[length_of_list - 1] == 'Thumbs.db':
        os.remove(directory + '/' + list_of_files[length_of_list - 1])
        list_of_files.pop()
    i=0
    for item in list_of_files:
        os.rename(directory + '/' + item, directory + '/' + str(i) + '.jpg')
        i+=1
    for item in list_of_files:
        img_path = directory + '/' + item
        img = cv2.imread(img_path)
        old_width = int(img.shape[1])
        old_height = int(img.shape[0])
        new_width = 1000
        k_resize = new_width / old_width
        new_height = int(old_height * k_resize)
        dim = (new_width, new_height)
        imgResized = cv2.resize(img, dim)
        cv2.imwrite(img_path, imgResized)