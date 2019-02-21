from VacEnvWrapper import Environment
import VacWindowWrapper as Window

# TESTING
from random import randint
import threading
import time

def test():

    def runloop(env):
        start = time.time()
        for x in range(10*20*60):
            env.step(randint(0, 4), 1 / 20)
            # if not env.running():
            #    return
        end = time.time()
        print(end - start)

    env1 = Environment()
    env2 = Environment()
    env3 = Environment()
    env4 = Environment()
    env5 = Environment()
    env6 = Environment()
    env7 = Environment()
    env8 = Environment()

    print(env1.running())
    print(env1.score())
    print(env1.world())

    Window.init(512, -50, 50, -50, 50)
    Window.attachEnv(env1.obj)
    Window.attachEnv(env2.obj)
    Window.attachEnv(env3.obj)
    Window.attachEnv(env4.obj)
    Window.attachEnv(env5.obj)
    Window.attachEnv(env6.obj)
    Window.attachEnv(env7.obj)
    Window.attachEnv(env8.obj)

    t = threading.Thread(target=Window.show)
    t.start()

    t1 = threading.Thread(target=runloop, args=[env1])
    t2 = threading.Thread(target=runloop, args=[env2])
    t3 = threading.Thread(target=runloop, args=[env3])
    t4 = threading.Thread(target=runloop, args=[env4])
    t5 = threading.Thread(target=runloop, args=[env5])
    t6 = threading.Thread(target=runloop, args=[env6])
    t7 = threading.Thread(target=runloop, args=[env7])
    t8 = threading.Thread(target=runloop, args=[env8])

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()

    Window.detachEnv(env1.obj)
    Window.detachEnv(env2.obj)
    Window.detachEnv(env3.obj)
    Window.detachEnv(env4.obj)
    Window.detachEnv(env5.obj)
    Window.detachEnv(env6.obj)
    Window.detachEnv(env7.obj)
    Window.detachEnv(env8.obj)

    Window.close()

    t.join()


test()
