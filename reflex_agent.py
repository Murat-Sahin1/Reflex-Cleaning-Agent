# Reflex agents, could be called as the most primitive agent of all the agents in AI. Basically, Reflex agents don't
# take their past percepts into the account. They act immediate by the rules and jurisdictions of their maker,
# without thinking what will be the result of their acts.
#
# Problem = We have 2 rooms, these rooms could be cleaned or could be traveled, but we can only do one action
# at a time. Let's create a solution with the reflex-agent AI approach
# Also keep in mind that this reflex agent could only perceive its room and if it is clean or not. This means
# you can only use the information that the agent has. Nothing more.
#
# Pseudo Code:
#   function Reflex-Cleaning-Agent([location, state]) returns action
#       if state = dirty return clean
#       else if location = A then return Go-Right
#       else if location = B then return Go-Left


class Reflex_Cleaning_Agent:

    def __init__(self, _location, _enviroment):
        self.my_enviroment = _enviroment
        self.location = _location
        self.room_a_is_dirty = True
        self.room_b_is_dirty = True
        # Initilizing my state with the data of my location.
        # My state is going to be something like this [-the room I'm in-, -clean or dirty-].
        # Remember, the state is a representation of my environment due to my perceptions.
        self.my_state = []
        self.initialize(self.location)

    def Run(self):
        if self.my_state[1] == 'dirty':
            self.clean(self.location)
        elif self.location == "room-A":
            self.go_right_room()
        elif self.location == "room-B":
            self.go_left_room()

    def clean(self, _location):
        if _location == 'room-A':
            self.my_enviroment[0] = [str(_location), 'clean']
            self.room_a_is_dirty = False
            self.my_state = [str(_location), 'clean']
        if _location == 'room-B':
            self.my_enviroment[1] = [str(_location), 'clean']
            self.room_b_is_dirty = False
            self.my_state = [str(_location), 'clean']
        print(_location, "is cleaned.")

    def go_right_room(self):
        self.room_a_is_dirty = False  # If we traveled to the room-b, then the room-a is clean
        self.location = self.my_enviroment[1][0]  # 'room-B'
        self.my_state = self.my_enviroment[1]
        print("Room A was clean, therefore robot went to the right room.")

    def go_left_room(self):
        self.room_b_is_dirty = False  # If we traveled to the room-a, then the room-b is clean
        self.location = self.my_enviroment[0][0]  # 'room-A'
        self.my_state = self.my_enviroment[0]
        print("Room B was clean, therefore robot went to the left room.")

    def initialize(self, _location):
        for room in self.my_enviroment:
            if room[0] == _location:
                self.my_state = room
        print("Robot is in the", self.my_state[0])

    def Run_Until_Everywhere_Is_Clean(self):
        while self.room_a_is_dirty or self.room_b_is_dirty:
            self.Run()
        print("Every room is clean.")

    def Return_Enviroment(self):
        return self.my_enviroment


class main:
    def __init__(self):
        # Let's do a test run on our reflex cleaning agent
        # You can change the dirty or clean values, or initial location of the agent however you like.
        my_enviroment = [['room-A', 'dirty'], ['room-B', 'clean']]
        location = 'room-A'
        reflex_agent = Reflex_Cleaning_Agent(location, my_enviroment)

        # TEST RUNNING FOR REFLEX_AGENT
        reflex_agent.Run_Until_Everywhere_Is_Clean()


main()
