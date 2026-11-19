# Asteroids

A small Asteroids-style arcade game built with Python and Pygame. Pilot the ship, avoid incoming asteroids, and shoot them to split or destroy them. The game ends when the player collides with an asteroid.

## Requirements

- [`uv`](https://docs.astral.sh/uv/)

uv determines the python-version, downloads a managed Python 3.13 installation if necessary, creates .venv, and installs the locked dependencies.

## Installation

Clone or download the repository, then open a terminal in the project directory and install the dependencies:

```bash
uv sync
```

This creates a project virtual environment and installs Pygame 2.6.1 from `pyproject.toml`.

## Running the game

From the project directory, run:

```bash
uv run python main.py
```

## Controls

| Key | Action |
| --- | --- |
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

Close the game window to quit.

## Gameplay

- Asteroids spawn at random edges of the screen and travel across the play area.
- Shooting an asteroid destroys or splits it, depending on its size.
- Colliding with an asteroid ends the game.
