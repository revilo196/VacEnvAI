from vacenv.vacenvwrapper import Environment
from vacenv.vacenvgym import VacEnvironment
import vacenv.vacwindowwrapper as Window

from gym.envs.registration import register

register(
    id='vacenv-v0',
    entry_point='vacenv:VacEnvironment',
)