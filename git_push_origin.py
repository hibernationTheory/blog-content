import os

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
os.chdir(CURRENT_PATH)
os.system('git push origin')