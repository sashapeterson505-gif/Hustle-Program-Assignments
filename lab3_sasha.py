#  Sasha Peterson | Lab 3 | Intro to Python

# Ticket 1

# PREDICT: It will be 17 characters 

username = "sashapeterson_123"
print(len(username))

# RESULT: 17 

# Ticket 2

# PREDICT: It will be "s" and "3"

username = "sashapeterson_123"
print(username[0])
print(username[-1])

# RESULT: indexing starts at 0, so if a string has 17 characters, the last character is at index -1, which is "3"


# Ticket 3

# PREDICT: It will print "Welcome to Loop, @sashapeterson_123!" twice and look identical

yourhandle = "@sashapeterson_123 " 
#Method 1: using concatenation
print("Welcome to Loop, " + yourhandle + "!") # Replace yourhandle with the actual variable name 
#Method 2: using an f-string
print(f"Welcome to Loop, {yourhandle}!")

# RESULT: i think the f string is easier because concatenation is less readable and confusing if not paying attention. 

# Ticket 4 

# PREDICT: i think running the broken line will cause a TypeError

# original username 
username = "sashapeterson_123"
# attempting to change the first character of the username (this will cause an error)
# username[0] = "S"  # This will raise a TypeError
username = "Xashapeterson_123" #this line breaks on purpose
# the right way to make the whole username print in capital letters
uppercase_username = username.upper()
print(uppercase_username)

# RESULT: i think immutable means the strung cant change after i create it


# Ticket 5

# PREDICT: the number that prints will be 3

feed = ["Hello world!", "How are you?", "I'm doing great!"]
print(len(feed))
print(feed[0])
print(feed[1])
print(feed[2])

# RESULT: the index i used to get the first post is 0, the second is 1, and the third is 2.

# Ticket 6

# PREDICT: the new 4th post will have index 3 

feed = ["Hello world!", "How are you?", "I'm doing great!"] #same feed as before
feed.append("New post!")
print(feed)

# RESULT: when i use .append(), the new post is added to the end of the list, so it gets index 3.

# Ticket 7 

# PREDICT: the list will be sorted alphabetically and "Hello world!" will be removed 

feed = ["Hello world!", "How are you?", "I'm doing great!", "New post!"] #same feed as before
feed.pop(0) # remove the oldest post (at index 0)
feed.sort() # sort the remaining posts alphabetically
print(feed)

# RESULT: the .pop method removes the post wherever u want to remove it from the list. the .sort method then arranges the remaining posts alphabetically.

# Ticket 8

# PREDICT: it will print 1234. i'm not really sure what profile[0] would do

profile = {
    "username": "sashapeterson_123",
    "followers": 1234,
    "verified": True
}
print(profile["followers"])

# RESULT: dictonaries use key names because it allows them to store and retrive data based on identifiers.

# Ticket 9

# PREDICT: when the key is missing, .get("age") will print nothing i think 

profile = {
    "username": "sashapeterson_123",
    "followers": 1234,
    "verified": True,
    "following": 19 
}
# update the follower value to 50
profile["follower"] = profile["followers"] + 50
# add a new key called "bio" 
profile["bio"] = "I'm a Python developer!"
# print the whole profile
print(profile)
# use .get() to look up a key that doesnt exist 
age_value = profile.get("age")
print(age_value)

# RESULT: .get() wont  crash the code if a key is missing 

# Ticket 10

# PREDICT: the code will print @sashapeterson_123  has 1234 followers and 3 posts. top post: hi there!

profile = {
    "username": "sashapeterson_123",
    "followers": 1234,
    "verified": True,
    "following": 69     
}
feed = [
    {"caption": "Hi there!", "likes": 10},
    {"caption": "Another post!", "likes": 20},
    {"caption": "Yet another post!", "likes": 30}
]
# create the profile summary using an f-string 
profile_summary = f"@{profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]['caption']}"

print(profile_summary)

# RESULT1: dictornary: profile (used for username and followers)
# RESULT2: list: feed (used for post count and the first post caption)