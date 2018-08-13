import cv2
import os
import os.path as os_path
from os import listdir


# get file from directory
def get_images_list(path):
    images_list = []
    # check input path exist or not
    bool_path = True

    while bool_path:
        if not os_path.exists(path):
            path = input("path doesn't exist, please check it and re-enter: ")
        else:
            bool_path = False

    # check file type
    files_list = [f for f in listdir(path) if os_path.isfile(os_path.join(path, f))]

    if files_list is None:
        return None
    else:
        for file in files_list:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                images_list.append(file)

    return images_list


def mouse_position(event, x, y, flags, param):
    global position

    # write into txt file
    txt_file_path = './coordinate/'
    image_split = image.split('.')
    file_name = txt_file_path + image_split[0] + '.txt'

    # check file exist
    if not os.path.exists(txt_file_path):
        os.makedirs(txt_file_path)

    if event == cv2.EVENT_LBUTTONDOWN:
        position = [(x, y)]

        with open(file_name, 'a') as f:
            f.writelines('(' + str(x) + ', ' + str(y) + ')')
            f.writelines("\t")

    elif event == cv2.EVENT_LBUTTONUP:
        position.append((x, y))

        with open(file_name, 'a') as f:
            f.writelines('(' + str(x) + ', ' + str(y) + ')')
            f.writelines("\n")

        f.close()

    cv2.rectangle(img, position[0], position[1], (0, 255, 0))


def delete_coordinate(image):
    file_path = './coordinate/' + image.split('.')[0] + '.txt'
    with open(file_path, 'r') as f:
        lines = f.readlines()
        if lines is None:
            print('no marks!')
        else:
            lines = lines[:-1]
            f.close()
    if lines is not None:
        with open(file_path, 'w') as f:
            f.writelines(lines)
            f.close()
        print("deleted!")


# file directory
# enter image directory (absolute path)
PATH = input("please enter image directory (absolute path): ")

image_list = get_images_list(PATH)

for image in image_list:
    img = cv2.imread(PATH + image)
    cv2.namedWindow(image, cv2.WINDOW_NORMAL)

    cv2.setMouseCallback(image, mouse_position)

    while(1):
        cv2.imshow(image, img)
        key = cv2.waitKey(10) & 0XFF
        if key == 32:
            break
        elif key == 27:
            delete_coordinate(image)
            font = cv2.FONT_ITALIC
            cv2.putText(img, 'Deleted!', (0, 20), font, 1, (0, 0, 255), 5, cv2.LINE_AA)

    cv2.destroyAllWindows()







