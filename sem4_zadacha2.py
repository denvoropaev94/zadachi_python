# transleterate = \
#   {'а': 'a','б': 'b','в': 'v','г' : 'g','д' : 'd','е' : 'e','ж' : 'zh','з' : 'z','и' : 'i',
#   'й' : 'y','к' : 'k','л' : 'l','м' : 'm','н' : 'n','о' :'o','п' : 'p','р' : 'r','с' : 's',
#   'т' : 't','у' : 'u','ф' : 'f','х' : 'kh','ц' : 'ts','ч' : 'ch','ш' : 'sh','щ' : 'shch',
#   'ь' : '\'','ы' :'y','ъ' : '','э' : 'e','ю' : 'yu','я' : 'ya'}
# text = input('input: ')

# for i in text:
#     print(transleterate[i], end = "")

t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = 'Переводим этот текст, сейчас!'
print(title.lower())

slug = ""
for s in title.lower():
    # print(ord('а'),ord(s))
    if "а" <= s <= "я":
        slug += t[ord(s) - ord('а')]
    else:
        slug += s



print(slug)