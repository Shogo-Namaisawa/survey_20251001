from os import environ

SESSION_CONFIGS = [
    dict(
        name = 'basic',
        display_name = 'Basic',
        num_demo_participants = 1,
        app_sequence = ['basic']
    ),

    dict(
        name = 'pre_commitment',
        display_name = 'Pre_commitment',
        num_demo_participants = 1,
        app_sequence = ['pre_commitment']
    ),

    dict(
        name = 'gain_emphasis',
        display_name = 'Gain_emphasis',
        num_demo_participants = 1,
        app_sequence = ['gain_emphasis']
    ),

    dict(
        name = 'loss_aversion',
        display_name = 'Loss_aversion',
        num_demo_participants = 1,
        app_sequence = ['loss_aversion']
    ),

    dict(
        name = 'using_llm',
        display_name = 'Using_LLM',
        num_demo_participants = 1,
        app_sequence = ['using_llm']
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6654196676519'

ROOMS = [
    dict(
        name = 'label',
        display_name = '実験参加者 label',
        participant_label_file = '_rooms/label.txt',
    ),
]