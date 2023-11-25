adj_fields = {'dictionary':'','non_past':'','non_past_pol':'','non_past_neg':'','non_past_pol_neg':'',
                'past':'','past_pol':'','past_neg':'','past_pol_neg':''}

verb_fields = {'dictionary':'','non_past':'','non_past_pol':'','non_past_neg':'','non_past_pol_neg':'',
                'past':'','past_pol':'','past_neg':'','past_pol_neg':'','te':''}

te_forms = {'って':['う','る','つ'],'んで':['む','ぶ','ぬ'],'いて':['く'],'いで':['ぐ'],'して':['す']}

def godan_inflections(keyword):
    def godan_te(keyword):
        if keyword == '行く':
            return '行って'
        elif keyword == '来る':
            return '来て'
        elif keyword == 'する':
            return 'して'
        for i in te_forms:
            if keyword[-1] in te_forms[i]:
                return keyword[:-1]+i
    def godan_stem(keyword):
        if keyword[-1] == 'ぶ' or keyword[-1] == 'つ':
            return keyword[:-1]+chr(ord(keyword[-1])-3)
        elif keyword[-1] in ['く','ぐ','す']:
            return keyword[:-1]+chr(ord(keyword[-1])-2)
        elif keyword[-1] in ['う','る','ぬ']:
            return keyword[:-1]+chr(ord(keyword[-1])-1)
    def godan_neg(keyword):
        if keyword[-1] == 'う':
            return keyword[:-1]+'わ'
        elif keyword[-1] == 'つ':
            return keyword[:-1]+'た'
        elif keyword[-1] == 'ぶ':
            return keyword[:-1]+chr(ord(keyword[-1])-6)
        elif keyword[-1] in ['く','ぐ','す']:
            return keyword[:-1]+chr(ord(keyword[-1])-4)
        elif keyword[-1] in ['る','ぬ']:
            return keyword[:-1]+chr(ord(keyword[-1])-2)
            
    verb_fields['dictionary'] = keyword
    verb_fields['non_past'] = keyword
    verb_fields['non_past_pol'] = godan_stem(keyword)+'ます'
    verb_fields['non_past_neg'] = godan_neg(keyword)+'ない'
    verb_fields['non_past_pol_neg'] = keyword[:-1]+chr(ord(keyword[-1])-1)+'ません'
    verb_fields['past'] = godan_te(keyword)[:-1]+chr(ord(godan_te(keyword)[-1])-7)
    verb_fields['past_pol'] = godan_stem(keyword)+'ました'
    verb_fields['past_neg'] = godan_neg(keyword)+'なかった'
    verb_fields['past_pol_neg'] = godan_stem(keyword)+'ませんでした'
    verb_fields['te'] = godan_te(keyword)
    return verb_fields

def ichidan_inflections(keyword):
    verb_fields['dictionary'] = keyword
    verb_fields['non_past'] = keyword
    verb_fields['non_past_pol'] = keyword[:-1]+'ます'
    verb_fields['non_past_neg'] = keyword[:-1]+'ない'
    verb_fields['non_past_pol_neg'] = keyword[:-1]+'ません'
    verb_fields['past'] = keyword[:-1]+'た'
    verb_fields['past_pol'] = keyword[:-1]+'ました'
    verb_fields['past_neg'] = keyword[:-1]+'なかった'
    verb_fields['past_pol_neg'] = keyword[:-1]+'ませんでした'
    verb_fields['te'] = keyword[:-1]+'て'
    return verb_fields

def i_inflections(keyword):
    adj_fields['dictionary'] = keyword
    adj_fields['non_past'] = keyword
    adj_fields['non_past_pol'] = keyword+'です'
    adj_fields['non_past_neg'] = keyword[:-1]+'くない'
    adj_fields['non_past_pol_neg'] = keyword[:-1]+'くないです'
    adj_fields['past'] = keyword[:-1]+'かった'
    adj_fields['past_pol'] = keyword[:-1]+'かったです'
    adj_fields['past_neg'] = keyword[:-1]+'くなかった'
    adj_fields['past_pol_neg'] = keyword[:-1]+'くなかったです'
    return adj_fields


def na_inflections(keyword):
    adj_fields['dictionary'] = keyword
    adj_fields['non_past'] = keyword+"だ"
    adj_fields['non_past_pol'] = keyword+'です'
    adj_fields['non_past_neg'] = keyword+'じゃない'
    adj_fields['non_past_pol_neg'] = keyword+'じゃないです'
    adj_fields['past'] = keyword+'だった'
    adj_fields['past_pol'] = keyword+'でした'
    adj_fields['past_neg'] = keyword+'じゃなかった'
    adj_fields['past_pol_neg'] = keyword+'じゃないです'
    return adj_fields


