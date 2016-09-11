# -*- coding: utf-8 -*
""" tts/talk.py

Django の DB 情報から OpenJtalk を操作します。
"""
from os import path
from srp.settings import MEDIA_ROOT, MEDIA_URL


class OpenJTalk(object):
    """
    from tts.models import Roid
    roid = Roid.objects.get(pk=1)    # キャラクターを設定
    jt = OpenJTalk()                 # OpenJTalk に必須の引数を設定
    jt.set_voiceModel(roid.voiceModel.path)   # OpenJTalk に音響モデルを渡す
    jt.run()
    """
    wdir = path.join(MEDIA_ROOT, 'wav')
    url = path.join(MEDIA_URL, 'wav')

    def __init__(self):
        from srp.settings import DIC_DIR
        from tts.models import OpenJTalk

        if OpenJTalk.objects.get(pk=1):
            openjtalk = OpenJTalk.objects.get(pk=1)
            self.openjtalk = openjtalk.openJTalk
        else:
            self.openjtalk = 'open_jtalk'
        self.dic = DIC_DIR
        self.set_wpath()

    def set_wpath(self, wfile=None):
        """
        wav ファイルの出力先を設定します
        """
        if wfile:
            self.wpath = wpath
        else:
            from datetime import datetime
            # 出力先の wav ファイル名を指定
            now = datetime.now()
            fname = now.strftime('%Y_%m_%d_%H_%M_%s')
            wav_name = fname + '.wav'
            log_name = fname + '.log'
            self.wav_path = path.join(self.wdir, wav_name)
            self.wav_url = path.join(self.url, wav_name)
            self.log_path = path.join(self.wdir, log_name)
            self.log_url = path.join(self.url, log_name)

    def set_voiceModel(self, voiceModel):
        self.voiceModel = voiceModel

    def run(self, text, log=False, speech_speed=None, half_tone=None, log_F0=None, all_pass=None):
        """
        OpenJTalk を実行します。

        text (str): 発話する文字列
        log (bool): ログファイルを残す [False]
        speech_speed (float): 発話速度 [1.0][0.0--*]
        half_tone(float): 声の高さ [0.0][*--*]
        all_pass (float): 声質 [0.0--1.0]
        log_F0 (float): 抑揚 [1.0][0.0--*]
        """
        from subprocess import Popen, PIPE
        if isinstance(text, unicode):
            text = text.encode('utf-8')

        echo = [
            'echo',
            '{0}'.format(text)
        ]
        jtalk = [
            self.openjtalk,
            '-m', self.voiceModel,
            '-x', self.dic,
            '-ow', self.wav_path
        ]
        if log:
            jtalk.extend(['-ot', self.log_path])
        if speech_speed:
            jtalk.extend(['-r', str(speech_speed)])
        if half_tone:
            jtalk.extend(['-fm', str(half_tone)])
        if log_F0:
            jtalk.extend(['-jf', str(log_F0)])
        if all_pass:
            jtalk.extend(['-a', str(all_pass)])

        proc_echo = Popen(echo, stdout=PIPE)
        proc_jtalk = Popen(jtalk, stdin=proc_echo.stdout, stdout=PIPE)
        proc_echo.stdout.close()
        return proc_jtalk.communicate()
