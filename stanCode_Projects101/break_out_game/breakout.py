"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This exciting game involves using a paddle to bounce a ball and break bricks.
Remember, you have only three lives; the game ends once they are all lost.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    lives = NUM_LIVES
    total_brick = graphics.get_total_brick()
    while True:
        pause(FRAME_RATE)  # Ensure it pause and wait for a click
        if lives <= 0 or total_brick <= 0:
            break
        else:
            if graphics.check_game_start():  # Check if the game starts or not
                graphics.get_ball().move(vx, vy)
                collision = graphics.get_hit_object()  # When ball collide sth, the "obj" returns to here
                if graphics.get_ball().x <= 0 or graphics.get_ball().x + graphics.get_ball().width >= graphics.window.width:
                    vx = -vx
                if graphics.get_ball().y <= 0:
                    vy = -vy
                if collision is not None:
                    if collision == graphics.paddle:  # If colliding with paddle, invert the Y to negative value
                        if vy > 0:
                            vy = -vy
                    else:
                        vy = -vy  # If not paddle, still invert the Y to negative value
                        graphics.window.remove(collision)  # remove collided brick(s)
                        total_brick -= 1
                if graphics.get_ball().y > graphics.window.height:
                    graphics.reset_ball()
                    vx = graphics.get_vx()
                    vy = graphics.get_vy()
                    lives -= 1


if __name__ == '__main__':
    main()
