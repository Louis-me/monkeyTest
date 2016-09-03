__author__ = 'Administrator'
from schematics.models import Model
from schematics.types import StringType,IntType
from schematics.types.compound import ListType
import json
class matplo(Model):
    cpu = ListType(IntType)
    men = ListType(IntType)
    title = ListType(StringType)
    locator = IntType()
# m = matplo()
# m.data = [[111],[3333]]
# m.title = ["11","222"]
# m.locator = 2
# m.title.append("3333")
# print(json.dumps(m.to_primitive()))

