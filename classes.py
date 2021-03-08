from random import randint


class Event:
    """ Event Class:
    Each Event has 4 values:
        - name: the event name
        - description: the event description
        - answers: a list of tuples. Each tuple contains: the answer, the sentence to print if the answer has been
          chosen, and the points to add or remove if the answer has been chosen
    """
    def __init__(self, name: str, description: str, answers: list):
        self.name = name
        self.description = description
        self.answers = answers
        self.points = 10

    def __repr__(self):
        return self.name

    def run(self) -> int:
        """ runs the event asking the user to choose between answers and returning the points to add or
         remove based on chosen answer"""
        print(self.name)
        print(self.description)
        for num, answer in enumerate(self.answers):
            print(f'{num}. {answer[0]}')
        user_input = 'a'
        while not user_input.isdecimal() and not 0 <= int(user_input) < len(self.answers):
            user_input = input('\n -> ')
        print(self.answers[int(user_input)][2])
        return self.answers[int(user_input)][2]


class Quest:
    """ Quest Class
    Each Ques has 7 values:
        - name: the name of the quest
        - description: the description of the quest
        - events: a list of events of the quest
        - duration: the number of events
        - current_event: the currently running event if the quest is running default to -1
        - current_points: the points last before quest failure
        - stress: the ammount of stress to add if the quest fails
    """
    def __init__(self, name: str, description: str, stress: int):
        self.name = name
        self.description = description
        self.events = list()
        self.duration = 0
        self.current_event = -1
        self.points = 5
        self.stress = stress

    def __repr__(self):
        return self.name

    def add_event(self, event):
        """ adds an event to the quest and extends quest duration """
        self.events.append(event)
        self.duration += 1

    def run_event(self):
        """ runs the next event in queue and checks if the quest has failed or not returning a value based on that"""
        self.current_event += 1
        if self.current_event == len(self.events):
            self.current_event = -1
            return None
        else:
            self.points += self.events[self.current_event].run()
        if self.points < 0:
            return self.stress
        if self.current_event == self.duration:
            return -1  # reduces stress by one on completion
        return 0  # returns 0 if the quest is still running and the points are higher or equal to 0


class Person:
    """ Person class:
    Each person has 3 different values:
        - name: the name of the person and his relationship (es. Jeff Smith the police officer)
        - description: a short background to the person not needed to be long but longer makes it better
        - score: A score modifier that will be lately used to see how likely the person will be to help US
    """

    def __init__(self, name: str, description: str, score: int):
        self.name = name
        self.description = description
        self.score = score
        self.quest = list()
        self.old_quests = list()

    def __repr__(self):
        return self.name

    def get_quest(self):
        """ returns a random quest never done before """
        return self.quest[randint(0, len(self.quest)-1)]

    def add_quest(self, quest: Quest):
        """ adds a quest to the user quest list """
        self.quest.append(quest)
        return

    def quest_completed(self, quest: Quest):
        """ marks a quest as completed and moves it to the old_quests list """
        self.old_quests.append(quest)
        self.quest.remove(quest)
        return






