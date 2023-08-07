class Singleton:
    __instance = None   # private variable to hold the instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton class cannot be instantiated more than once")
        else:
            Singleton.__instance = self
            self.value = "This is a singleton instance."

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance


if __name__ == "__main__":
    s1 = Singleton.getInstance()
    s2 = Singleton.getInstance()
    print(s1 == s2) # Output: True
    print(s1.value) # Output: This is a singleton instance.
