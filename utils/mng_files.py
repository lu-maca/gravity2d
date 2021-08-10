import os
from os import listdir

def deleteFiles():
    my_path = 'C:\\Users\\Luca\\Desktop\\progetti\\fisica1\\gravity\\RESULTS\\POS\\'
    for file_name in listdir(my_path):
        if file_name.endswith('.txt'):
            os.remove(my_path + file_name)

    my_path = 'C:\\Users\\Luca\\Desktop\\progetti\\fisica1\\gravity\\RESULTS\\VEL\\'
    for file_name in listdir(my_path):
        if file_name.endswith('.txt'):
            os.remove(my_path + file_name)