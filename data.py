# data.py
# База учебных сценариев для игры "Фишинг-Детектив"

EMAILS = [
    {
        "sender": "support@paypal-security.com",
        "subject": "Urgent: Your account has been limited",
        "body": "Dear customer, we detected unusual activity. Please click here to verify your identity: http://paypal-secure.xyz/verify",
        "is_phishing": True,
        "explanation": "Адрес отправителя не совпадает с официальным доменом paypal.com. Ссылка ведёт на подозрительный сайт. Используется срочность.",
        "hints": ["Проверьте домен отправителя.", "Наведите курсор на ссылку, чтобы увидеть реальный URL."]
    },
    {
        "sender": "newsletter@github.com",
        "subject": "Your weekly GitHub digest",
        "body": "Here are the latest updates from your repositories. Visit https://github.com/notifications to see more.",
        "is_phishing": False,
        "explanation": "Домен github.com официальный. Нет срочных требований. Ссылка ведёт на настоящий сайт GitHub.",
        "hints": []
    },
    {
        "sender": "security@amazon-support.com",
        "subject": "Your Amazon account has been compromised",
        "body": "We detected unauthorized access. Please reset your password immediately: http://amazon-security-update.com",
        "is_phishing": True,
        "explanation": "Домен amazon-support.com не является официальным. Ссылка ведёт на фишинговый сайт. Срочный тон.",
        "hints": ["Официальный Amazon использует домен amazon.com.", "Ссылка не ведёт на amazon.com."]
    },
    {
        "sender": "no-reply@github.com",
        "subject": "Your password was changed",
        "body": "Your GitHub password was successfully changed. If you did not make this change, please contact support immediately.",
        "is_phishing": False,
        "explanation": "Письмо от официального домена github.com. Нет ссылок с требованием ввести данные.",
        "hints": []
    },
    {
        "sender": "hr@yourcompany.com",
        "subject": "Important: Update your direct deposit information",
        "body": "Please download the attached form and fill in your new bank details. Send it back to hr@yourcompany.com.",
        "is_phishing": True,
        "explanation": "Запрос конфиденциальных финансовых данных по электронной почте — типичный признак фишинга. Всегда проверяйте такие запросы по телефону.",
        "hints": ["Никогда не отправляйте банковские данные по email.", "Проверьте отправителя: домен может быть подделан."]
    },
    {
        "sender": "news@medium.com",
        "subject": "Daily digest for you",
        "body": "Here are today's top stories. Read more at https://medium.com",
        "is_phishing": False,
        "explanation": "Официальный домен medium.com. Нет подозрительных ссылок или запросов данных.",
        "hints": []
    },
    {
        "sender": "admin@secure-bank.com",
        "subject": "Your statement is ready",
        "body": "Please login to view your statement: http://secure-bank.com/login",
        "is_phishing": True,
        "explanation": "Домен secure-bank.com может быть поддельным. Банки обычно не просят переходить по ссылкам из письма.",
        "hints": ["Проверьте, совпадает ли домен с официальным сайтом банка.", "Лучше зайти в банк через официальное приложение или вручную ввести адрес."]
    }
]

WEBSITES = [
    {
        "name": "Fake Bank Login",
        "description": "Страница, похожая на вход в интернет-банк.",
        "elements": [
            {"text": "URL: http://secure-bank-login.com", "is_suspicious": True,
             "explanation": "HTTP вместо HTTPS и домен не является официальным."},
            {"text": "Логотип: Bank of America с немного неправильным шрифтом", "is_suspicious": True,
             "explanation": "Поддельный логотип — частый признак фишинга."},
            {"text": "Форма: поля «Логин» и «Пароль»", "is_suspicious": False,
             "explanation": "Обычные поля для входа."},
            {"text": "Кнопка: «Войти»", "is_suspicious": False, "explanation": "Стандартная кнопка."},
            {"text": "Мелкий текст: «Входя, вы соглашаетесь с условиями» со скрытой ссылкой",
             "is_suspicious": True,
             "explanation": "Скрытые ссылки или необычные условия могут быть признаком мошенничества."}
        ]
    },
    {
        "name": "Fake Amazon Page",
        "description": "Страница, имитирующая Amazon.",
        "elements": [
            {"text": "URL: https://amaz0n.com", "is_suspicious": True,
             "explanation": "Домен amaz0n.com с нулём вместо «o» — типичный фишинг."},
            {"text": "Логотип Amazon", "is_suspicious": False,
             "explanation": "Логотип выглядит правильно, но домен уже подозрителен."},
            {"text": "Форма: ввод данных кредитной карты", "is_suspicious": True,
             "explanation": "Amazon не запрашивает данные карты на главной странице без входа."},
            {"text": "Кнопка «Купить сейчас»", "is_suspicious": False, "explanation": "Обычная кнопка."},
            {"text": "Отсутствие HTTPS-замка", "is_suspicious": True,
             "explanation": "Нет защищённого соединения — данные могут быть перехвачены."}
        ]
    },
    {
        "name": "Fake Government Services",
        "description": "Страница, выдающая себя за государственный сервис.",
        "elements": [
            {"text": "URL: http://gosuslugi-portal.ru", "is_suspicious": True,
             "explanation": "Неправильный домен, HTTP вместо HTTPS."},
            {"text": "Логотип с ошибкой в названии", "is_suspicious": True,
             "explanation": "Опечатки в логотипе — признак подделки."},
            {"text": "Поля для ввода СНИЛС и пароля", "is_suspicious": False,
             "explanation": "Обычные поля для госуслуг."},
            {"text": "Кнопка «Войти»", "is_suspicious": False, "explanation": "Стандартная кнопка."},
            {"text": "Мелкий текст: «Ваш аккаунт будет заблокирован через 24 часа»", "is_suspicious": True,
             "explanation": "Давление и угрозы — признак фишинга."}
        ]
    }
]