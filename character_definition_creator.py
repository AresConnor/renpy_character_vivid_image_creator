"""
文件格式:
chara_dir = 'images/chara/<chara_dir_name>'
<emotion_name[1,2,3....]>必須前後相等

<chara_dir_name>:文件结构 ——>
<any_file_name>.png                            <== 层叠式图像:always
|--emotion                                     <== 层叠式图像:group emotion
    |--(xxx,yyy)                               <== 位置
    |--<emotion_name1>.png                     <== 动画1
    |--<emotion_name2>.png                     <== 动画2
    |--...
|--eye_wink
    |--(xxx,yyy)
    |--<emotion_name1>
        |--0.png
        |--1.png
        |--2.png
        |--3.png
    |--<emotion_name2>
        |--0.png
        |--1.png
        |--2.png
        |--3.png
    |-- ...
|--speaking
    |--(xxx,yyy)
    |--<emotion_name1>
        |--0.png
        |--1.png
        |--2.png
    |--<emotion_name2>
        |--0.png
        |--1.png
        |--2.png
    |-- ...


    注意！
    注意！
    注意！
    注意！
    注意！
    <emotion_name>的集合中必须包含一个'normal'表情！作为 默认表情
"""

import os


def read_pos_from_file(filename):
    if filename.startswith('(') and filename.endswith(')'):
        pos = (
            int(filename[1:filename.index(',')]), int(filename[filename.index(',') + 1:filename.index(')')]))
        return pos
    else:
        return None


def turn_str_into_int(__str):
    try:
        return int(__str)
    except:
        return None


