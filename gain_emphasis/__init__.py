from otree.api import *


doc = """
Gain Emphasis Survey Application
"""


class C(BaseConstants):
    NAME_IN_URL = 'gain_emphasis'
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
        choices=range(0, 80)
    )

    q_gain_focus = models.CharField(
        initial=None,
        choices=['非常に重要', 'やや重要', 'どちらでもない', 'あまり重要でない', '全く重要でない'],
        verbose_name='利益や成功を強調した情報をどの程度重視しますか？',
        widget=widgets.RadioSelect
    )

    q_positive_outcomes = models.CharField(
        initial=None,
        choices=['とても魅力的', 'やや魅力的', 'どちらでもない', 'あまり魅力的でない', '全く魅力的でない'],
        verbose_name='ポジティブな結果や成果についての説明をどう感じますか？',
        widget=widgets.RadioSelect
    )


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_gain_focus', 'q_positive_outcomes']


class Results(Page):
    pass


page_sequence = [Page1, Results]