import lark
from pathlib import Path
from pprint import pprint
from collections import defaultdict

# MAKE SURE THAT THERE IS A NEW LINE AT THE BOTTOM OF THE TEXT FILE

parser = lark.Lark(r"""
start: (term)*
term: key "=" value "\n"
key: CNAME | SIGNED_NUMBER
value: CNAME | SIGNED_NUMBER | ESCAPED_STRING | map
map: "{" (term)* "}"
%import common.CNAME
%import common.ESCAPED_STRING
%import common.SIGNED_NUMBER
%import common.WS
%ignore WS
%ignore /#.*/
""")

class TreeTransformer(lark.Transformer):
    def start(self, items):
        return dict(items)

    def term(self, items):
        return (items[0], items[1])

    def CNAME(self, item):
        return item.value

    def SIGNED_NUMBER(self, item):
        return int(item.value)

    def ESCAPED_STRING(self, item):
        return item.value[1:-1]

    def map(self, items):
        return dict(items)

    def key(self, item):
        return item[0]

    def value(self, item):
        return item[0]

data = Path("aGoTTeam and AAR winners.txt").read_text()
tree = parser.parse(data)
res = TreeTransformer().transform(tree)
pprint(res)

names_by_culture = defaultdict(list)
for info in res.values():
    names_by_culture[info["culture"]].append(info["name"])
pprint(dict(names_by_culture))