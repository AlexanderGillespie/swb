#!/usr/bin/python3

import json
import playsound as ps
import time

class Prompter():
    def __init__(self):
        self._questions = [
            "In most ways my life is close to ideal",
            "The conditions of my life are excellent",
            "I am satisfied with my life",
            "So far I have gotten the important things I want in life",
            "If I could live my life over, I would change almost nothing"
        ]
        self._swb_score = 0

    def launch_survey(self):
        # Send a notification sound
        ps.playsound("notification.mp3")

        # Prompt the user to interact with the program
        print("Let's take a minute to measure your subjective well-being.")
        input("Press [Enter] when you're ready to continue.")

        # Print the survey start time and instructions
        print("Time is [{}]".format(time.strftime('%d-%b-%Y %I:%M %p')))
        print("Please answer the following questions.\n"
                "Enter 1 for strongly disagree.\n"
                "Enter 6 for strongly agree.")

        self._administer_survey()

    def fix_swb_score(self):
        self._swb_score = self._swb_score / len(self._questions)

    def send_to_json(self):
        # If you let the json file get big enough then this will /eventually/ 
        # run out of memory. That being said, if you stick with this long 
        # enough to run into that issue then idk my friend.
        with open("swb-log.json") as f:
            json_data = json.loads(f.read())
        
        # TODO: Make this print to json


    def _administer_survey(self):
        for question in self._questions:
            answer = self._ask_question(question)
            self._swb_score += answer
    
    def _ask_question(self, question):
        try:
            # This runs as long as answer on the following line is a number
            answer = int(input("{}: ".format(question)))
            if answer >= 1 and answer <= 6:
                return answer
            else:
                self._invalid_entry()
                return self._ask_question(question)
        except:
            # This runs if answer is not a number
            self._invalid_entry()
            return self._ask_question(question)

    def _invalid_entry(self):
        print("Please enter '1', '2', '3', '4', '5', or '6'")


def main():
    prompter = Prompter()
    prompter.launch_survey()
    prompter.fix_swb_score()
    prompter.send_to_json()

if __name__ == "__main__":
    main()