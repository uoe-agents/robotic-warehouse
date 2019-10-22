import os
import sys

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(TEST_DIR, os.pardir))
sys.path.insert(0, PROJECT_DIR)

from robotic_warehouse.warehouse import Warehouse, Direction, Action


def test_simple_movement_down():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.DOWN
    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 26


def test_simple_movement_up():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.UP
    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 24


def test_simple_movement_left():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.LEFT
    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 3
    assert env.agents[0].y == 25


def test_simple_movement_right():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT
    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 5
    assert env.agents[0].y == 25


def test_simple_wall_collision_up():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 0
    env.agents[0].dir = Direction.UP
    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 0


def test_simple_wall_collision_down():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 28
    env.agents[0].dir = Direction.DOWN
    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 28


def test_simple_wall_collision_right():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 9  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT
    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 9
    assert env.agents[0].y == 25


def test_simple_wall_collision_left():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 0  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.LEFT
    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 0
    assert env.agents[0].y == 25


def test_head_collision():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=2, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT

    env.agents[1].x = 5  # should place it next to the other
    env.agents[1].y = 25
    env.agents[1].dir = Direction.LEFT
    env._recalc_grid()
    env.step([Action.FORWARD, Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[1].x == 5
    assert env.agents[1].y == 25


def test_chain_movement_1():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=2, msg_bits=0)
    env.reset()
    env.agents[0].x = 3
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT

    env.agents[1].x = 4
    env.agents[1].y = 25
    env.agents[1].dir = Direction.RIGHT
    env._recalc_grid()
    env.step([Action.FORWARD, Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[1].x == 5
    assert env.agents[1].y == 25


def test_chain_movement_2():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=2, msg_bits=0)
    env.reset()
    env.agents[0].x = 8
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT

    env.agents[1].x = 9
    env.agents[1].y = 25
    env.agents[1].dir = Direction.RIGHT
    env._recalc_grid()
    env.step([Action.FORWARD, Action.FORWARD])

    assert env.agents[0].x == 8
    assert env.agents[0].y == 25
    assert env.agents[1].x == 9
    assert env.agents[1].y == 25


def test_chain_movement_3():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=3, msg_bits=0)
    env.reset()
    env.agents[0].x = 3
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT

    env.agents[1].x = 4
    env.agents[1].y = 25
    env.agents[1].dir = Direction.RIGHT

    env.agents[2].x = 5
    env.agents[2].y = 26
    env.agents[2].dir = Direction.UP

    env._recalc_grid()
    env.step(3 * [Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[1].x == 5
    assert env.agents[1].y == 25
    assert env.agents[2].x == 5
    assert env.agents[2].y == 26


def test_circle_chain_movement():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=4, msg_bits=0)
    env.reset()
    env.agents[0].x = 3
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT

    env.agents[1].x = 4
    env.agents[1].y = 25
    env.agents[1].dir = Direction.UP

    env.agents[2].x = 4
    env.agents[2].y = 24
    env.agents[2].dir = Direction.LEFT

    env.agents[3].x = 3
    env.agents[3].y = 24
    env.agents[3].dir = Direction.DOWN

    env._recalc_grid()
    env.step(4 * [Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25

    assert env.agents[1].x == 4
    assert env.agents[1].y == 24

    assert env.agents[2].x == 3
    assert env.agents[2].y == 24

    assert env.agents[3].x == 3
    assert env.agents[3].y == 25


def test_turn_right_0():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.UP
    env._recalc_grid()
    env.step([Action.RIGHT])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[0].dir == Direction.RIGHT


def test_turn_right_1():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT
    env._recalc_grid()
    env.step([Action.RIGHT])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[0].dir == Direction.DOWN


def test_turn_right_2():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.DOWN
    env._recalc_grid()
    env.step([Action.RIGHT])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[0].dir == Direction.LEFT


def test_turn_right_3():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.LEFT
    env._recalc_grid()
    env.step([Action.RIGHT])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[0].dir == Direction.UP


def test_turn_left_0():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.UP
    env._recalc_grid()
    env.step([Action.LEFT])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[0].dir == Direction.LEFT


def test_turn_left_1():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.RIGHT
    env._recalc_grid()
    env.step([Action.LEFT])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[0].dir == Direction.UP


def test_turn_left_2():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.DOWN
    env._recalc_grid()
    env.step([Action.LEFT])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[0].dir == Direction.RIGHT


def test_turn_left_3():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = 25
    env.agents[0].dir = Direction.LEFT
    env._recalc_grid()
    env.step([Action.LEFT])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 25
    assert env.agents[0].dir == Direction.DOWN


def test_simple_carrying():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = env.shelfs[0].x = 4  # should place it in the middle (empty space)
    env.agents[0].y = env.shelfs[0].y = 25
    env.agents[0].dir = Direction.DOWN

    env.agents[0].carrying_shelf = env.shelfs[0]

    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 4
    assert env.agents[0].y == 26
    assert env.shelfs[0].x == 4
    assert env.shelfs[0].y == 26


def test_simple_carrying_collision():
    grid_size = (29, 10)

    env = Warehouse(grid_size=grid_size, n_agents=1, msg_bits=0)
    env.reset()
    env.agents[0].x = env.shelfs[0].x = 3
    env.agents[0].y = env.shelfs[0].y = 25
    env.agents[0].dir = Direction.LEFT

    env.agents[0].carrying_shelf = env.shelfs[0]

    env._recalc_grid()
    env.step([Action.FORWARD])

    assert env.agents[0].x == 3
    assert env.agents[0].y == 25
    assert env.shelfs[0].x == 3
    assert env.shelfs[0].y == 25