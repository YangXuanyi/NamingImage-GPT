from OFA_Chinese.component.ofa.modeling_ofa import OFAModel
from torchvision import transforms
from PIL import Image
from glob import glob
from transformers import BertTokenizerFast
import time
from PyQt5.QtWidgets import QApplication

def OFA_generate_SingleProcess(model_path, image_path, prompt, progressBar):
    '''
    使用OFA模型从输入图像中提取对应的文字内容, 用于处理单张图像
    :param model_path: OFA模型路径
    :param image_path: 图像路径
    :param prompt:     询问提示词
    :param progressBar: 处理进度显示条控件
    :return: 返回提取文字内容
    '''
    # 初始化model和tokenizer
    model = OFAModel.from_pretrained(model_path)
    progressBar.setValue(20)
    tokenizer = BertTokenizerFast.from_pretrained(model_path)
    progressBar.setValue(30)
    # 初始化图片预处理器
    mean, std = [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]
    resolution = 256
    patch_resize_transform = transforms.Compose([
            lambda image: image.convert("RGB"),
            transforms.Resize((resolution, resolution), interpolation=Image.BICUBIC),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std)
        ])
    input_ids = tokenizer([prompt], return_tensors="pt").input_ids
    progressBar.setValue(40)

    img = Image.open(image_path)
    patch_images = patch_resize_transform(img).unsqueeze(0)
    # 生成caption
    gen = model.generate(input_ids, patch_images=patch_images, num_beams=5, no_repeat_ngram_size=3)
    progressBar.setValue(80)
    text = tokenizer.batch_decode(gen, skip_special_tokens=True)[0].replace(' ', '')
    print(text)
    return str(text)


def OFA_generate_BatchProcess(model_path, image_path_list, prompt, textBrowser, progressBar):
    '''
    使用OFA模型从输入图像中提取对应的文字内容, 用于处理单张图像
    :param model_path: OFA模型路径
    :param image_path_list: 待处理的图像路径list
    :param prompt:     询问提示词
    :param progressBar: 处理进度显示条控件
    :return: 返回提取文字内容
    '''
    # 初始化model和tokenizer
    model = OFAModel.from_pretrained(model_path)
    tokenizer = BertTokenizerFast.from_pretrained(model_path)
    progressBar.setValue(10)
    # 初始化图片预处理器
    mean, std = [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]
    resolution = 256
    patch_resize_transform = transforms.Compose([
            lambda image: image.convert("RGB"),
            transforms.Resize((resolution, resolution), interpolation=Image.BICUBIC),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std)
        ])
    input_ids = tokenizer([prompt], return_tensors="pt").input_ids
    progressBar.setValue(15)

    num_image = len(image_path_list) #待处理图像数量
    content_list = []  #用来存储所有图像的文字提取内容
    current_process = 15  #当前处理进度
    step_process = int((95-current_process)/ num_image) #处理一张图片的进展幅度

    for i in range(0, num_image):
        print(image_path_list[i])
        img = Image.open(image_path_list[i])
        patch_images = patch_resize_transform(img).unsqueeze(0)
        # 生成caption
        gen = model.generate(input_ids, patch_images=patch_images, num_beams=5, no_repeat_ngram_size=3)
        text = tokenizer.batch_decode(gen, skip_special_tokens=True)[0].replace(' ', '')
        #对每个图像的text内容做格式化处理: 去掉里面可能含有的换行字符; 统一以图i:开头
        if '\n' in text:
            text = text.replace('\n', ' ')
        text = '图' + str(i) + ': ' + text
        content_list.append(text)
        #显示最新处理结果并更新进度条
        textBrowser.append(text)
        current_process = current_process + step_process
        progressBar.setValue(current_process)
        QApplication.processEvents()

    return content_list

# model_path = './ofa-cn-base-muge-v2'
# image_path = 'F:/NEU_Project_Code/GitHub/NamingImage-GPT/imgs/robot.png'
# prompt = '图片描述了什么?'
# OFA_generate(model_path, image_path, prompt)