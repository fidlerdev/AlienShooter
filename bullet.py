from gamesprite import *

class Bullet(GameSprite):
    # Вызывается в каждом кадре
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()