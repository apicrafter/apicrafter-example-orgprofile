import csv

def _calc_share(adict, total):
    for k, v in adict.items():
        adict[k]['share'] = v['amount'] * 100.0 / total
    return adict


def dsort(adict, key='share'):
    edges = list(adict.items())
    edges.sort(key=lambda x: x[1][key], reverse=True)
    return edges

KEYMAP = [[1000000000, u'миллиард', u'миллиарда', u'миллиардов'],
        [1000000, u'миллион', u'миллиона', u'миллионов'],
        [1000, u'тысяча', u'тысячи', u'тысяч'],
        [1, u'рубль', u'рубля', u'рублей'],
            ]

KEYMAP_SOKR = [[1000000000, u'млрд.', u'млрд.', u'млрд.'],
        [1000000, u'млн.', u'млн.', u'млн.'],
        [1000, u'тыс.', u'тыс.', u'тыс.'],
        [1, u'рубль', u'рубля', u'рублей'],
            ]

KEYMAP_POSTFIX = [u'рубль', u'рубля', u'рублей']

def num2txt(i, skiplevel=1):
    parts = []
    if skiplevel > 0:
        amap = KEYMAP[:-skiplevel]
    else:
        amap = KEYMAP
    for mapper in amap:
        n = int((int(i) / mapper[0]) % 1000)
#        print(n)
        if n < 1:
            if mapper[0] == 1: parts.append(mapper[3])
            continue
        p = n % 10
        if p == 1:
            parts.append('%d %s' % (n, mapper[1]))
        elif p in [2, 3, 4]:
            parts.append('%d %s' % (n, mapper[2]))
        else:
            parts.append('%d %s' % (n, mapper[3]))
#    if len(parts) == 0:
#        parts.append('%d' % i)
    if skiplevel > 0:
        parts.append(u'рублей')
    return ' '.join(parts)
