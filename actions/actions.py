# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_query_camera"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        zoneName = tracker.get_slot("zoneName")
        location = tracker.get_slot("location")
        
        if zoneName == None :
            dispatcher.utter_message(text="请指定校区!")
            return [SlotSet("zoneName",None),SlotSet("location",None)]
        
        if location == None :
            dispatcher.utter_message(text="{'zoneName':'"+zoneName+"'}")
            return [SlotSet("zoneName",None),SlotSet("location",None)]

        dispatcher.utter_message(text="{'zoneName':'"+zoneName+"','location':'"+location+"'}")

        #在最后清空slot中的值
        return [SlotSet("zoneName",None),SlotSet("location",None)]
