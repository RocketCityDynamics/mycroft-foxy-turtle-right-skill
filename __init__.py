from mycroft import MycroftSkill, intent_file_handler


class MycroftFoxyTurtleRight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('right.turtle.foxy.mycroft.intent')
    def handle_right_turtle_foxy_mycroft(self, message):
        self.speak_dialog('right.turtle.foxy.mycroft')


def create_skill():
    return MycroftFoxyTurtleRight()

