from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty


class StoryWidget(MDRelativeLayout):
    name = StringProperty()
    avatar = StringProperty()
    image = StringProperty()
