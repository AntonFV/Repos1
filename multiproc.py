from PIL import Image
from multiprocessing import Process,Pool
import multiprocessing
import time
new_img = Image.new('RGB', (500, 500), 'blue')
uu=new_img.convert("L")
uu.save('out_color_image.jpg')

gg=new_img.rotate(90)
gg.save('out_rotate_image.jpg')

new_size = (800, 600)
newSize=new_img.resize(new_size)
newSize.save('out_resize_imag.jpg')





def resize_function():
    new_size=(800, 600)
    newSizeImg=new_img.resize(new_size)
    newSizeImg.save('out_resized_image.jpg')
    
def color_function():
    newColorImg=new_img.convert('L')
    newColorImg.save('out_coloured_image.jpg')


def rotate_function():
    imgRotate=new_img.rotate(-90)
    imgRotate.save('out_rotated_image.jpg')

if __name__ == "__main__":

    processes = []
    
    process=multiprocessing.Process(target=resize_function,)
    processes.append(process)
    process2=multiprocessing.Process(target=rotate_function,)
    processes.append(process2)
    process3=multiprocessing.Process(target=color_function,)
    processes.append(process3)
    process.start()
    process2.start()
    process3.start()
    
    for process in processes:
        process.join()
        process2.join()
        process3.join()
        
    print("Все процессы завершены")