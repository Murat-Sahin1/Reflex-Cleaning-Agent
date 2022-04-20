# Reflex agents, could be called as the most primitive agent of all the agents in AI. Basically, Reflex agents don't take their past percepts into the account. They act immediate by the rules and jurisdictions of their maker, without thinking what will be the result of their acts.
#
Problem = We have 2 rooms, these rooms could be cleaned or could be traveled, but we can only do one action at a time. Let's create a solution with the reflex-agent AI approach.
#
Also keep in mind that this reflex agent could only perceive its room and if it is clean or not. This means you can only use the information that the agent has. Nothing more.

# Pseudo Code of the maintary action:
#   function Reflex-Cleaning-Agent([location, state]) returns action
#       if state = dirty return clean
#       else if location = A then return Go-Right
#       else if location = B then return Go-Left

