class Instagram:
    def __init__(self, name, id):
        self.person_name = name
        self.person_id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = Instagram("A", 1)
user_2 = Instagram("B", 2)

user_1.follow(user_2)   # method call
print(user_1.followers)
print(user_1.following)
print("---------------")
print(user_2.followers)
print(user_2.following)


