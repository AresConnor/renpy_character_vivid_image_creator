init python:
    def kotori_chaofeng_talking_func(st,at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag == 'kotori_voice':
            return ('kotori_chaofeng_speaking',0.1)
        else:
            return ('kotori_quiet',0.1)

    def kotori_normal_talking_func(st,at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag == 'kotori_voice':
            return ('kotori_normal_speaking',0.1)
        else:
            return ('kotori_quiet',0.1)

    def kotori_shy_talking_func(st,at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag == 'kotori_voice':
            return ('kotori_shy_speaking',0.1)
        else:
            return ('kotori_quiet',0.1)

