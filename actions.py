# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import random
from rasa_sdk import Action
from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

time_list = ['明天下午2点','明天下午3点','明天下午4点']

class ActionTimeConfirm(Action):


    def name(self) -> Text:
        return "action_time_confirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_time_confirm",
        time=tracker.get_slot('time'),
        )

        return []

class ActionTimeNumberConfirm(Action):


    def name(self) -> Text:
        return "action_time_number_confirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_time_confirm",
        time=tracker.get_slot('time'),
        )

        time_dict = {"一":1,'1':1,'二':2,'2':2,'三':3,'3':3}
        time_number = tracker.get_slot('time_number')
        dispatcher.utter_message(template="utter_time_confirm",
        time=time_list[time_dict[time_number]],
        )

        return []
