# data.py
# База учебных сценариев для игры "Фишинг-Детектив"

EMAILS = [
    {
        "sender": "support@paypal-security.com",
        "subject": "Urgent: Your account has been limited",
        "body": "Dear customer, we detected unusual activity. Please click here to verify your identity: http://paypal-secure.xyz/verify",
        "is_phishing": True,
        "difficulty": 1,
        "signs": [
            "Подозрительный адрес отправителя",
            "Срочные требования",
            "Подозрительные ссылки"
        ],
        "explanation": "Адрес отправителя не совпадает с официальным доменом paypal.com. Ссылка ведёт на подозрительный сайт. Используется срочность.",
        "hints": [
            "Обратите внимание на адрес отправителя — он точно официальный?",
            "Домен paypal-security.com не совпадает с официальным paypal.com.",
            "Это фишинг: поддельный адрес, срочность и ссылка на чужой сайт."
        ]
    },
    {
        "sender": "newsletter@github.com",
        "subject": "Your weekly GitHub digest",
        "body": "Here are the latest updates from your repositories. Visit https://github.com/notifications to see more.",
        "is_phishing": False,
        "difficulty": 1,
        "signs": [],
        "explanation": "Домен github.com официальный. Нет срочных требований. Ссылка ведёт на настоящий сайт GitHub.",
        "hints": [
            "Проверьте домен отправителя.",
            "Домен github.com — официальный.",
            "Это безопасное письмо: официальный домен, нет давления, ссылка ведёт на github.com."
        ]
    },
    {
        "sender": "security@amazon-support.com",
        "subject": "Your Amazon account has been compromised",
        "body": "We detected unauthorized access. Please reset your password immediately: http://amazon-security-update.com",
        "is_phishing": True,
        "difficulty": 2,
        "signs": [
            "Подозрительный адрес отправителя",
            "Срочные требования",
            "Подозрительные ссылки"
        ],
        "explanation": "Домен amazon-support.com не является официальным. Ссылка ведёт на фишинговый сайт. Срочный тон.",
        "hints": [
            "Проверьте домен отправителя.",
            "Официальный Amazon использует только amazon.com.",
            "Это фишинг: домен amazon-support.com — подделка, ссылка не на amazon.com."
        ]
    },
    {
        "sender": "no-reply@github.com",
        "subject": "Your password was changed",
        "body": "Your GitHub password was successfully changed. If you did not make this change, please contact support immediately.",
        "is_phishing": False,
        "difficulty": 2,
        "signs": [],
        "explanation": "Письмо от официального домена github.com. Нет ссылок с требованием ввести данные.",
        "hints": [
            "Проверьте домен отправителя.",
            "Домен github.com — официальный.",
            "Это безопасное письмо: официальный домен, нет ссылок на сторонние сайты."
        ]
    },
    {
        "sender": "hr@yourcompany.com",
        "subject": "Important: Update your direct deposit information",
        "body": "Please download the attached form and fill in your new bank details. Send it back to hr@yourcompany.com.",
        "is_phishing": True,
        "difficulty": 3,
        "signs": [
            "Запрос персональных данных",
            "Срочные требования"
        ],
        "explanation": "Запрос конфиденциальных финансовых данных по электронной почте — типичный признак фишинга. Всегда проверяйте такие запросы по телефону.",
        "hints": [
            "Что именно просят сделать в письме?",
            "Запрос банковских данных по email — красный флаг.",
            "Это фишинг: ни один банк или HR не запрашивает реквизиты по email."
        ]
    },
    {
        "sender": "news@medium.com",
        "subject": "Daily digest for you",
        "body": "Here are today's top stories. Read more at https://medium.com",
        "is_phishing": False,
        "difficulty": 1,
        "signs": [],
        "explanation": "Официальный домен medium.com. Нет подозрительных ссылок или запросов данных.",
        "hints": [
            "Проверьте домен отправителя.",
            "Домен medium.com — официальный.",
            "Это безопасное письмо: официальный домен, нет запросов данных."
        ]
    },
    {
        "sender": "admin@secure-bank.com",
        "subject": "Your statement is ready",
        "body": "Please login to view your statement: http://secure-bank.com/login",
        "is_phishing": True,
        "difficulty": 3,
        "signs": [
            "Подозрительный адрес отправителя",
            "Подозрительные ссылки"
        ],
        "explanation": "Домен secure-bank.com может быть поддельным. Банки обычно не просят переходить по ссылкам из письма.",
        "hints": [
            "Проверьте домен и ссылку.",
            "Домен secure-bank.com не совпадает с официальным доменом банка.",
            "Это фишинг: домен поддельный, ссылка ведёт не на официальный сайт."
        ]
    }
]

