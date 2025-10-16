from otree.api import *
import openai


doc = """
Basic Survey Application
"""


class C(BaseConstants):
    NAME_IN_URL = 'using_llm'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
############## コメントアウトを解除して、ここにAPI KEY を入力してください。##########################
    # OPENAI_API_KEY = ''
#############################################################################################

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # APIで生成されたナッジメッセージを保存する
    nudge_message = models.LongStringField(
        initial="アンケート調査では設問と関係のない回答や設問をよく読まない不真面目な回答が問題となっております。"
    )

    # デモグラフィック情報
    q_gender = models.IntegerField(
        initial=None,
        choices=[
            [0, '男性'],
            [1, '女性'],
            [2, 'その他']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">1. あなたの性別を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_age = models.IntegerField(
        initial=None,
        choices=[
            [0, '19歳以下'],
            [1, '20-29歳'],
            [2, '30-39歳'],
            [3, '40-49歳'],
            [4, '50-59歳'],
            [5, '60-69歳'],
            [6, '70歳以上']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">2. あなたの年代を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_area = models.IntegerField(
        initial=None,
        choices=[
            [0, '北海道'],
            [1, '東北地方'],
            [2, '関東地方'],
            [3, '中部地方'],
            [4, '近畿地方'],
            [5, '中国地方'],
            [6, '四国地方'],
            [7, '九州地方'],
            [8, '回答しない']
        ], 
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">3. お住まいの地方を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_education = models.IntegerField(
        initial=None,
        choices=[
            [0, '中学校卒業'],
            [1, '高等学校卒業'],
            [2, '専門学校卒業'],
            [3, '短期大学卒業'],
            [4, '大学卒業'],
            [5, '大学院修了'],
            [6, 'その他']
        ],
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">4. あなたの最終学歴を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    q_device = models.IntegerField(
        initial=None,
        choices=[
            [0, 'パソコン'],
            [1, 'タブレット'],
            [2, 'スマートフォン'],
            [3, 'それ以外']
        ], 
        verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">5. 現在お使いの回答端末を教えてください。</span>',
        widget=widgets.RadioSelect
    )

    # BigFive質問項目
    big5_1 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">1.活発で，外向的だと思う</span>',
                                widget=widgets.RadioSelect()
                                )

    big5_2 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">2.他人に不満をもち，もめごとを起こしやすいと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_3 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">3.しっかりしていて，自分に厳しいと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_4 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">4.心配性で，うろたえやすいと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_5 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">5.新しいことが好きで，変わった考えをもつと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_6 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">6.ひかえめで，おとなしいと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_7 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">7.人に気をつかう，やさしい人間だと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    # 不真面目回答者を抽出する項目, 
    big5_IMC =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">8.この選択肢では下から三番目を選択してください</span>',
                                widget=widgets.RadioSelect()
                                )

    big5_8 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">9.だらしなく，うっかりしていると思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_9 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">10.冷静で，気分が安定していると思う</span>',
                                widget=widgets.RadioSelect()
                                )


    big5_10 =  models.IntegerField(initial=None,
                                    choices=[
                                        [1, '1：全く違うと思う'],
                                        [2, '2：おおよそ違うと思う'],
                                        [3, '3：少し違うと思う'],
                                        [4, '4：どちらでもない'],
                                        [5, '5：少しそう思う'],
                                        [6, '6：まあまあそう思う'],
                                        [7, '7：強くそう思う'],
                                        ],
                                verbose_name='<span style="font-size: 1.2rem; font-weight: 500;">11.発想力に欠けた，平凡な人間だと思う</span>',
                                widget=widgets.RadioSelect()
                                )


    Gaiko = models.IntegerField()
    Kyocho = models.IntegerField()
    Kinben = models.IntegerField()
    Shinkei = models.IntegerField()
    Kaiho = models.IntegerField()



    # 陰謀論信奉尺度(ConspiracyPage)
    inboron1 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>政府は、無辜の市民やよく知られた有名人の殺害に関与し、そのことを秘密にしている。</B>',
                                widget=widgets.RadioSelect
                                )
    inboron2 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>国家元首のもつ権力は、世界政治を実際に支配している小規模で未知の集団がもつ権力にはかなわない。</B>',
                                widget=widgets.RadioSelect
                                )
    inboron3 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>秘密組織が地球外生命体とコンタクトをとっているが、その事実は大衆には伏せられている。</B>',
                                widget=widgets.RadioSelect
                                )
    inboron4 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>ある種の病原体や病気の感染拡大は、ある組織による慎重かつ秘匿された活動の結果である。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron5 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>科学者の集団が、大衆を欺くために証拠を操作、ねつ造、または隠蔽している。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron6 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>政府は、自国へのテロ行為を容認、またはそれに関与し、その関与を偽装している。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron7 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>小規模の秘密の集団が、戦争の開始といった世界の重要な意思決定の責任を担っている。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron8 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>異星人からの接触の証拠は、大衆には伏せられている。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron9 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>マインドコントロールを可能にする技術は、人知れず使われている。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron10 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>現在の産業に不都合な先進技術は規制されている。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron11 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>政府は、犯罪行為への関与を隠すために、人々をカモにしている。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron12 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>いくつかの重大な出来事は、秘密裏に世界を操っている小集団の活動の結果である。</B>',
                                widget=widgets.RadioSelect
                                )

    # 不真面目回答を抽出する設問(IMC)
    inboronIMC = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>この選択肢では、たぶん正しいを選択してください。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron13 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>UFOの目撃情報や噂の中には、実際の異星人との接触から注意を逸らすために計画的に作られた、または仕組まれたものがある。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron14 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>新しい薬や技術の実験は、知らされることなく、また同意を得ることなしに、日常的に大衆に対して行われている。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron15 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>多くの重要な情報が、私利私欲のために大衆から慎重に隠蔽されている。</B>',
                                widget=widgets.RadioSelect
                                )

    inboron16 = models.IntegerField(initial=None,
                                choices=[
                                    [1, 'きっと正しくない'],[2, 'たぶん正しくない'],
                                    [3, 'わからない・決められない'],
                                    [4, 'たぶん正しい'],[5, 'きっと正しい']],
                                verbose_name='<B>新型コロナウイルスの感染拡大は、ある組織による慎重かつ秘匿された活動の結果である。</B>',
                                widget=widgets.RadioSelect
                                )

    #CRTテスト
    crt_bat = models.PositiveIntegerField()
    crt_widget = models.PositiveIntegerField()
    crt_lake = models.PositiveIntegerField()
    crt_DQS = models.PositiveIntegerField()
    crt_rank = models.PositiveIntegerField()

