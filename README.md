# Pong

## Setup

This code is a partially done version of the classic game "pong". Your mission
is to create a fully working one-player version that:

1. Has the ball move up/down and left/right
2. Has the ball bounce off the top, bottom, and right walls
3. Has the ball bounce off the paddle
4. Has a "score" variable that shows how many hits in a row the user has had
5. Resets the game and the "score" if the player misses the ball and it touches
   the left wall

The only thing that you _should_ need to do with this project is:

### 0. Open the project's workspace

Open `vscode` and select `File` -> `Open Workspace from File`. Then, select the
`pong.code-workspace` file within this project folder.

### 1. Install necessary extensions

On the left-most side of the `vscode` window, select the "Extensions" tab (four
small squares making a larger square) and install the following extensions:

- `Python`
- `Pylance` (auto installed with `Python` extension)
- `Black Formatter`
- `isort`

> Note: be careful to select only the "Microsoft approved" extensions.

### 2. Install necessary Python modules

Open the terminal window by selecting `Terminal` -> `New Terminal`. Then,
install all the required libraries by typing:

```
pip3 install pytest pygame
```

## Game Development

Work to accomplish each of the following tasks in order:

1. Have the ball move up/down and left/right
    - Hint: `ball_x_speed` and `ball_y_speed` variables
2. Change the ball from white to blue
    - Hint: You'll need to change the `get_rgb_color()` function
2. Have the ball bounce off the top, bottom, and right walls
    - Hint for look how the ball detects/reacts to the right wall and copy the logic
3. Have the ball bounce off the paddle
    - Hint: You'll have to alter `ball_y_speed`
4. Have a "score" variable that shows how many hits in a row the user has had
    - Hint: Do some research `pygame.font.Font` on the internet
5. Reset the game and the "score" if the player misses the ball and it touches
   the left wall

### Extensions:

- Two player pong with a left AND right paddle
- Have the ball become a "random" color every time it hits a paddle
- Have the ball bounce off the paddle at a different angle based on where it hits the paddle

### Difficulties:

The hardest part of this game, other than understanding the code, is to detect
when the ball is hitting the paddle. The way I think about it is the following:
if the ball is to the left of the right side of the paddle **AND** to the right
of the left side of the paddle **AND** to below the top of the paddle **AND**
above the bottom of the paddle then it's hitting the paddle. You can represent
this with a complex if statement that uses three `and` connectors.
