# 图片名:kotori# 识别到:3种表情(标签)
#     chaofeng
#     normal
#     shy
# voice_tag = kotori_voice

init:
    image kotori_always:
        'images/chara/kotori/琴里.png'

    image kotori_chaofeng_emotion:
        'images/chara/kotori/emotion/chaofeng.png'
    image kotori_normal_emotion:
        'images/chara/kotori/emotion/normal.png'
    image kotori_shy_emotion:
        'images/chara/kotori/emotion/shy.png'

    image kotori_chaofeng_wink0:
        'images/chara/kotori/eye_wink/chaofeng/0.png'
    image kotori_chaofeng_wink1:
        'images/chara/kotori/eye_wink/chaofeng/1.png'
    image kotori_chaofeng_wink2:
        'images/chara/kotori/eye_wink/chaofeng/2.png'
    image kotori_chaofeng_wink3:
        'images/chara/kotori/eye_wink/chaofeng/3.png'
    image kotori_normal_wink0:
        'images/chara/kotori/eye_wink/normal/0.png'
    image kotori_normal_wink1:
        'images/chara/kotori/eye_wink/normal/1.png'
    image kotori_normal_wink2:
        'images/chara/kotori/eye_wink/normal/2.png'
    image kotori_normal_wink3:
        'images/chara/kotori/eye_wink/normal/3.png'
    image kotori_shy_wink0:
        'images/chara/kotori/eye_wink/shy/0.png'
    image kotori_shy_wink1:
        'images/chara/kotori/eye_wink/shy/1.png'
    image kotori_shy_wink2:
        'images/chara/kotori/eye_wink/shy/2.png'
    image kotori_shy_wink3:
        'images/chara/kotori/eye_wink/shy/3.png'

    image kotori_chaofeng_speaking0:
        'images/chara/kotori/speaking/chaofeng/0.png'
    image kotori_chaofeng_speaking1:
        'images/chara/kotori/speaking/chaofeng/1.png'
    image kotori_chaofeng_speaking2:
        'images/chara/kotori/speaking/chaofeng/2.png'
    image kotori_normal_speaking0:
        'images/chara/kotori/speaking/normal/0.png'
    image kotori_normal_speaking1:
        'images/chara/kotori/speaking/normal/1.png'
    image kotori_normal_speaking2:
        'images/chara/kotori/speaking/normal/2.png'
    image kotori_shy_speaking0:
        'images/chara/kotori/speaking/shy/0.png'
    image kotori_shy_speaking1:
        'images/chara/kotori/speaking/shy/1.png'
    image kotori_shy_speaking2:
        'images/chara/kotori/speaking/shy/2.png'

image kotori_chaofeng_winking:
    'kotori_chaofeng_wink0'
    choice 5:
        5.0
    choice 4:
        3.0
    choice 1:
        1.0
    'kotori_chaofeng_wink1'
    0.03
    'kotori_chaofeng_wink2'
    0.03
    'kotori_chaofeng_wink3'
    0.03
    'kotori_chaofeng_wink2'
    0.05
    'kotori_chaofeng_wink1'
    0.05
    repeat

image kotori_normal_winking:
    'kotori_normal_wink0'
    choice 5:
        5.0
    choice 4:
        3.0
    choice 1:
        1.0
    'kotori_normal_wink1'
    0.03
    'kotori_normal_wink2'
    0.03
    'kotori_normal_wink3'
    0.03
    'kotori_normal_wink2'
    0.05
    'kotori_normal_wink1'
    0.05
    repeat

image kotori_shy_winking:
    'kotori_shy_wink0'
    choice 5:
        5.0
    choice 4:
        3.0
    choice 1:
        1.0
    'kotori_shy_wink1'
    0.03
    'kotori_shy_wink2'
    0.03
    'kotori_shy_wink3'
    0.03
    'kotori_shy_wink2'
    0.05
    'kotori_shy_wink1'
    0.05
    repeat

image kotori_chaofeng_speaking:
    'kotori_chaofeng_speaking0'
    0.1
    'kotori_chaofeng_speaking1'
    0.1
    'kotori_chaofeng_speaking2'
    0.1
    'kotori_chaofeng_speaking1'
    0.1
    repeat

image kotori_normal_speaking:
    'kotori_normal_speaking0'
    0.1
    'kotori_normal_speaking1'
    0.1
    'kotori_normal_speaking2'
    0.1
    'kotori_normal_speaking1'
    0.1
    repeat

image kotori_shy_speaking:
    'kotori_shy_speaking0'
    0.1
    'kotori_shy_speaking1'
    0.1
    'kotori_shy_speaking2'
    0.1
    'kotori_shy_speaking1'
    0.1
    repeat

image kotori_quiet:
    Color(color='#0000', hls=None, hsv=None, rgb=None, alpha=0)
    xsize 96
    ysize 36

image kotori_chaofeng_talking = DynamicDisplayable(kotori_chaofeng_talking_func)
image kotori_normal_talking = DynamicDisplayable(kotori_normal_talking_func)
image kotori_shy_talking = DynamicDisplayable(kotori_shy_talking_func)

layeredimage kotori:
    always:
        'kotori_always'
    group emotion:
        pos (192, 111)
        attribute normal default:
            'kotori_normal_emotion'
        attribute chaofeng:
            'kotori_chaofeng_emotion'
        attribute shy:
            'kotori_shy_emotion'
    group eye:
        pos (267,242)
        attribute normal default:
            'kotori_normal_winking'
        attribute chaofeng:
            'kotori_chaofeng_winking'
        attribute shy:
            'kotori_shy_winking'
    group mouth:
        pos (298,283)
        attribute chaofeng:
            'kotori_chaofeng_talking'
        attribute normal:
            'kotori_normal_talking'
        attribute shy:
            'kotori_shy_talking'
