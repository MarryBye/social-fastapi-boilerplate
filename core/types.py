from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class Privacy(str, Enum):
    public = "public"
    private = "private"
    friends_only = "friends_only"