import gzip
from pynbt import NBTFile
from array import array
from PIL import Image as im
from PIL.Image import Image
from typing import List, Tuple

from core.service.constants import *


def convert_id_to_color(id: int) -> Tuple[int]:
    r = (BASE_COLORS[id // 4]['r'] * SHADES_COEFFICIENTS[id % 4]) // 255
    g = (BASE_COLORS[id // 4]['g'] * SHADES_COEFFICIENTS[id % 4]) // 255
    b = (BASE_COLORS[id // 4]['b'] * SHADES_COEFFICIENTS[id % 4]) // 255
    return (r, g, b)


def paint_img(color_array) -> Image:
    img = im.new('RGB', (BASE_A, BASE_A))
    for i in range(BASE_A * BASE_A):
        y = i // BASE_A
        x = i % BASE_A
        color = convert_id_to_color(color_array[i])
        img.putpixel((x, y), color)
    return img


def get_color_array(map_file_name: str) -> array:
    with gzip.open(map_file_name, 'rb') as gzip_file:
        nbt = NBTFile(gzip_file)
        blockbytes = nbt['data']['colors'].value
        data = array('b', blockbytes)
        return data


def get_image_map(map_file_name: str) -> Image:
    color_array = get_color_array(map_file_name)
    img = paint_img(color_array)
    return img


def save_images_map(image_list: List[List[Image]], image_name: str):
    rows = len(image_list)
    columns = len(image_list[0])
    result = im.new('RGB', (columns*BASE_A, rows*BASE_A))
    
    for row in range(rows):
        for column in range(columns):
            tmp = image_list[row][column] if image_list[row][column] else im.new('RGB', (BASE_A, BASE_A))
            result.paste(tmp, (column*BASE_A, row*BASE_A))
    
    result.save(image_name, 'PNG')