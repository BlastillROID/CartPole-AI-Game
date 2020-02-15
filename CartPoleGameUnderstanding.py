import gym
import keyboard
env = gym.make('CartPole-v1')
step_index=0
env.reset()
while True:
    try:
        step_index= step_index+1
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print("Step {}:".format(step_index))
        print("action: {}".format(action))
        print("observation: {}".format(observation))
        print("reward: {}".format(reward))
        print("done: {}".format(done))
        print("info: {}".format(info))
        if keyboard.is_pressed('a'):
            break
    except:
        break