from otree.api import *


doc = """
Using LLM Survey Application
"""


class C(BaseConstants):
    NAME_IN_URL = 'using_llm'
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

    q_llm_experience = models.CharField(
        initial=None,
        choices=['毎日使用', '週に数回', '月に数回', 'たまに使用', '使ったことがない'],
        verbose_name='LLM（大規模言語モデル）をどの程度使用しますか？',
        widget=widgets.RadioSelect
    )

    q_llm_trust = models.CharField(
        initial=None,
        choices=['とても信頼している', 'やや信頼している', 'どちらでもない', 'あまり信頼していない', '全く信頼していない'],
        verbose_name='LLMの回答や提案をどの程度信頼しますか？',
        widget=widgets.RadioSelect
    )


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_llm_experience', 'q_llm_trust']


class Results(Page):
    pass


page_sequence = [Page1, Results]