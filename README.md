# renpy_character_vivid_image_creator
永恒天希程序组-角色立绘效果生成器

角色图片存放位置位于 <项目>/game/images/chara/<角色图片文件夹名称>/ 下

文件结构如下 ——>
<any_file_name>.png                            <== 层叠式图像:always
|--emotion                                     <== 层叠式图像:group emotion
    |--(xxx,yyy)                               <== 图层的位置
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

