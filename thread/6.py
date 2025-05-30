import threading
from PIL import Image
import numpy as np

def grayscale(image_array, num_threads=4):
    height, width, _ = image_array.shape
    img = np.zeros((height, width, 3), dtype=image_array.dtype)

    def process_rows(thread_id, start_row, end_row):
        print(f"THREAD {thread_id} -> processando linhas {start} até {end}.")
        for y in range(start_row, end_row):
            for x in range(width):
                r, g, b = image_array[y][x]
                gray = (int(r) + int(g) + int(b)) // 3
                img[y][x] = [gray, gray, gray]
        print(f"THREAD {thread_id} - terminou.")

    thread_range = height // num_threads
    print(f"\nnumero de threads: {num_threads}")
    print("linhas por thread:", thread_range)
    threads = []

    for i in range(num_threads):
        start = i * thread_range
        end = height if i == num_threads - 1 else (i + 1) * thread_range
        t = threading.Thread(target=process_rows, args=(i, start, end,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return img

if __name__ == "__main__":
    n = input("nome da imagem para transfomar (ou nenhuma pra usar imagem pre-definida): ")
    if not n:
        img = Image.open('image.jpg') # input de test
        print("\nimagem selecionada: image.jpg")
    else:
        img = Image.open(n)
        print(f"imagem selecionada: {n}")
    image_arr = np.array(img)


    r = grayscale(image_arr, 6)
    Image.fromarray(r).save("grayscale.jpg")
    print("imagem modificada salva como: grayscale.jpg")