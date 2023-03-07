# MENGUBAH FILE KE LIST INTEGER
def file_to_binary(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        binary_list = [int(byte) for byte in binary_data]
    return binary_list

#print(binary_list)

# MENGUBAH LIST INTEGER KE FILE
def binary_to_file(binary_list, file_path):
    binary_data = bytes(binary_list)
    with open(file_path, 'wb') as file:
        file.write(binary_data)

#file_path = "new_text.png" # replace with the file path you want to write to
#binary_to_file(binary_list, file_path)

# MENGUBAH LIST INTEGER KE BINER
def int_list_to_binary(int_list):
    binary_list = []
    for integer in int_list:
        binary_str = format(integer, '08b')
        for digit in binary_str:
            binary_list.append(int(digit))
    return binary_list

#int_list = [65, 66, 67] # replace with your own list of integers
#binary_list = int_list_to_binary(int_list)
#print(binary_list)

# MENGUBAH BINER KE LIST INTEGER
def binary_to_int_list(binary_list):
    int_list = []
    binary_str = ''.join(str(bit) for bit in binary_list)
    for i in range(0, len(binary_str), 8):
        byte_str = binary_str[i:i+8]
        int_list.append(int(byte_str, 2))
    return int_list

#binary_list = [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1] # replace with your own binary list
#int_list = binary_to_int_list(binary_list)
#print(int_list)

# MELENGKAPI LIST AGAR ANGGOTANYA MENJADI KELIPATAN 2073600
def fill_binary_list(binary_list):
    x = 2073600 - ((len(binary_list)) % 2073600)
    fill = [0 for i in range(x)]
    filled_binary_list = binary_list + fill
    return filled_binary_list

# MEMBUAT LIST OF FRAMES
def split_to_frames(binary_list):
    # Menghitung panjang setiap list dalam tuple
    list_length = 2073600

    # Memecah list binary_list menjadi sekumpulan list dengan panjang list_length
    frame_lists = [binary_list[i:i+list_length] for i in range(0, len(binary_list), list_length)]

    # Mengembalikan hasil
    return frame_lists


# BUAT FRAME
import numpy as np
from PIL import Image
import os

def save_frames_as_png(frame_lists):
    if not os.path.exists('test'):
        os.makedirs('test')
    
    for i, frame in enumerate(frame_lists):
        # Ubah list menjadi matriks
        matrix = np.array(frame).reshape((1080, 1920))

        # Ubah matriks menjadi gambar PIL
        image = Image.fromarray((matrix * 255).astype(np.uint8), mode='L')

        # Simpan gambar ke dalam folder "test"
        filename = f"test/frame_{i+1}.png"
        image.save(filename)
        print("frame",i+1,"created")

# LAUNCH

file_path = "test.pdf"
int_list = file_to_binary(file_path)

binary_list = int_list_to_binary(int_list)

filled_binary_list = fill_binary_list(binary_list)

frame_lists = split_to_frames(filled_binary_list)

save_frames_as_png(frame_lists)
