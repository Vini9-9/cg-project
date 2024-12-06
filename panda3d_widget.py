from kivy.uix.widget import Widget
from kivy.clock import Clock
import subprocess
import sys

import threading

class Panda3DWidget(Widget):
    __events__ = ('on_model_loaded',)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.panda_process = subprocess.Popen(
            [sys.executable, "panda3d_renderer.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        self.output_thread = threading.Thread(target=self.read_output, daemon=True)
        self.output_thread.start()

    def read_output(self):
        for line in self.panda_process.stdout:
            if line.strip() == "MODEL_LOADED":
                Clock.schedule_once(lambda dt: self.dispatch('on_model_loaded'))

    def load_model(self, model_path):
        self.panda_process.stdin.write(f"LOAD {model_path}\n")
        self.panda_process.stdin.flush()

    def on_model_loaded(self):
        pass  # Este método será chamado quando o modelo for carregado

    def on_exit(self):
        if self.panda_process:
            self.panda_process.stdin.write("EXIT\n")
            self.panda_process.stdin.flush()
            self.panda_process.wait()
            self.panda_process = None