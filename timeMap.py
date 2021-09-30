class LinkedList:
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value
        self.next = None


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.database = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        node = LinkedList(timestamp, value)
        node.next = self.database.get(key)
        self.database[key] = node
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.database:
            return ""
        
        head = self.database[key]
        while head:
            if timestamp >= head.timestamp:
                return head.value
            head = head.next

        return ""