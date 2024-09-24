class MyHashMap:

    #time complexity = o(1)
    #space complexity = o(n)
    #used a fixed size list to store key value pairs. Put stores a key value pair based on the key. 
    #get retrieves a value based on the key or returns -1 if value doesn't exsit. remove deletes a value by setting the value to none for a key.
    def __init__(self):
        self.data = [None] * 10000000

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        value = self.data[key]
        if value != None:
            return value
        else:
            return -1

    def remove(self, key: int) -> None:
        self.data[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
