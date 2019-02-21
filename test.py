import numpy as np
import vacenv
import gym
import threading

from stable_baselines import A2C
from stable_baselines.common.policies import MlpLstmPolicy
from stable_baselines.common.vec_env import DummyVecEnv

if __name__ == '__main__':
    env = vacenv.VacEnvironment()
    # env.reset()
    env_dummy = DummyVecEnv([lambda: env])

    # setup Window
    vacenv.Window.init(512, -50, 50, -50, 50)
    vacenv.Window.attachEnv(env.obj.obj)
    t = threading.Thread(target=vacenv.Window.show)
    t.start()

    model = A2C(MlpLstmPolicy, env_dummy, verbose=1, tensorboard_log="./a2c_tensorboard/" )
    model.learn(total_timesteps=10000000, log_interval=1000)

    print("Saving model to model.pkl")
    model.save("model.pkl")
