from string import Template

INSTRUCTION_PROMPT = Template("""Your role is the game master in a game similar to D&D.
The player will write what they want to do or what they want to learn from you. Your task is to write to the player about what happened when they took action.
You have a script to guide you. You can't reveal the script to the player. The player can only interact with items present in the room.
To find out if an item is in the room, you need to use the item search function. (If the player tries to interact with an item that doesn't exist or make an action that their character can't make given the context, they need to be informed of this).""")

BASE_SCENARIO_PROMPT = Template("""1. Game Start:
The player wakes up in a dimly lit room with no memory of how they got there. All windows are barred, and there's only one door, which is locked.
2. First Puzzle: The Clock:

A grandfather clock in the room is missing its minute hand.
Searching the room, the player finds the minute hand hidden under a loose floorboard.
Setting the clock to a specific time (hinted by a calendar date in the room) opens a drawer in the clock that contains a small key.
3. Second Puzzle: The Bookshelf:

The key from the clock fits a small box on the bookshelf.
Inside the box, there's a riddle that hints at a specific book on the shelf.
Pulling that book opens a secret compartment with a metal rod.
4. Third Puzzle: The Painting:

There's a large painting on the wall of a landscape. Part of the scenery (like a tree) is protruding slightly.
Using the metal rod, the player can press the protruding part, which reveals a safe behind the painting.
5. Fourth Puzzle: The Safe:

The safe has a combination lock.
Clues scattered around the room (like numbers on the spines of specific books) give the combination.
Inside the safe, there's a key to exit.
""")

BASE_SETUP = Template(
    """The player wakes up in a dimly lit room with no memory of how they got there. All windows are barred, and there's only one door, which is locked.""")

CLASSIFY_USER_REQUEST_PROMPT = Template("""Classify user's intention "$user_request" as "Ask", "Doing" or "Not under your control".
"Ask" means that user don't want to interact with environment. User asks for some info they have already received from environment. "Ask" should be addressed to game-master
"Doing" means that user wants to interact with environment and modify it. It may be changing location, changing items position and giving something to environment (information, items, physical moves). It should be done by user's character.
"Not under your control" means that user want to do something that is under their control - they are not an object of this request. User may control ONLY their thoughts, decisions, acts, moves. User can't control their feeling and things outside/beside their body. User can't control other characters unless another is mentioned

Example 1
user_request: I say my speech
Output: {"class": "Doing"}

Example 2
user_request: James tells me about his job
Output: {"class": "Not under your control"}

Example 3
user_request: What's the name of my companion?
Output: {"class": "Ask"}

Example 4
user_request: I try to fly with my arms?
Output: {"class": "Doing"}

Output as JSON: {"class": "<your text>"}
""")

DESCRIBE_NOT_CONTOLLED_ACTION_PROMPT = Template("""User's request "$user_request" cannot be performed because it's under their control.
Describe in one-two sentences that it doesn't modify environment and doesn't make sense.

Example 1
user_request: Emily started talking with him
Answer: You've tried but you can't control Emily to force her to talk with him

Example 2
user_request: The gate has opened
Answer: There is no way to open the gate without your moves

Example 3
user_request: I found the key on the floor
Answer: You haven't found any keys at first look.

Example 4:
user_request: I enter into the room and portraits started talking to me.
Answer: You enter into the room. In your mind portraits are talking to you but you are not sure if they are real. 
""")
