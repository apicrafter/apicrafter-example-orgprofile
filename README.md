# API Crafter example organization profile

Этот пример демонстрирует использование API проекта APICrafter, без SDK, напрямую из Python

Утилита oprofcmd.py собирает данные по юридическому лицу и сохраняет их в папку data/ИНН организации/...
Данные из каждого источника сохраняются отдельным файлом, дополнительно не обрабатываются и доступны "как есть".

Для работы утилиты нужен ключ доступа к API, его можно оформить на сайте https://beta.apicrafter.ru или запросить 
письмом на apicrafter@apicrafter.ru 


## Работа

Дл я работы утилиты надо выполнить команды:

Инициализировать с кодом ключа

    python oprofcmd.py init ... 

Просмотреть список проверяемых баз (профилей) юридического лица

    python oprofcmd.py profiles

Собрать сведения по юр.лицу (пример с ИНН 3328101380, АО "ГАЗПРОМ ГАЗОРАСПРЕДЕЛЕНИЕ ВЛАДИМИР")

    python oprofcmd.py collect 3328101380 


## Пример результатов сбора данных
Каждый JSON файл содержит сведения из одного источника данных.

    berezka_cust.json
    cust_contracts_223fz.json
    egrul.json
    fnsdebtam.json
    fnspaytax.json
    fnsrevexp.json
    gzcustomer.json
    naturalmon.json
    rknoperpd.json
    rostruddecl.json
    roszdravlic.json
    statreg.json
    supp_contracts.json
    supp_contracts_223fz.json
    trudorgs.json
    woodcontractlease.json


## Пример содержания

Сведения о суммах недоимки и задолженности по пеням и штрафам, файл fnsdebtam.json

    [
        {
            "_id": "60817caa4a8ca8f47ac60642",
            "org": {
                "orgname": "АКЦИОНЕРНОЕ ОБЩЕСТВО \"ГАЗПРОМ ГАЗОРАСПРЕДЕЛЕНИЕ ВЛАДИМИР\"",
                "inn": "3328101380"
            },
            "arrears": {
                "taxname": "Страховые и другие взносы на обязательное пенсионное страхование, зачисляемые в Пенсионный фонд Российской Федерации",
                "unpaidtaxsumm": 0.0,
                "penaltysumm": 0.09,
                "finesumm": 0.0,
                "arrearssumm": 0.09
            },
            "id": "45d0c9bb-c4ff-4dd0-8a64-87922c012f5e",
            "date_doc": "Sat, 10 Apr 2021 00:00:00 GMT",
            "date_formed": "Tue, 31 Dec 2019 00:00:00 GMT"
        }
    ]

