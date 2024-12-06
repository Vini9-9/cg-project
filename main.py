from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from panda3d_widget import Panda3DWidget

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.panda3d_widget = Panda3DWidget()
        self.add_widget(self.panda3d_widget)
        
        self.load_button = Button(text="Carregar Modelo", size_hint_y=None, height=50)
        self.load_button.bind(on_press=self.load_model)
        self.add_widget(self.load_button)

        self.status_label = Label(text="Status: Esperando", size_hint_y=None, height=30)
        self.add_widget(self.status_label)

        self.panda3d_widget.bind(on_model_loaded=self.update_status)

    def load_model(self, instance):
        self.panda3d_widget.load_model('models/panda')
        self.status_label.text = "Status: Carregando modelo..."

    def update_status(self, instance):
        self.status_label.text = "Status: Modelo carregado com sucesso"

class SimpleApp(App):
    def build(self):
        return MainLayout()

    def on_stop(self):
        self.root.panda3d_widget.on_exit()

if __name__ == '__main__':
    SimpleApp().run()