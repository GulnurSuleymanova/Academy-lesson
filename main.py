from mblock import event
# initialize variables

@event.greenflag
def on_greenflag():
  sprite.x = 0
  sprite.y = -41
  while True:
    sprite.set_costume('costume1')
    if sprite.is_keypressed('right arrow'):
      sprite.direction = 90
      sprite.set_costume('costume2')
      sprite.forward(10)

    if sprite.is_keypressed('left arrow'):
      sprite.set_costume('costume2')
      sprite.direction = -90
      sprite.forward(10)

