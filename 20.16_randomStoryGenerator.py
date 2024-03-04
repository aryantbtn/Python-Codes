# Story generator with Python Created by Aryan
# Our task is to generate a random story every time the user runs the program. I will first store the parts of the stories in different lists, then the Random module can be used to select the random parts of the story stored in the different lists:
'''import random

when_story = ['A few years ago', 'Yesterday', 'Last night', 'On 15th August', 'Once upon a time']
who_story = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat', 'a dolphin']
name_story = ['Arayn', 'Hardik', 'Keshav', 'Abhishek', 'Gaurav', 'Aman Yadav', 'Amitabh Bachchan']
residence = ['India', 'Germany', 'Italy', 'France', 'Paris', 'London', 'America', 'Russia']
went_to = ['cinema', 'university', 'semister', 'school', 'hotel', 'mall', 'hostel', 'venue']
happened = ['made a lot of friends', 'eats a pizza', 'found a key', 'wrotes a book', 'solve the puzzle', 'get puzzled to solve the mystery', 'be patient and calm']
post_alloted = ['Sr. Assistant Professor', 'Jr. Developer', 'Writer', 'Film Maker', 'Student', 'Managing Director', 'Dean Faculty', 'Lecturer']
print(type(when_story))

print(random.choice(when_story)+ ', ' + random.choice(who_story) + ' named ' + random.choice(name_story) + ' who live in '+ random.choice(residence) + ' currently posted as ' + random.choice(post_alloted) + ' went to the ' + random.choice(went_to) + ' and ' + random.choice(happened))'''