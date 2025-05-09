"""
Hotel Management


The purpose of this program is to make sure you have an understanding of the topics you learned in Python Apprentice.  This is going to be your 1st program you write all by yourself, imagine someone hired you to create a hotel management program.


Getting Started:

Under projects create a new file and name it hotel_management.py

Create a docstring (it's the triple quotes “””  stuff goes inside “””)

Take some time to organize your thoughts on how the program will be laid out and what you will need (functions, imports, loops, etc.)

Write down your thoughts as a list or instructions to yourself inside the docstring

Add your imports (Tkinter or whatever you need)

Code away, make sure to keep it organized so you know where things are and what they do.

Separate different functionalities into their own functions.



Requirements:

Should run in 1 While Loop

Everything except a few top level variables (aka Global) should be in functions

The functions should, mostly, return something

For instance if I had a function called add, it should return the sum rather than just doing the operation or printing it.

Remember, with Python you can set a variable to a return value of a function, so:  my_age = add(10, 5)

Add arguments to your functions as needed

Must contain and iterate over these data structures:

List

Dictionary

Tuple


Functionality Requirements:

Must be interactive, either in the command line with print() and input() or with Tkinter

Check guests in and out

Charge guests for their room(s)

Multiple room check in

Multiple Night Check in

Add 1 new feature of your choice

Ex.  Upgrade room, room service, spa package, etc.  



Have Fun!!! 
"""
"""
1 while loop? (while hotel opened?)
Input to check in guests and put in rooms (append into dictionary?)
Be able to delete from dic (func)
Rooms have to be filled. (If room is used, take out of a list of rooms?) + (charge guest for each room)
If people have more than one room do i put them in a special list?
People arranged by names
Rooms have to have some input into how many nights they are booked (Charge accordingly)
Must have  timer when guests are done with their booking (Do i make an option for them to ADD nights when they are done?)
Add extra thing AFTER you finish coding the the main thing.
"""
hotel_opened = True
checked_in_rooms = {}
rooms = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def check_in(checked_in_rooms, roomnum, roomname):
        checked_in_rooms[roomnum] = roomname


while hotel_opened:
    
    
    check_in(checked_in_rooms, int(input("Which room number would you like?   ")), input("And what name is the room for?   "))
    for room in rooms:
        if room in checked_in_rooms.keys():
            print(f"Room {room} is checked in")
        else:
            print(f"Room {room} is available") 
    

    hotel_opened = False    