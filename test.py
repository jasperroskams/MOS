import pyxel
import matplotlib.pyplot as plt
import numpy as np



SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024

MAX_BUBBLE_SPEED = 1.8
NUM_INITIAL_BUBBLES = 50
NUM_EXPLODE_BUBBLES = 2


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Bubble:
    def __init__(self):
        self.r = pyxel.rndf(1, 2)

        self.pos = Vec2(
            pyxel.rndf(self.r, SCREEN_WIDTH - self.r),
            pyxel.rndf(self.r, SCREEN_HEIGHT - self.r),
        )

        self.vel = Vec2(
            pyxel.rndf(-MAX_BUBBLE_SPEED, MAX_BUBBLE_SPEED),
            pyxel.rndf(-MAX_BUBBLE_SPEED, MAX_BUBBLE_SPEED),
        )

        self.color = pyxel.rndi(1, 15)

    def update(self, game):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y
        if self.vel.x < 0:
            self.vel.x += (self.r) // 25
        else:
            self.vel.x -= (self.r) // 25
        if self.vel.y < 0:
            self.vel.y += (self.r) // 25
        else:
            self.vel.y -= (self.r) // 25


        if self.vel.x < 0 and self.pos.x < self.r:
            self.vel.x *= -1

        if self.vel.x > 0 and self.pos.x > SCREEN_WIDTH - self.r:
            self.vel.x *= -1

        if self.vel.y < 0 and self.pos.y < self.r:
            self.vel.y *= -1

        if self.vel.y > 0 and self.pos.y > SCREEN_HEIGHT - self.r:
            self.vel.y *= -1
        if self.r > 10:
            for bubbel in game.bubbles:
                if self.r > bubbel.r:
                    verschil = abs(self.pos.x - bubbel.pos.x) + abs(self.pos.y - bubbel.pos.y)

                    zwaartekracht = 0.0005 * (self.r - bubbel.r) - (verschil / 1000000)
                    if zwaartekracht <= 0:
                        zwaartekracht = 0.0000000001
                    if bubbel.pos.x > self.pos.x:
                        bubbel.vel.x -= zwaartekracht
                    else:
                        bubbel.vel.x += zwaartekracht
                    if bubbel.pos.y > self.pos.y:
                        bubbel.vel.y -= zwaartekracht
                    else:
                        bubbel.vel.y += zwaartekracht


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Pyxel Bubbles", capture_scale=1)
        pyxel.mouse(True)

        self.is_exploded = False
        self.bubbles = [Bubble() for _ in range(NUM_INITIAL_BUBBLES)]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        num_bubbles = len(self.bubbles)

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            for i in range(num_bubbles):
                bubble = self.bubbles[i]
                dx = bubble.pos.x - pyxel.mouse_x
                dy = bubble.pos.y - pyxel.mouse_y

                if dx * dx + dy * dy < bubble.r * bubble.r:
                    self.is_exploded = True
                    new_r = pyxel.sqrt(bubble.r * bubble.r / NUM_EXPLODE_BUBBLES) + (bubble.r / 100)

                    for j in range(NUM_EXPLODE_BUBBLES):
                        angle = 360 * j / NUM_EXPLODE_BUBBLES

                        new_bubble = Bubble()
                        new_bubble.r = new_r
                        new_bubble.pos.x = bubble.pos.x + (
                            bubble.r + new_r
                        ) * pyxel.cos(angle)
                        new_bubble.pos.y = bubble.pos.y + (
                            bubble.r + new_r
                        ) * pyxel.sin(angle)
                        new_bubble.vel.x = pyxel.cos(angle) * MAX_BUBBLE_SPEED
                        new_bubble.vel.y = pyxel.sin(angle) * MAX_BUBBLE_SPEED
                        self.bubbles.append(new_bubble)

                    del self.bubbles[i]
                    break

        for i in range(num_bubbles - 1, -1, -1):
            bi = self.bubbles[i]
            bi.update(self)

            for j in range(i - 1, -1, -1):
                bj = self.bubbles[j]
                dx = bi.pos.x - bj.pos.x
                dy = bi.pos.y - bj.pos.y
                total_r = bi.r + bj.r

                if dx * dx + dy * dy < total_r * total_r:
                    if bi.r < bj.r:
                        new_bubble = Bubble()
                        new_bubble.r = pyxel.sqrt(bi.r * bi.r + bj.r * bj.r) + ((bi.r + bj.r) / 100)
                        new_bubble.pos.x = bj.pos.x
                        new_bubble.pos.y = bj.pos.y
                        new_bubble.vel.x = bj.vel.x
                        new_bubble.vel.y = bj.vel.y
                        new_bubble.color = bj.color
                        bi.is_exploded = True
                        new_r = pyxel.sqrt(bi.r * bi.r / NUM_EXPLODE_BUBBLES) + (bi.r / 100)
                        for j in range(NUM_EXPLODE_BUBBLES):
                            angle = 360 * j / NUM_EXPLODE_BUBBLES
                            new_bubble1 = Bubble()
                            new_bubble1.r = new_r
                            new_bubble1.pos.x = bi.pos.x + (bi.r + new_r) * pyxel.cos(angle)
                            new_bubble1.pos.y = bi.pos.y + (bi.r + new_r) * pyxel.sin(angle)
                            new_bubble1.vel.x = pyxel.cos(angle) * MAX_BUBBLE_SPEED
                            new_bubble1.vel.y = pyxel.sin(angle) * MAX_BUBBLE_SPEED
                            self.bubbles.append(new_bubble1)
                        del self.bubbles[i]
                        break
                    else:
                        new_bubble = Bubble()
                        new_bubble.r = pyxel.sqrt(bi.r * bi.r + bj.r * bj.r)
                        new_bubble.pos.x = bi.pos.x
                        new_bubble.pos.y = bi.pos.y
                        new_bubble.vel.x = bi.vel.x
                        new_bubble.vel.y = bi.vel.y
                        new_bubble.color = bi.color
                        bj.is_exploded = True
                        new_r = pyxel.sqrt(bj.r * bj.r / NUM_EXPLODE_BUBBLES) + (bj.r / 100)
                        for j in range(NUM_EXPLODE_BUBBLES):
                            angle = 360 * j / NUM_EXPLODE_BUBBLES
                            new_bubble2 = Bubble()
                            new_bubble2.r = new_r
                            new_bubble2.pos.x = bj.pos.x + (bj.r + new_r) * pyxel.cos(angle)
                            new_bubble2.pos.y = bj.pos.y + (bj.r + new_r) * pyxel.sin(angle)
                            new_bubble2.vel.x = pyxel.cos(angle) * MAX_BUBBLE_SPEED
                            new_bubble2.vel.y = pyxel.sin(angle) * MAX_BUBBLE_SPEED
                            self.bubbles.append(new_bubble2)
                        del self.bubbles[j]
                        break
                    self.bubbles.append(new_bubble)
                    del self.bubbles[i]
                    del self.bubbles[j]
                    num_bubbles -= 1
                    break

    def draw(self):
        pyxel.cls(0)

        for bubble in self.bubbles:
            pyxel.circ(bubble.pos.x, bubble.pos.y, bubble.r, bubble.color)

        if not self.is_exploded and pyxel.frame_count % 20 < 10:
            pyxel.text(96, 50, "CLICK ON BUBBLE", pyxel.frame_count % 15 + 1)


App()
