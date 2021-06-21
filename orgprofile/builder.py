# -*- coding: utf8 -*-
import os
from .sources.crafter import get_egrul, get_supplier_contracts_44fz, get_customer_contracts_44fz, get_customer
from .sources.crafter import get_supplier_contracts_223fz, get_customer_contracts_223fz

from .sources.crafter import DIRECT_DATACRAFTER_URL, LOCAL_DATACRAFTER_URL
import json
from orgprofile.sources.crafter import get_crafter_basic

SOURCES_MAP  = {'balances' : {'epoint' : '/gks/orgbalances', 'prefix' : DIRECT_DATACRAFTER_URL, 'qkey' : 'inn',  'help' : 'Бухгалтерские балансы юридических лиц'},
               'statreg' : {'epoint' : '/gks/statreg', 'prefix' : DIRECT_DATACRAFTER_URL, 'qkey' : 'inn', 'help' : 'Статрегистр Росстата' },
               'egrul' : {'method' : get_egrul, 'help' : 'ЕГРЮЛ'},
               'supp_contracts' : {'method' : get_supplier_contracts_44fz, 'help' : 'Государственные и муниципальные контракты. Поставщик'},
               'cust_contracts' : {'method' : get_customer_contracts_44fz, 'help' : 'Государственные и муниципальные контракты. Заказчик'},
               'supp_contracts_223fz' : {'method' : get_supplier_contracts_223fz, 'help' : 'Контракты по 223-ФЗ. Поставщик'},
               'cust_contracts_223fz' : {'method' : get_customer_contracts_223fz, 'help' : 'Контракты по 223-ФЗ. Заказчик'},
               'gzcustomer' :{'method' : get_customer, 'help' : 'Реестр государственных и муниципальных заказчиков'},
               'subsidies': {'epoint': '/minfin/subsidiesdocs', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'receiver.inn', 'help': 'Реестр соглашений на предоставлений субсидий федерального бюджета '},
               'msp' :{'epoint' : '/rmsp/rmsp', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'org.inn', 'help' : 'Реестр малых и средних предприятий'},
               'budgetreg': {'epoint': '/budgetreg/budgetreg', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'info.inn', 'help': 'Реестр участников и неучастников бюджетного процесса'},
               #               'nko' : {'method' : get_ngo, 'help' : 'Данные из портала Открытые НКО'},
               'itaccreditorgs': {'epoint': '/minsvyaz/accreditorgs', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'inn', 'help': 'Реестр аккредитованных организаций, осуществляющих деятельность в области информационных технологий'},
               'mspreestrpp': {'epoint': '/mspreestrpp/mspreestrpp', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'inn', 'help': 'Реестр производственных субъектов малого и среднего предпринимательства - потенциальных поставщиков крупнейших заказчиков'},
               'eduorgsaccred': {'epoint': 'obrnadzor', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'EduOrgINN', 'help': 'Реестр организаций, осуществляющих образовательную деятельность по аккредитованным образовательным программам '},
               'fnsdebtam' : {'epoint' : '/fnsdebtam/fnsdebtam', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'org.inn', 'help' : 'Сведения о суммах недоимки и задолженности по пеням и штрафам'},
               'fnspaytax': {'epoint': '/fnspaytax/fnspaytax', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'org.inn', 'help': 'Сведения об уплаченных организацией в календарном году о налогах'},
               'fnsrevexp': {'epoint': '/fnsrevexp/fnsrevexp', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'org.inn', 'help': 'Сведения о суммах доходов и расходов по данным бухгалтерской (финансовой) отчетности организации за год'},
               'fnssnr' : {'epoint' : '/fnssnr/fnssnr', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'org.inn', 'help' : 'Сведения о специальных налоговых режимах, применяемых налогоплательщиками'},
               'fnssshr': {'epoint': '/fnsssshr/fnssshr', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'org.inn', 'help': 'Сведения о среднесписочной численности работников организации'},
               'fnstaxoffence': {'epoint': '/fnstaxoffence/fnstaxoffence', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'org.inn', 'help': 'Сведения о налоговых правонарушениях и мерах ответственности за их совершение'},
               'gosuslugi': {'epoint': '/gosuslugi/orgs', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'inn', 'help': 'Реестр всех организаций с портала госуслуг версии 3 (ЕПГУ v3) gosuslugi.ru'},
               'mosstatesupport': {'epoint': '/mos/statesupport', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'INN', 'help': 'Реестр субъектов малого и среднего предпринимательства – получателей поддержки г. Москвы'},
               'rknoperpd' : {'epoint' : '/rkn/operpd', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'inn', 'help' : 'Реестр операторов, осуществляющих обработку персональных данных'},
               'roszdravlic' : {'epoint' : '/roszdravnadzor/roszdravlic', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'inn', 'help' : 'Реестр лицензий Росздравнадзора'},
               'zhkhproviders' : {'epoint' : '/minsvyaz/zhkhproviders', 'prefix'  : LOCAL_DATACRAFTER_URL, 'qkey' : 'inn', 'help' : 'Реестр поставщиков информации ГИС ЖКХ с портала dom.gosuslugi.ru'},
               'rknresosmi' : {'epoint' : '/rkn/resosmi', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'founders.founder.inn', 'help' : 'Свидетельства о регистрации средства массовой информации'},
               'kosngocontest' : {'epoint' : '/kosmosru/dushorgs', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'inn', 'help' : 'Организации с портала Душевная Москва'},
               'mossmallcontr2016-supp': {'epoint' : '/mos/smallcontr2016', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'SupplierINN', 'help': 'Контракты малого объёма г. Москвы до 2016 года включительно (поставщики)'},
               'mossmallcontr2016-cust': {'epoint': '/mos/smallcontr2016', 'prefix': LOCAL_DATACRAFTER_URL,
                                           'qkey': 'PayerINN',
                                           'help': 'Контракты малого объёма г. Москвы до 2016 года включительно (заказчики)'},
                'naturalmon' : {'epoint' : '/fas/naturalmon', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'orginn',  'help' : 'Реестр субъектов естественных монополий'},
                'reestrpo' : {'epoint' : '/minsvyaz/reestrpo', 'prefix' : LOCAL_DATACRAFTER_URL, 'qkey' : 'inn', 'help': 'Единый реестр российских программ для электронных вычислительных машин и баз данных'},
                'rostruddecl': {'epoint': '/rostrud/declaration', 'prefix': LOCAL_DATACRAFTER_URL, 'qkey': 'inn',
                                'help': 'Реестр деклараций соответствия рабочих мест'},
                'trudorgs': {'epoint': '/trud/trudorgs', 'prefix': LOCAL_DATACRAFTER_URL,
                             'qkey': 'inn',
                             'help': 'Организации размещающие вакансии на портале ТрудВсем'},
                'trudvac': {'epoint': '/trud/trudvac', 'prefix': LOCAL_DATACRAFTER_URL,
                            'codetype': 'ogrn',
                            'qkey': 'organization',
                            'help': 'Вакансии на портале ТрудВсем'},
                'woodcontractlease': {'epoint': '/lesegais/contractlease', 'prefix': LOCAL_DATACRAFTER_URL,
                                      'qkey': 'inn',
                                      'help': 'Договоры аренды лесного участка'},
                'gisp_orgs': {'epoint': '/minpro/gisporgs', 'prefix': LOCAL_DATACRAFTER_URL, 'qkey': 'org_inn',
                              'help': 'Перечень производителей промышленной продукции, произведенной на территории Российской Федерации'},
                'fcisp_orgs': {'epoint': '/monstroy/fcisporgs', 'prefix': LOCAL_DATACRAFTER_URL, 'qkey': 'inn',
                               'help': 'Перечень юридических лиц и индивидуальных предпринимателей в части мониторинга цен на строительные ресурсы'},
                'berezka_supp': {'epoint': '/berezka/suppliers', 'prefix': LOCAL_DATACRAFTER_URL, 'qkey': 'inn',
                                 'help': 'Поставщики зарегистрированные в агрегаторе закупок Березка'},
                'berezka_cust': {'epoint': '/berezka/customers', 'prefix': LOCAL_DATACRAFTER_URL, 'qkey': 'inn',
                                 'help': 'Заказчики зарегистрированные в агрегаторе закупок Березка'},
                'reestrgk_cust': {'epoint': '/reestrgk/customers', 'prefix': LOCAL_DATACRAFTER_URL, 'qkey': 'inn',
                                 'help': 'Заказчики оп госконтрактам до 2013 года'},
                'reestrgk_supp': {'epoint': '/reestrgk/suppliers', 'prefix': LOCAL_DATACRAFTER_URL, 'qkey': 'inn',
                                 'help': 'Поставщики по госконтрактам до 2013 года'},
                'reestrgk_contracts': {'epoint': '/reestrgk/contracts', 'prefix': LOCAL_DATACRAFTER_URL, 'qkey': 'suppliers.inn',
                                  'help': 'Федеральные госконтракты с 2007 по 2013 годы'},

                }


def build_profile(orgcode, profiles, apikey=None, filepath=None):
    """Builds profile"""
    outname = orgcode + '.json'
    if os.path.exists(outname):
        f = open(outname, 'r')
        data = f.read()
        f.close()
        return json.loads(data)
    profile = {}
    if profiles == 'all':
        profiles = SOURCES_MAP.keys()
    for p in profiles:
        if 'method' in SOURCES_MAP[p]:
            data = SOURCES_MAP[p]['method'](orgcode, apikey=apikey)
        else:
            data = get_crafter_basic(SOURCES_MAP[p]['epoint'], SOURCES_MAP[p]['prefix'], SOURCES_MAP[p]['qkey'], orgcode, apikey=apikey)
        s = '-' if not data or len(data) == 0 else '+'
        print(s + ' ' + SOURCES_MAP[p]['help'])
        profile[p] = data
        if not os.path.exists(os.path.join(filepath, orgcode)):
            os.makedirs(os.path.join(filepath, orgcode))
        if data:
            outname = os.path.join(filepath, orgcode, p + '.json')
            f = open(outname, 'w', encoding='utf8')
            f.write(json.dumps(data, indent=4, ensure_ascii=False))
            f.close()
    return profile