# PAGES
class StartPage(Page):
    """アンケート開始ページ
    """
    pass


class DemographicPage(Page):
    """デモグラフィック情報収集ページ"""
    form_model = 'player'
    form_fields = ['q_gender', 'q_age', 'q_area', 'q_education', 'q_device']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # OpenAI clientを初期化
        client = openai.OpenAI(api_key=C.OPENAI_API_KEY)

        # OpenAI APIに送信するプロンプトを定義
        prompt_text = "あなたはアンケートで誠実な回答を促すためのメッセージを生成するAIです。行動経済学のナッジ理論にもとづき、不誠実回答者を減らすメッセージを考えてください。"

        # APIを呼び出し
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt_text},
                    {"role": "user", "content": "100字以内でメッセージを生成してください。"}
                ],
                temperature=0.9,
                max_tokens=300 # トークン数の調整
            )
            # 生成されたメッセージをPlayerモデルに保存
            generated_text = response.choices[0].message.content.strip()
            player.nudge_message = generated_text
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            player.nudge_message = "エラーによりメッセージを生成できませんでした。そのままお進みください。"


class NudgePage(Page):
    """LLMによる生成ナッジ提示ページ"""
    # StartPageの次へボタンがAPI呼び出しのトリガーなのでここでの処理はない
    pass


class BigFivePage(Page):
    """BigFive心理調査ページ"""
    form_model = 'player'
    form_fields = ['big5_1',
                   'big5_2',
                   'big5_3',
                   'big5_4',
                   'big5_5',
                   'big5_6',
                   'big5_7',
                   'big5_IMC', # 不適切回答者を抽出する項目
                   'big5_8',
                   'big5_9',
                   'big5_10']

    #@staticmethod

class ConspiracyPage(Page):
    """陰謀論信奉尺度調査ページ"""
    form_model = Player
    form_fields = [
        'inboron1', 'inboron2', 'inboron3', 'inboron4', 'inboron5', 'inboron6', 
        'inboron7', 'inboron8', 'inboron9', 'inboron10', 'inboron11', 'inboron12', 
        'inboronIMC', 'inboron13', 'inboron14', 'inboron15', 'inboron16'
    ]

class CrtPage(Page):
    """認知反射テスト調査ページ"""
    form_model = 'player'
    form_fields = ['crt_bat',
                  'crt_widget',
                  'crt_lake',
                  'crt_DQS', # 不真面目回答者を抽出する設問
                  'crt_rank']


class Results(Page):
    """完了ページ"""
    pass


page_sequence = [StartPage, DemographicPage, NudgePage, BigFivePage, ConspiracyPage, CrtPage, Results]