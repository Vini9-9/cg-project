from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

class DadosPessoaisForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Nome
        self.add_widget(Label(text='Nome:'))
        self.nome_input = TextInput(multiline=False)
        self.add_widget(self.nome_input)

        # Idade
        self.add_widget(Label(text='Idade:'))
        self.idade_input = TextInput(multiline=False, input_filter='int')
        self.add_widget(self.idade_input)

        # Massa
        self.add_widget(Label(text='Massa (kg):'))
        self.massa_input = TextInput(multiline=False, input_filter='float')
        self.add_widget(self.massa_input)

        # Sexo
        self.add_widget(Label(text='Sexo:'))
        self.sexo_spinner = Spinner(
            text='Selecione',
            values=('Masculino', 'Feminino', 'Outro')
        )
        self.add_widget(self.sexo_spinner)

        # Etnia
        self.add_widget(Label(text='Etnia:'))
        self.etnia_input = TextInput(multiline=False)
        self.add_widget(self.etnia_input)

        # Botão de envio
        self.submit_button = Button(text='Enviar')
        self.submit_button.bind(on_press=self.submit_data)
        self.add_widget(self.submit_button)

    def submit_data(self, instance):
        print(f"Nome: {self.nome_input.text}")
        print(f"Idade: {self.idade_input.text}")
        print(f"Massa: {self.massa_input.text}")
        print(f"Sexo: {self.sexo_spinner.text}")
        print(f"Etnia: {self.etnia_input.text}")

class DadosPessoaisApp(App):
    def build(self):
        return DadosPessoaisForm()

if __name__ == '__main__':
    DadosPessoaisApp().run()