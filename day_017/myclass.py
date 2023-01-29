class User:
    def __init__(self,userd_id, username):
        self.id = userd_id
        self.username = username.capitalize()
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "mithran")
user_2 = User("002", "kabilan")

user_1.follow(user_2)

print(f"User 1 following: {user_1.following}")
print(f"User 1 followers: {user_1.followers}")
print(f"User 2 following: {user_2.following}")
print(f"User 2 followers: {user_2.followers}")

 
