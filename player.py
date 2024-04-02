from gamesprite import *
from bullet import Bullet

class Player(GameSprite):
    '''
    Класс спрайта игрока
    '''
    bullets = sprite.Group()
    # Время последнего выстрела
    last_bullet_time: int = time.get_ticks()
    # Минимальное время ожидания перед выстрелом
    bullet_delay: int = 400
   
    # Создаем звук выстрела
    mixer.init()
    fire_sound = mixer.Sound('fire.ogg')


    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT]:
            self.rect.x += self.speed
        if key_pressed[K_SPACE]:
            self.fire()
        # Левый край
        if self.rect.right < 0:
            self.rect.x = self.window.get_width() - 10
        if self.rect.x >= self.window.get_width():
            self.rect.x = -50

    def fire(self):
        '''
        Метод стрельбы игрока
        '''
        # Сейчас
        now = time.get_ticks()

        if now - self.last_bullet_time >= self.bullet_delay:
            self.bullets.add(
                Bullet('bullet.png', 
                    self.rect.x,
                    self.rect.top,
                    6,
                    self.window)
            )
            # Фиксируем время последнего выстрел
            self.last_bullet_time = now
            self.fire_sound.play()
