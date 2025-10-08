from otree.api import *


doc = """
Basic Survey Application
"""


class C(BaseConstants):
    NAME_IN_URL = 'basic'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_gender = models.CharField(
        initial=None,
        choices=['男性', '女性', '回答しない'],
        verbose_name='あなたの性別を教えてください。',
        widget=widgets.RadioSelect
    )

    q_age = models.IntegerField(
        initial=None,
        verbose_name='あなたの年齢を教えてください。',
        choices=range(0, 125)
    )

    q_area = models.CharField(
        initial=None,
        choices=['北海道', '東北地方', '関東地方',
                '中部地方', '近畿地方', '中国地方', 
                '四国地方', '九州地方'], 
        verbose_name='お住まいの地方を教えてください。'
    )

    q_device = models.CharField(
        initial=None,
        choices=['パソコン', 'タブレット', 'スマートフォン', 'それ以外'], 
        verbose_name='回答端末を教えてください',
        widget=widgets.RadioSelect
    )


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_area', 'q_device']


class Results(Page):
    pass


page_sequence = [Page1, Results]