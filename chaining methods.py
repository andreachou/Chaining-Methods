class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"User first name: {self.first_name}")
        print(f"User last name: {self.last_name}")
        print(f"User email: {self.email}")
        print(f"User age: {self.age}")
        print(f"Reward member: {self.is_rewards_member}")
        print(f"Gold card points: {self.gold_card_points}")
        return self # for chaining methond

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self

    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
            return self
        else:
            print("Your points are not enough")


# create new instance
user1 = User("Adam", "Smith", "adam.smith@gmail.com", "52")
user2 = User("Maria", "Anderson", "manderson@yahoo.com", "32")
user3 = User("Kevin", "Harris", "kevin.harris@hotmail.com", "21")


user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
