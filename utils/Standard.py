from data.Trash_dataset import Trash_BBOX_LABEL_NAMES
from utils.config import opt


def final_devide(name):
    if opt.standard == 'Shenzhen':
        class_name, color_name = Shenzhen[name]
    
    return class_name, color_name

Shenzhen = {
    'applecore': ['Food Waste', 'green'],
    'banana_peel': ['Food Waste', 'green'],
    'battery': ['Hazardous Waste', 'red'],
    'book': ['Recyclable', 'blue'],
    'button_battery': ['Hazardous Waste', 'red'],
    'capsule': ['Hazardous Waste', 'red'],
    'cigarette_case': ['Recyclable', 'blue'],
    'cigarette_butt': ['Residual Waste', 'black'],
    'lunch_box': ['Recyclable', 'blue'],
    'paper_cup': ['Recyclable', 'blue'],
    'modulator_tube': ['Hazardous Waste', 'red'],
    'glass_bottle': ['Recyclable', 'blue'],
    'mask': ['Hazardous Waste', 'red'],
    'mercurial_thermometer': ['Hazardous Waste', 'red'],
    'mobilephone': ['Recyclable', 'blue'],
    'carton': ['Recyclable', 'blue'],
    'pencil': ['Recyclable', 'blue'],
    'plastic_bottle': ['Recyclable', 'blue'],
    'remote_control': ['Recyclable', 'blue'],
    'tea_leaf': ['Food Waste', 'green'],
    'shoe': ['Recyclable', 'blue'],
    'can': ['Recyclable', 'blue'],
    'rice': ['Food Waste', 'green'],
    'tin_can': ['Recyclable', 'blue'],
    'toothbrush': ['Recyclable', 'blue'],
    'trousers': ['Recyclable', 'blue'],
    't_shirt': ['Recyclable', 'blue'],
    'vegetable_leaf': ['Food Waste', 'green'],
    'waste_paper': ['Recyclable', 'blue'],
    'watermelon_peel': ['Food Waste', 'green']
}
