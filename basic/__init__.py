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
    # デモグラフィック情報
    q_gender = models.CharField(
        initial=None,
        choices=['男性', '女性', 'その他', '回答しない'],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">1. あなたの性別を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_age = models.CharField(
        initial=None,
        choices=['19歳以下', '20-29歳', '30-39歳', '40-49歳', '50-59歳', '60-69歳', '70歳以上'],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">2. あなたの年代を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_area = models.CharField(
        initial=None,
        choices=['北海道', '東北地方', '関東地方',
                '中部地方', '近畿地方', '中国地方', 
                '四国地方', '九州地方', '回答しない'], 
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">3. お住まいの地方を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_education = models.CharField(
        initial=None,
        choices=['中学校卒業', '高等学校卒業', '専門学校卒業', '短期大学卒業', 
                '大学卒業', '大学院修了（修士）', '大学院修了（博士）', 'その他'],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">4. あなたの最終学歴を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_device = models.CharField(
        initial=None,
        choices=['パソコン', 'タブレット', 'スマートフォン', 'それ以外'], 
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">5. 現在お使いの回答端末を教えてください。</span>',
        widget=widgets.RadioSelect
    )


# PAGES
class StartPage(Page):
    """アンケート開始ページ"""
    pass


class HonestyPage(Page):
    """誠実性確認ページ"""
    pass


class DemographicPage(Page):
    """デモグラフィック情報収集ページ"""
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_area', 'q_education', 'q_device']


class Results(Page):
    """完了ページ"""
    pass


page_sequence = [StartPage, HonestyPage, DemographicPage, Results]