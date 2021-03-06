#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gym_minigrid.minigrid import *
from gym_minigrid.register import register
from gym import error, spaces, utils

class FourRoomsEnv(MiniGridEnv):
    """
    Classic 4 rooms gridworld environment.
    Can specify agent and goal position, if not it set at random.
    """
# goal_pos=np.array([3,1])):Ω
    def __init__(self, max_steps=100, agent_pos=np.array([3,3]),
     goal_pos=np.array([9,9])):
     # goal_pos=np.array([3,9])):
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        super().__init__(grid_size=13, max_steps=max_steps)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(0, 0)
        self.grid.horz_wall(0, height - 1)
        self.grid.vert_wall(0, 0)
        self.grid.vert_wall(width - 1, 0)

        room_w = width // 2
        room_h = height // 2

        # For each row of rooms
        for j in range(0, 2):

            # For each column
            for i in range(0, 2):
                xL = i * room_w
                yT = j * room_h
                xR = xL + room_w
                yB = yT + room_h

                # Bottom wall and door
                if i + 1 < 2:
                    self.grid.vert_wall(xR, yT, room_h)
                    pos = (xR, yT +3) #self._rand_int(yT + 1, yB))
                    self.grid.set(*pos, None)

                # Bottom wall and door
                if j + 1 < 2:
                    self.grid.horz_wall(xL, yB, room_w)
                    pos = (xL+3, yB) #(self._rand_int(xL + 1, xR), yB)
                    self.grid.set(*pos, None)

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = 3 #self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos

        else:
            self.place_obj(Goal())

        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info

register(
    id='MiniGrid-FourRooms-v0',
    entry_point='gym_minigrid.envs:FourRoomsEnv'
)



class FourRoomsDistractorsEnv(MiniGridEnv):
    """
    Classic 4 rooms gridworld environment.
    Can specify agent and goal position, if not it set at random.
    """
# goal_pos=np.array([3,1])):Ω
    def __init__(self, max_steps=100, agent_pos=np.array([3,3]),
     goal_pos=np.array([9,9])):
     # goal_pos=np.array([3,9])):
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        self._distraction_default_pos = np.array([9,3])
        super().__init__(grid_size=13, max_steps=max_steps)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(0, 0)
        self.grid.horz_wall(0, height - 1)
        self.grid.vert_wall(0, 0)
        self.grid.vert_wall(width - 1, 0)

        room_w = width // 2
        room_h = height // 2

        # For each row of rooms
        for j in range(0, 2):

            # For each column
            for i in range(0, 2):
                xL = i * room_w
                yT = j * room_h
                xR = xL + room_w
                yB = yT + room_h

                # Bottom wall and door
                if i + 1 < 2:
                    self.grid.vert_wall(xR, yT, room_h)
                    pos = (xR, yT +3) #self._rand_int(yT + 1, yB))
                    self.grid.set(*pos, None)

                # Bottom wall and door
                if j + 1 < 2:
                    self.grid.horz_wall(xL, yB, room_w)
                    pos = (xL+3, yB) #(self._rand_int(xL + 1, xR), yB)
                    self.grid.set(*pos, None)

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = 3 #self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos

            distraction = Distraction()
            self.put_obj(distraction, *self._distraction_default_pos)
            distraction.init_pos, distraction.cur_pos = self._distraction_default_pos
        else:
            self.place_obj(Goal())

        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info

register(
    id='MiniGrid-FourRoomsDistractor-v0',
    entry_point='gym_minigrid.envs:FourRoomsDistractorsEnv'
)




class FourRoomsTransferEnv(MiniGridEnv):
    """
    Classic 4 rooms gridworld environment.
    Can specify agent and goal position, if not it set at random.
    """

    def __init__(self, max_steps=100, 
                                      #   agent_pos=np.array([3,3]),
                                      # goal_pos=np.array([9,9]),
                                      # distraction_pos = np.array([9,3]) ):
                                        agent_pos=np.array([3,9]),
                                      goal_pos=np.array([9,3]),
                                      distraction_pos = np.array([9,9]) ):
     # goal_pos=np.array([3,9])):
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        self._distraction_default_pos = distraction_pos
        super().__init__(grid_size=13, max_steps=max_steps)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(0, 0)
        self.grid.horz_wall(0, height - 1)
        self.grid.vert_wall(0, 0)
        self.grid.vert_wall(width - 1, 0)

        room_w = width // 2
        room_h = height // 2

        # For each row of rooms
        for j in range(0, 2):

            # For each column
            for i in range(0, 2):
                xL = i * room_w
                yT = j * room_h
                xR = xL + room_w
                yB = yT + room_h

                # Bottom wall and door
                if i + 1 < 2:
                    self.grid.vert_wall(xR, yT, room_h)
                    pos = (xR, yT +3) #self._rand_int(yT + 1, yB))
                    self.grid.set(*pos, None)

                # Bottom wall and door
                if j + 1 < 2:
                    self.grid.horz_wall(xL, yB, room_w)
                    pos = (xL+3, yB) #(self._rand_int(xL + 1, xR), yB)
                    self.grid.set(*pos, None)

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = 3 #self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos

            distraction = Distraction()
            self.put_obj(distraction, *self._distraction_default_pos)
            distraction.init_pos, distraction.cur_pos = self._distraction_default_pos
        else:
            self.place_obj(Goal())

        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info

    def transfer(self):
        self._distraction_default_pos = np.array([9,9])
        self._goal_default_pos = np.array([9,3])

