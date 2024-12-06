import sys
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
import pickle

loadPrcFileData("", """
window-type offscreen
audio-library-name null
""")

class Panda3DRenderer(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.disableMouse()
        self.cam.setPos(0, -10, 0)
        self.cam.lookAt(0, 0, 0)
        self.model = None

    def load_model(self, model_path):
        if self.model:
            self.model.removeNode()
        self.model = self.loader.loadModel(model_path)
        if self.model:
            self.model.reparentTo(self.render)
            self.model.setScale(1)
            self.model.setPos(0, 0, 0)
            print("MODEL_LOADED")
            sys.stdout.flush()

    def run(self):
        while True:
            command = sys.stdin.readline().strip()
            if command.startswith("LOAD "):
                model_path = command[5:]
                self.load_model(model_path)
            elif command == "EXIT":
                break
            self.taskMgr.step()

if __name__ == "__main__":
    renderer = Panda3DRenderer()
    renderer.run()