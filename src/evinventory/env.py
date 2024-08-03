from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
    EVAN_DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
