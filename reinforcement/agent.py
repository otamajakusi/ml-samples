import random
from environment import Environment


class Agent:
    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state):
        return random.choice(self.actions)


def main():
    grid = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 9, 0, 0], [0, 0, 0, 0]]

    env = Environment(grid)
    agent = Agent(env)

    for i in range(10):
        state = env.reset()
        total_reward = 0
        done = False
        while not done:
            action = agent.policy(state)
            """
            行動を指定して次の状態を得る
            行動の報酬を得る
            完了を得る
            """
            next_state, reward, done = env.step(action)
            total_reward += reward
            state = next_state
        print(f"Episode {i}: Agent gets {total_reward:.1f} reward")


if __name__ == "__main__":
    main()
