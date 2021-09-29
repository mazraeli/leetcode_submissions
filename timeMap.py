import copy as cp

class TimeMap:

    def __init__(self):
        
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if (key in self.map):
            self.map[key][timestamp] = value
        else:
            tdict = {}
            tdict[timestamp] = value
            self.map[key] = cp.deepcopy(tdict)
            tdict.clear()

    def get(self, key: str, timestamp: int) -> str:
        
        if not(key in self.map):
            return ""

        tdict = self.map[key]
        timestamp_list = list(tdict.keys())
        timestamp_list.sort()

        i = 0
        for time in timestamp_list:
            if (time == timestamp):
                return self.map[key][timestamp_list[i]]
            if (i == 0 and time > timestamp):
                return ""
            if (time > timestamp):
                return self.map[key][timestamp_list[i - 1]]
            i += 1

        return self.map[key][timestamp_list[i - 1]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
