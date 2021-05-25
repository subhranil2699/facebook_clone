from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty


class Post(MDCard):
    name = StringProperty()
    avatar = StringProperty()
    post = StringProperty()

    likes = StringProperty()
    comments = StringProperty()
    caption = StringProperty()
    updated_ago = StringProperty()