register(
    id='MiniGrid-FourRoomsTransfer-v0',
    entry_point='gym_minigrid.envs:FourRoomsTransferEnv'
)




class FourRoomsTrapsEnv(MiniGridEnv):
    """
    Classic 4 rooms gridworld environment.
    Can specify agent and goal position, if not it set at random.
    """
# goal_pos=np.array([3,1])):Ω
    def __init__(self, max_steps=100, agent_pos=np.array([3,3]),
             goal_pos=np.array([9,9])):
             # goal_pos=np.array([3,9])):
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        self._trap_default_pos = np.array([9,3])
        super().__init__(grid_size=13, max_steps=max_steps)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(0, 0)
        self.grid.horz_wall(0, height - 1)
        self.grid.vert_wall(0, 0)
        self.grid.vert_wall(width - 1, 0)

        room_w = width // 2
        room_h = height // 2

        # For each row of rooms
        for j in range(0, 2):

            # For each column
            for i in range(0, 2):
                xL = i * room_w
                yT = j * room_h
                xR = xL + room_w
                yB = yT + room_h

                # Bottom wall and door
                if i + 1 < 2:
                    self.grid.vert_wall(xR, yT, room_h)
                    pos = (xR, yT +3) #self._rand_int(yT + 1, yB))
                    self.grid.set(*pos, None)

                # Bottom wall and door
                if j + 1 < 2:
                    self.grid.horz_wall(xL, yB, room_w)
                    pos = (xL+3, yB) #(self._rand_int(xL + 1, xR), yB)
                    self.grid.set(*pos, None)

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = 3 #self._rand_int(0, 4)  # assuming random start direction
        else:
            self.place_agent()


        goal = Goal()
        self.put_obj(goal, *self._goal_default_pos)
        goal.init_pos, goal.cur_pos = self._goal_default_pos

        trap = Trap()
        self.put_obj(trap, *self._trap_default_pos)
        trap.init_pos, trap.cur_pos = self._trap_default_pos


        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info

register(
    id='MiniGrid-FourRoomsTraps-v0',
    entry_point='gym_minigrid.envs:FourRoomsTrapsEnv'
)



class FourRoomsWindyEnv(MiniGridEnv):
    """
    Classic 4 rooms gridworld environment.
    Can specify agent and goal position, if not it set at random.
    """

    def __init__(self, max_steps=100, 
                                      # agent_pos=np.array([3,3]),
                                      # goal_pos=np.array([9,9]),
                                      # distraction_pos = np.array([9,3]),
                                      # ):
                                        agent_pos=np.array([3,9]),
                                      goal_pos=np.array([9,3]),
                                      distraction_pos = np.array([9,9]) ):
        self.windy_states= [np.array([4,2]),np.array([4,3]),np.array([4,4])]
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        self._distraction_default_pos = distraction_pos
        super().__init__(grid_size=13, max_steps=max_steps)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(0, 0)
        self.grid.horz_wall(0, height - 1)
        self.grid.vert_wall(0, 0)
        self.grid.vert_wall(width - 1, 0)

        room_w = width // 2
        room_h = height // 2

        # For each row of rooms
        for j in range(0, 2):

            # For each column
            for i in range(0, 2):
                xL = i * room_w
                yT = j * room_h
                xR = xL + room_w
                yB = yT + room_h

                # Bottom wall and door
                if i + 1 < 2:
                    self.grid.vert_wall(xR, yT, room_h)
                    pos = (xR, yT +3) #self._rand_int(yT + 1, yB))
                    self.grid.set(*pos, None)

                # Bottom wall and door
                if j + 1 < 2:
                    self.grid.horz_wall(xL, yB, room_w)
                    pos = (xL+3, yB) #(self._rand_int(xL + 1, xR), yB)
                    self.grid.set(*pos, None)

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            self.agent_dir = 3 #self._rand_int(0, 4)  
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos

            distraction = Distraction()
            self.put_obj(distraction, *self._distraction_default_pos)
            distraction.init_pos, distraction.cur_pos = self._distraction_default_pos
        else:
            self.place_obj(Goal())

        self.mission = 'Reach the goal'

    def step(self, action):
        # import pdb;pdb.set_trace()
        # print(action)
        if np.any(np.all(self.agent_pos == self.windy_states, axis=1)) and action==self.actions.right:
            if np.random.rand() > 0.5:
                action=self.actions.left
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info

    def transfer(self):
        self._distraction_default_pos = np.array([9,9])
        self._goal_default_pos = np.array([9,3])

register(
    id='MiniGrid-FourRoomsWindy-v0',
    entry_point='gym_minigrid.envs:FourRoomsWindyEnv'
)