class Character_dynamic(object):
    def __init__(self, name=None, chara_dir_name=None, chara_voice_tag: str = None):

        self.__name = name
        self.__voice_tag = chara_voice_tag
        self.__chara_dir_name = chara_dir_name
        self.__chara_img_path = f'./images/chara/{chara_dir_name}'
        self.__chara_default_img = None
        self.__chara_group_names = []

        self.__chara_attributes = []

        self.__emotion_group_pos = None
        self.__eye_wink_group_pos = None
        self.__speaking_group_pos = None

        self.__emotion_group_imgs = {}
        self.__eye_wink_group_imgs = {}
        self.__speaking_group_imgs = {}

        self.__emotion_group_anime = {}
        self.__eye_wink_group_anime = {}
        self.__speaking_group_anime = {}

        for file_obj in os.listdir(self.__chara_img_path):
            # 判断是否为文件 并且 扩展名为png
            if os.path.isfile(os.path.join(self.__chara_img_path, file_obj)) and (
                    'png' in os.path.splitext(file_obj)[1]):
                self.__chara_default_img = os.path.join(file_obj)
            elif os.path.isdir(os.path.join(self.__chara_img_path, file_obj)):
                self.__chara_group_names.append(file_obj)

        if {'emotion', 'eye_wink', 'speaking'}.issubset(self.__chara_group_names):
            pass
        else:
            raise Exception(f'请检查角色文件夹\'{os.path.join(self.__chara_img_path)}\'内的格式是否正确!')

        for file_obj1 in os.listdir(os.path.join(self.__chara_img_path, 'emotion')):
            if 'png' in os.path.splitext(file_obj1)[1]:
                self.__chara_attributes.append(os.path.splitext(file_obj1)[0])
                self.__emotion_group_imgs.update({os.path.splitext(file_obj1)[0]: file_obj1})
            elif os.path.isfile(os.path.join(self.__chara_img_path, 'emotion', file_obj1)):
                self.__emotion_group_pos = read_pos_from_file(file_obj1)

        if 'normal' in self.__chara_attributes:
            pass
        else:
            raise Exception('请检查是否有normal表情,该表情会作为默认表情加载!!!')

        # 判断eye_wink speaking 文件夹里是否有和emotion文件夹内相同名字的表情文件夹
        if set(self.__chara_attributes).issubset(os.listdir(os.path.join(self.__chara_img_path, 'eye_wink'))) and set(
                self.__chara_attributes).issubset(os.listdir(os.path.join(self.__chara_img_path, 'speaking'))):
            pass
        else:
            raise Exception(
                f'请检查角色文件夹\'{os.path.join(self.__chara_img_path)}\'下的eye_wink|speaking文件夹内的表情文件夹名是否与emotion文件夹内的保持一致!')

        # eye_wink
        # file_obj2 = <emotion_name> img = <image file under DIR<emotion_name>>
        for file_obj2 in os.listdir(os.path.join(self.__chara_img_path, 'eye_wink')):
            file_obj_curr_path = os.path.join(self.__chara_img_path, 'eye_wink', file_obj2)
            if os.path.isfile(file_obj_curr_path):
                self.__eye_wink_group_pos = read_pos_from_file(file_obj2)
            elif os.path.isdir(file_obj_curr_path) and file_obj2 in self.__chara_attributes:
                self.__eye_wink_group_imgs.update({
                    file_obj2: []
                })
                img_list = os.listdir(file_obj_curr_path)
                for img in img_list:
                    name, ext = os.path.splitext(img)
                    if (os.path.isfile(os.path.join(file_obj_curr_path, img))) and (
                            turn_str_into_int(name) is not None) and ('png' in ext):
                        self.__eye_wink_group_imgs[file_obj2].append(img)

        # speaking
        # file_obj2 = <emotion_name> img = <image file under DIR<emotion_name>>
        for file_obj3 in os.listdir(os.path.join(self.__chara_img_path, 'speaking')):
            file_obj_curr_path = os.path.join(self.__chara_img_path, 'speaking', file_obj3)
            if os.path.isfile(os.path.join(self.__chara_img_path, 'speaking', file_obj3)):
                self.__speaking_group_pos = read_pos_from_file(file_obj3)
            elif os.path.isdir(file_obj_curr_path) and file_obj3 in self.__chara_attributes:
                self.__speaking_group_imgs.update({
                    file_obj3: []
                })
                img_list = os.listdir(file_obj_curr_path)
                for img in img_list:
                    name, ext = os.path.splitext(img)
                    if (os.path.isfile(os.path.join(file_obj_curr_path, img))) and (
                            turn_str_into_int(name) is not None) and ('png' in ext):
                        self.__speaking_group_imgs[file_obj3].append(img)

    def __create_eye_wink_anime_from_images(self):
        """
                返回值[0] init代码块
                返回值[1] 普通代码块
        """
        """
        image_dict : {
            <emotion1>:[0.png, 1.png, 2.png...],
            <emotion2>:[0.png, 1.png, 2.png...],
            ...
        }
        """
        image_object_addr_list = {}

        # init: 代码块中内容
        str2write_init = ''
        for k in self.__eye_wink_group_imgs.keys():
            v = self.__eye_wink_group_imgs[k]
            i = 0
            image_object_addr_list.update({k: []})
            for img in v:
                image_object_addr = f'{self.__chara_img_path[2:]}/eye_wink/{k}/{img}'
                str2write_init = str2write_init + f'\timage {self.__name}_{k}_wink{i}:\n\t\t\'{image_object_addr}\'\n'
                image_object_addr_list[k].append(f'{self.__name}_{k}_wink{i}')
                i += 1

        # 普通代码块中内容 --> str2write_nor
        str2write_nor = ''
        for k in image_object_addr_list.keys():
            v = image_object_addr_list[k]
            str2write_nor = str2write_nor + f'image {self.__name}_{k}_winking:\n'

            self.__eye_wink_group_anime.update({
                k: f'{self.__name}_{k}_winking'
            })

            str2write_nor = str2write_nor + f'\t\'{v[0]}\'\n\tchoice 5:\n\t\t5.0\n\tchoice 4:\n\t\t3.0\n\tchoice 1:\n\t\t1.0\n'
            for i in range(1, len(v)):
                str2write_nor = str2write_nor + f'\t\'{v[i]}\'\n\t0.03\n'
            v.reverse()
            for i in range(1, len(v) - 1):
                str2write_nor = str2write_nor + f'\t\'{v[i]}\'\n\t0.05\n'
            str2write_nor = str2write_nor + '\trepeat\n\n'

        return str2write_init + '\n', str2write_nor

    def __create_speaking_anime_from_images(self):
        """
        返回值[0] init代码块
        返回值[1] 普通代码块
        """
        image_object_addr_list = {}

        # init: 代码块中内容
        str2write_init = ''
        for k in self.__speaking_group_imgs.keys():
            v = self.__speaking_group_imgs[k]
            i = 0
            image_object_addr_list.update({k: []})
            for img in v:
                image_object_addr = f'{self.__chara_img_path[2:]}/speaking/{k}/{img}'
                str2write_init = str2write_init + f'\timage {self.__name}_{k}_speaking{i}:\n\t\t\'{image_object_addr}\'\n'
                image_object_addr_list[k].append(f'{self.__name}_{k}_speaking{i}')
                i += 1

        # 普通代码块中内容 --> str2write_nor
        str2write_nor = ''
        for k in image_object_addr_list.keys():
            v = image_object_addr_list[k]
            str2write_nor = str2write_nor + f'image {self.__name}_{k}_speaking:\n'
            for i in range(0, len(v)):
                str2write_nor = str2write_nor + f'\t\'{v[i]}\'\n\t0.1\n'
            v.reverse()
            for i in range(1, len(v) - 1):
                # 不做最后一个表情的0.1差分:
                str2write_nor = str2write_nor + f'\t\'{v[i]}\'\n\t0.1\n'

                """if i == 1:
                    str2write_nor = str2write_nor + f'\t\'{v[i]}\'\n'
                else:
                    str2write_nor = str2write_nor + f'\t\'{v[i]}\'\n\t0.1\n'"""
            str2write_nor = str2write_nor + '\trepeat\n\n'
        return str2write_init + '\n', str2write_nor

    def __create_emotion_image(self):
        """
        init 代码块
        """
        emotion2str = ''
        for k in self.__emotion_group_imgs.keys():
            emotion2str += f'\timage {self.__name}_{k}_emotion:\n'

            self.__emotion_group_anime.update({
                k: f'{self.__name}_{k}_emotion'
            })

            emotion2str += f'\t\t\'{self.__chara_img_path[2:]}/emotion/{self.__emotion_group_imgs[k]}\'\n'
        return emotion2str + '\n'

    def __create_speaking_functions(self):
        """
        init python:代码块
        """
        func2str = ''
        for attrib in self.__chara_attributes:
            func2str += f'\tdef {self.__name}_{attrib}_talking_func(st,at):\n'
            func2str += f'\t\tif renpy.music.is_playing(channel=\'voice\') and _get_voice_info().tag == \'{self.__voice_tag}\':\n'
            func2str += f'\t\t\treturn (\'{self.__name}_{attrib}_speaking\',0.1)\n'
            func2str += '\t\telse:\n'
            func2str += f'\t\t\treturn (\'{self.__name}_quiet\',0.1)\n\n'
        return func2str

    def __create_chara_quiet_image(self):
        """
        普通 代码块
        """
        quiet_image = f'image {self.__name}_quiet:\n'
        quiet_image += '\tColor(color=\'#0000\', hls=None, hsv=None, rgb=None, alpha=0)\n'
        quiet_image += '\txsize 96\n'
        quiet_image += '\tysize 36\n'
        return quiet_image + '\n'

    def __create_always_image(self):
        """
        init 代码块
        """
        alway_image = ''
        alway_image += f'\timage {self.__name}_always:\n'
        alway_image += f'\t\t\'{self.__chara_img_path[2:]}/{self.__chara_default_img}\'\n\n'
        return alway_image

    def __from_func_create_dynamicDisplayable(self):
        DynamicDisplayable2str = ''
        for attrib in self.__chara_attributes:
            DynamicDisplayable2str += f'image {self.__name}_{attrib}_talking = DynamicDisplayable({self.__name}_{attrib}_talking_func)\n'
            self.__speaking_group_anime.update({
                attrib: f'{self.__name}_{attrib}_talking'
            })
        return DynamicDisplayable2str + '\n'

    def __create_layeredimage(self):
        layeredimage = ''
        layeredimage += f'layeredimage {self.__name}:\n'
        layeredimage += f'\talways:\n'
        layeredimage += f'\t\t\'{self.__name}_always\'\n'
        # group emotion
        layeredimage += '\tgroup emotion:\n'
        layeredimage += f'\t\tpos {self.__emotion_group_pos}\n'

        # 确保default在最上层
        for attrib in self.__emotion_group_imgs.keys():
            if attrib == 'normal':
                layeredimage += f'\t\tattribute {attrib} default:\n'
            else:
                continue
            layeredimage += f'\t\t\t\'{self.__emotion_group_anime[attrib]}\'\n'
        for attrib in self.__emotion_group_imgs.keys():
            if attrib == 'normal':
                continue
            else:
                layeredimage += f'\t\tattribute {attrib}:\n'
            layeredimage += f'\t\t\t\'{self.__emotion_group_anime[attrib]}\'\n'

        # group eye
        layeredimage += '\tgroup eye:\n'
        layeredimage += f'\t\tpos ({self.__emotion_group_pos[0] + self.__eye_wink_group_pos[0]},{self.__emotion_group_pos[1] + self.__eye_wink_group_pos[1]})\n'
        # 确保default在最上层
        for attrib in self.__eye_wink_group_imgs.keys():
            if attrib == 'normal':
                layeredimage += f'\t\tattribute {attrib} default:\n'
            else:
                continue
            layeredimage += f'\t\t\t\'{self.__eye_wink_group_anime[attrib]}\'\n'
        for attrib in self.__eye_wink_group_imgs.keys():
            if attrib == 'normal':
                continue
            else:
                layeredimage += f'\t\tattribute {attrib}:\n'
            layeredimage += f'\t\t\t\'{self.__eye_wink_group_anime[attrib]}\'\n'
        # group mouth
        layeredimage += '\tgroup mouth:\n'
        layeredimage += f'\t\tpos ({self.__emotion_group_pos[0] + self.__speaking_group_pos[0]},{self.__emotion_group_pos[1] + self.__speaking_group_pos[1]})\n'
        for attrib in self.__eye_wink_group_imgs.keys():
            layeredimage += f'\t\tattribute {attrib}:\n'
            layeredimage += f'\t\t\t\'{self.__speaking_group_anime[attrib]}\'\n'

        return layeredimage

    def __createImageDefinition(self):
        always_image = self.__create_always_image()
        wink_init, wink_normal = self.__create_eye_wink_anime_from_images()
        speaking_init, speaking_normal = self.__create_speaking_anime_from_images()
        emotion_init = self.__create_emotion_image()
        speaking_func_initPython = self.__create_speaking_functions()


        content = ''
        content_python = ''
        # 文件说明:
        content += f'# 图片名:{self.__name}'
        content += f'# 识别到:{len(self.__chara_attributes)}种表情(标签)\n'
        for attrib in self.__chara_attributes:
            content += f'#     {attrib}\n'
        content += f'# voice_tag = {self.__voice_tag}\n\n'

        # init block:
        content += 'init:\n'
        content += always_image + emotion_init + wink_init + speaking_init

        # init python block:
        content_python += 'init python:\n'
        content_python += speaking_func_initPython

        # renpy block:
        quiet_image_str = self.__create_chara_quiet_image()
        dd_items = self.__from_func_create_dynamicDisplayable()
        layered_image_str = self.__create_layeredimage()
        content += wink_normal + speaking_normal + quiet_image_str + dd_items + layered_image_str

        content = content.replace('\t', '    ')
        content_python = content_python.replace('\t', '    ')
        return content, content_python

    def createDefinitionFiles(self):
        content_renpy, content_python = self.__createImageDefinition()
        with open(f'{self.__name}_image_renpy.rpy', 'w', encoding='utf-8') as fp:
            fp.write(content_renpy)
            fp.close()
        with open(f'{self.__name}_image_python.rpy', 'w', encoding='utf-8') as fp:
            fp.write(content_python)
            fp.close()


if __name__ == '__main__':
    # Character_dynamic类有三个参数:名称,所在目录名,voice_tag(角色character定义时需要用到<角色说话>)
    # Character_dynamic类只有一个public方法,作用是根据现有的文件结构生成层叠式图像定义
    kotori = Character_dynamic('kotori', 'kotori', 'kotori_voice')
    kotori.createDefinitionFiles()
