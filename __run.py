import timeMap

inst = timeMap.TimeMap()


# inst.set("love","high",10)
# inst.set("love","low",20)
# print(inst.get("love",5))
# print(inst.get("love",10))
# print(inst.get("love",15))
# print(inst.get("love",20))
# print(inst.get("love",25))


inst.set("foo","bar",1)
print(inst.get("foo",1))
print(inst.get("foo",3))
inst.set("foo","bar2",4)
print(inst.get("foo",4))
print(inst.get("foo",5))
