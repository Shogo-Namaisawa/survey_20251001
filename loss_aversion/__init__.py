from otree.api import *


doc = """
Loss Aversion Survey Application
"""


class C(BaseConstants):
    NAME_IN_URL = 'loss_aversion'
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

    q_loss_sensitivity = models.CharField(
        initial=None,
        choices=['非常に敏感', 'やや敏感', 'どちらでもない', 'あまり敏感でない', '全く敏感でない'],
        verbose_name='損失やリスクに対してどの程度敏感ですか？',
        widget=widgets.RadioSelect
    )

    q_risk_avoidance = models.CharField(
        initial=None,
        choices=['いつも避ける', 'よく避ける', '時々避ける', 'あまり避けない', '全く避けない'],
        verbose_name='リスクのある選択肢を避ける傾向がありますか？',
        widget=widgets.RadioSelect
    )


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_loss_sensitivity', 'q_risk_avoidance']


class Results(Page):
    pass


page_sequence = [Page1, Results]