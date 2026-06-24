#  Sasha Peterson | Lab 3 | Intro to Python

# Ticket 1
username = "sashapeterson_123"
print(len(username))

# PREDICT: It will be 17 characters 
# RESULT: 17 

# Ticket 2
username = "sashapeterson_123"
print(username[0])
print(username[-1])

# PREDICT: It will be "s" and "3"
# RESULT: indexing starts at 0, so if a string has 17 characters, the last character is at index -1, which is "3"

# Ticket 3
yourhandle = "@sashapeterson_123 " 
#Method 1: using concatenation
print("Welcome to Loop, " + yourhandle + "!") # Replace yourhandle with the actual variable name 
#Method 2: using an f-string
print(f"Welcome to Loop, {yourhandle}!")

# PREDICT: It will print "Welcome to Loop, @sashapeterson_123!" twice and look identical
# RESULT: i think the f string is easier because concatenation is less readable and confusing if not paying attention. 

# Ticket 4 

# Ticket 5
feed = ["Hello world!", "How are you?", "I'm doing great!"]
print(len(feed))
print(feed[0])
print(feed[1])
print(feed[2])

# PREDICT: the number that prints will be 3
# RESULT: the index i used to get the first post is 0, the second is 1, and the third is 2.

# Ticket 6
feed = ["Hello world!", "How are you?", "I'm doing great!"] #same feed as before
feed.append("New post!")
print(feed)

# PREDICT: the new 4th post will have index 3 
# RESULT: when i use .append(), the new post is added to the end of the list, so it gets index 3.

# Ticket 7 
feed = ["Hello world!", "How are you?", "I'm doing great!", "New post!"] #same feed as before
feed.pop(0) # remove the oldest post (at index 0)
feed.sort() # sort the remaining posts alphabetically
print(feed)

# PREDICT: the list will be sorted alphabetically and "Hello world!" will be removed 
# RESULT: the .pop method removes the post wherever u want to remove it from the list. the .sort method then arranges the remaining posts alphabetically.

# Ticket 8
profile = {
    "username": "sashapeterson_123",
    "followers": 1234,
    "verified": True
}
print(profile["followers"])

# PREDICT: it will print 1234. i'm not really sure what profile[0] would do
# RESULT: dictonaries use key names because it allows them to store and retrive data based on identifiers.

# Ticket 9
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

# PREDICT: when the key is missing, .get("age") will print nothing i think 
# RESULT: .get() wont  crash the code if a key is missing 

# Ticket 10
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

# PREDICT: the code will print @sashapeterson_123  has 1234 followers and 3 posts. top post: hi there!
# RESULT1: dictornary: profile (used for username and followers)
# RESULT2: list: feed (used for post count and the first post caption)