from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

from home_page import HomePage

# Resize the window
Window.size = (350, 600)


class FacebookApp(MDApp):
    def build(self):
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file("home_page.kv")
        Builder.load_file("components/avatar_image.kv")
        Builder.load_file("components/three_buttons.kv")
        Builder.load_file("components/online_friends.kv")
        Builder.load_file("components/story_widget.kv")
        Builder.load_file("components/posts.kv")

    def on_start(self):
        self.root.dispatch("on_enter")


if __name__ == '__main__':
    FacebookApp().run()
