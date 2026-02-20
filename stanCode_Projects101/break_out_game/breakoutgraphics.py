"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

The game was developed using custom methods and a variety of variables.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout',
                 __dx=0, __dy=0):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.paddle_offset = paddle_offset
        self.__dx = 0
        self.__dy = 0
        self.is_game_start = False
        self.total_brick = brick_rows * brick_cols

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                       y=window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width - BALL_RADIUS) / 2, y=(window_height - BALL_RADIUS) / 2)
        self.ball.filled = True
        self.window.add(self.ball)
        self.brick_count = brick_cols * brick_rows
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmousemoved(self.horizontal_move)
        onmouseclicked(self.ball_move)

        # Draw bricks
        color = None
        for i in range(brick_cols):
            for j in range(brick_rows):
                current_x = i * (brick_width + brick_spacing)  # Define x for brick
                current_y = brick_offset + j*(brick_height + brick_spacing)  # Define y for brick
                brick = GRect(brick_width, brick_height, x=current_x, y=current_y)  # Create brick by using "for_in range
                if j <= 1:
                    color = (255, 0, 0)
                if 1 < j <= 3:
                    color = (255, 215, 0)
                if 3 < j <= 5:
                    color = (255, 255, 0)
                if 5 < j <= 7:
                    color = (0, 102, 0)
                if 7 < j:
                    color = (0, 51, 153)

                brick.filled = True
                brick.fill_color = color
                self.window.add(brick)

    def horizontal_move(self, mouse):
        if 0+self.paddle.width/2 < mouse.x < (self.window.width - self.paddle.width-self.paddle.width/2):
            self.paddle.x = mouse.x - self.paddle.width/2
        if mouse.x >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        if mouse.x <= 0:
            self.paddle.x = 0

    def ball_move(self, mouse):
        self.is_game_start = True
        self.__dy = MAX_X_SPEED
        self.__dy = INITIAL_Y_SPEED

    def set_ball_speed(self, __dx, __dy):
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.ball.dx = __dx
        self.ball.dy = __dy

    def check_game_start(self):
        return self.is_game_start

    def get_ball(self):
        return self.ball

    def get_window(self):
        return self.window

    def get_vx(self):
        vx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            vx = -vx
        return vx

    def get_vy(self):
        return INITIAL_Y_SPEED

    def get_hit_object(self):
        ball_x = self.ball.x
        ball_y = self.ball.y
        r2 = self.ball.width
        obj = self.window.get_object_at(ball_x, ball_y)  # Check left top corner
        if obj is not None:
            return obj
        obj = self.window.get_object_at(ball_x+r2, ball_y)  # Check right top corner
        if obj is not None:
            return obj
        obj = self.window.get_object_at(ball_x, ball_y + r2)  # Check left down corner
        if obj is not None:
            return obj
        obj = self.window.get_object_at(ball_x + r2, ball_y + r2)  # Check right down corner
        if obj is not None:
            return obj
        return None

    def reset_ball(self):
        self.ball.x = (self.window.width - BALL_RADIUS)/2
        self.ball.y = (self.window.height - BALL_RADIUS)/2
        self.is_game_start = False

    def get_total_brick(self):
        total_brick = BRICK_ROWS * BRICK_COLS
        return total_brick








