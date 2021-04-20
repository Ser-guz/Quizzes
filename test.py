import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


BASE_DIR2 = os.path.dirname(os.path.realpath(__file__))
BASE_DIR_0 = os.path.dirname(BASE_DIR2)

STATIC_DIR = os.path.join(BASE_DIR2, 'static/')
DIRS = [os.path.join(BASE_DIR, 'templates')]
DIRS2 = [os.path.join(BASE_DIR2, 'templates')]

print(1)