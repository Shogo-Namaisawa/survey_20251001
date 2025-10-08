from otree.api import *


doc = """
Pre-commitment Survey Application
"""


class C(BaseConstants):
    NAME_IN_URL = 'pre_commitment'
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

    q_commitment_preference = models.CharField(
        initial=None,
        choices=['とても重視する', 'やや重視する', 'どちらでもない', 'あまり重視しない', '全く重視しない'],
        verbose_name='約束や計画を守ることをどの程度重視しますか？',
        widget=widgets.RadioSelect
    )

    q_future_planning = models.CharField(
        initial=None,
        choices=['いつもする', 'よくする', '時々する', 'あまりしない', '全くしない'],
        verbose_name='将来の計画を立てることはありますか？',
        widget=widgets.RadioSelect
    )


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_commitment_preference', 'q_future_planning']


class Results(Page):
    pass


page_sequence = [Page1, Results]