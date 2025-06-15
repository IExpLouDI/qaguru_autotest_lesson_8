import os

### test data
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
DIR_WITH_DATA = os.path.join(ROOT_DIR, "tests_data")
USERS_DATA = os.path.join(DIR_WITH_DATA, "users.csv")