WEBSITES = [
    {
        "name": "Fake Bank Login",
        "description": "Страница, похожая на вход в интернет-банк.",
        "difficulty": 1,
        "elements": [
            {"text": "URL: http://secure-bank-login.com", "is_suspicious": True,
             "sign": "Подозрительный URL",
             "explanation": "HTTP вместо HTTPS и домен не является официальным."},
            {"text": "Логотип: Bank of America с немного неправильным шрифтом", "is_suspicious": True,
             "sign": "Поддельный логотип",
             "explanation": "Поддельный логотип — частый признак фишинга."},
            {"text": "Форма: поля «Логин» и «Пароль»", "is_suspicious": False,
             "explanation": "Обычные поля для входа."},
            {"text": "Кнопка: «Войти»", "is_suspicious": False, "explanation": "Стандартная кнопка."},
            {"text": "Мелкий текст: «Входя, вы соглашаетесь с условиями» со скрытой ссылкой",
             "is_suspicious": True, "sign": "Скрытые условия",
             "explanation": "Скрытые ссылки или необычные условия могут быть признаком мошенничества."}
        ]
    },
    {
        "name": "Fake Amazon Page",
        "description": "Страница, имитирующая Amazon.",
        "difficulty": 2,
        "elements": [
            {"text": "URL: https://amaz0n.com", "is_suspicious": True,
             "sign": "Подозрительный URL",
             "explanation": "Домен amaz0n.com с нулём вместо «o» — типичный фишинг."},
            {"text": "Логотип Amazon", "is_suspicious": False,
             "explanation": "Логотип выглядит правильно, но домен уже подозрителен."},
            {"text": "Форма: ввод данных кредитной карты", "is_suspicious": True,
             "sign": "Запрос конфиденциальных данных",
             "explanation": "Amazon не запрашивает данные карты на главной странице без входа."},
            {"text": "Кнопка «Купить сейчас»", "is_suspicious": False, "explanation": "Обычная кнопка."},
            {"text": "Отсутствие HTTPS-замка", "is_suspicious": True,
             "sign": "Отсутствие HTTPS",
             "explanation": "Нет защищённого соединения — данные могут быть перехвачены."}
        ]
    },
    {
        "name": "Fake Government Services",
        "description": "Страница, выдающая себя за государственный сервис.",
        "difficulty": 3,
        "elements": [
            {"text": "URL: http://gosuslugi-portal.ru", "is_suspicious": True,
             "sign": "Подозрительный URL",
             "explanation": "Неправильный домен, HTTP вместо HTTPS."},
            {"text": "Логотип с ошибкой в названии", "is_suspicious": True,
             "sign": "Поддельный логотип",
             "explanation": "Опечатки в логотипе — признак подделки."},
            {"text": "Поля для ввода СНИЛС и пароля", "is_suspicious": False,
             "explanation": "Обычные поля для госуслуг."},
            {"text": "Кнопка «Войти»", "is_suspicious": False, "explanation": "Стандартная кнопка."},
            {"text": "Мелкий текст: «Ваш аккаунт будет заблокирован через 24 часа»", "is_suspicious": True,
             "sign": "Давление и угрозы",
             "explanation": "Давление и угрозы — признак фишинга."}
        ]
    }
]

# Словарь рекомендаций по темам
RECOMMENDATIONS = {
    "Подозрительный адрес отправителя": "Всегда проверяйте домен отправителя. Официальные компании используют только свои домены (например, paypal.com, а не paypal-security.com).",
    "Срочные требования": "Фишинговые письма часто давят на эмоции: «срочно», «немедленно», «аккаунт будет заблокирован». Настоящие компании так не пишут.",
    "Подозрительные ссылки": "Наводите курсор на ссылку перед кликом — реальный адрес может отличаться от текста. Не переходите по ссылкам из писем, лучше введите адрес вручную.",
    "Запрос персональных данных": "Никогда не отправляйте пароли, номера карт, СНИЛС и другие данные по email. Банки и госорганы так не делают.",
    "Подозрительный URL": "Проверяйте адресную строку. Поддельные домены часто имитируют настоящие (amaz0n.com вместо amazon.com) или используют лишние слова (secure-bank-login.com).",
    "Поддельный логотип": "Присмотритесь к логотипу: ошибки в шрифте, цвете или написание — признак подделки.",
    "Скрытые условия": "Читайте мелкий текст. Мошенники прячут там важные условия или ссылки.",
    "Отсутствие HTTPS": "Настоящие сайты используют HTTPS (замок в адресной строке). Если его нет — не вводите данные.",
    "Запрос конфиденциальных данных": "Если сайт просит данные карты на главной странице без входа — это подозрительно.",
    "Давление и угрозы": "Угрозы («аккаунт заблокируют») — типичный приём мошенников. Не паникуйте, проверьте информацию на официальном сайте."
}