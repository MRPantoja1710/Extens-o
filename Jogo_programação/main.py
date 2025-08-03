import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty

class QuizScreen(Screen):
    pergunta = StringProperty("")
    alternativas = ListProperty([])

    def on_enter(self):
        with open("dados.json", encoding="utf-8") as f:
            self.questoes = json.load(f)
        self.indice = 0
        self.carregar_questao()

    def carregar_questao(self):
        q = self.questoes[self.indice]
        self.pergunta = q["pergunta"]
        self.alternativas = q["alternativas"]

    def responder(self, resposta):
        correta = self.questoes[self.indice]["correta"]
        if resposta == correta:
            self.ids.resultado.text = "✅ Resposta correta!"
        else:
            self.ids.resultado.text = f"❌ Resposta errada! Era: {correta}"

        self.indice += 1
        if self.indice < len(self.questoes):
            self.carregar_questao()
        else:
            self.ids.pergunta.text = "🎉 Fim do jogo!"
            self.ids.botoes.clear_widgets()

class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(QuizScreen(name="quiz"))
        return sm

if __name__ == '__main__':
    QuizApp().run()
