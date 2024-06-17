# Pong

This code is a partially done version of the classic game "pong". Your mission
is to create a fully working one-player version that:

1. Has the ball move up/down and left/right
2. Has the ball bounce off the top, bottom, and right walls
3. Has the ball bounce off the paddle
4. Has a "score" variable that shows how many hits in a row the user has had
5. Resets the game and the "score" if the player misses the ball and it touches
   the left wall

## Setup

The only thing that you _should_ need to do to get this project up and running
is:

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

### 3. Verify it runs

You now should be able to run the program and see a white ball and paddle set
against a black background. Assuming you have that, move onto the next task.

## Game Development

Now that everything is setup, you can start with developing the game.

## Read the Code

Look through the code and try and understand it. Pay particular attention to:

- The difference between `ball_x` vs. `ball_x_speed`
- What happens during a "collision"
- Why the paddle can only move up (but not down)

## Modify the Code

Now that you understand the code a little bit, work to accomplish each of the
following tasks in order:

1. Have the ball move up/down and left/right
    - Hint: examine the `ball_x_speed` and `ball_y_speed` variables
2. Change the ball from white to blue
    - Hint: change the `get_rgb_color()` function
2. Have the ball bounce off the top, bottom, and right walls
    - Hint: examine how the ball detects/reacts to the right wall and copy the logic
3. Have the ball bounce off the paddle
    - Hint: look at the `ball_y_speed`
4. Have a "score" variable that shows how many hits in a row the user has had
    - Hint: research `pygame.font.Font` on the internet
5. Reset the game and the "score" if the player misses the ball and it touches
   the left wall

### Difficulties:

The hardest part of developing this game is to detect when the ball hits the
paddle. The way I think about it is the following: if the ball is to the left of
the right side of the paddle **AND** to the right of the left side of the paddle
**AND** to below the top of the paddle **AND** above the bottom of the paddle,
then it's hitting the paddle. You can represent this with a complex `if`
statement that uses three `and` connectors.

## Extend the Code

- Two-player pong with a left AND right paddle
- Have the ball become a new, "random" color every time it hits a paddle
- Have the ball bounce off the paddle at an angle dependent on where it hits the paddle
