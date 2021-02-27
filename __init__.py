from mycroft import MycroftSkill, intent_file_handler


class MycroftFoxyTurtleRight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('right.turtle.foxy.mycroft.intent')
    def handle_right_turtle_foxy_mycroft(self, message):
        self.speak_dialog('right.turtle.foxy.mycroft')
        subprocess.call(["ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.5}}'"],shell=True)

def create_skill():
    return MycroftFoxyTurtleRight()

