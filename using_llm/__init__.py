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

    # BigFive質問項目
    big5_1 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">1.活発で，外向的だと思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_2 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">2.他人に不満をもち，もめごとを起こしやすいと思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_3 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">3.しっかりしていて，自分に厳しいと思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_4 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">4.心配性で，うろたえやすいと思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_5 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">5.新しいことが好きで，変わった考えをもつと思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_6 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">6.ひかえめで，おとなしいと思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_7 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">7.人に気をつかう，やさしい人間だと思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_8 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">8.だらしなく，うっかりしていると思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_9 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">9.冷静で，気分が安定していると思う</span>',
        widget=widgets.RadioSelect()
    )

    big5_10 = models.IntegerField(
        initial=None,
        choices=[
            [1, '1：全く違うと思う'],
            [2, '2：おおよそ違うと思う'],
            [3, '3：少し違うと思う'],
            [4, '4：どちらでもない'],
            [5, '5：少しそう思う'],
            [6, '6：まあまあそう思う'],
            [7, '7：強くそう思う'],
        ],
        verbose_name='<span style="font-size: 1.4rem; font-weight: 900;">10.発想力に欠けた，平凡な人間だと思う</span>',
        widget=widgets.RadioSelect()
    )

    # BigFive計算用フィールド
    Gaiko = models.IntegerField()
    Kyocho = models.IntegerField()
    Kinben = models.IntegerField()
    Shinkei = models.IntegerField()
    Kaiho = models.IntegerField()


# PAGES
class StartPage(Page):
    """アンケート開始ページ"""
    pass


class HonestyPage(Page):
    """ナッジ提示ページ（LLM使用）"""
    pass


class DemographicPage(Page):
    """デモグラフィック情報収集ページ"""
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_area', 'q_education', 'q_device']


class BigFivePage(Page):
    """BigFive心理調査ページ"""
    form_model = 'player'
    form_fields = ['big5_1', 'big5_2', 'big5_3', 'big5_4', 'big5_5',
                   'big5_6', 'big5_7', 'big5_8', 'big5_9', 'big5_10']


class ConspiracyPage(Page):
    """陰謀論信奉尺度調査ページ"""
    pass


class CrtPage(Page):
    """認知反射テスト調査ページ"""
    pass


class Results(Page):
    """完了ページ"""
    pass


page_sequence = [StartPage, HonestyPage, DemographicPage, BigFivePage, ConspiracyPage, CrtPage, Results]