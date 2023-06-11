import os
from dotenv import load_dotenv

load_dotenv()

# CROS Origins

FRONT_END_PROTOCOL = os.environ.get('FRONT_END_PROTOCOL')
FRONT_END_HOST = os.environ.get('FRONT_END_HOST')
FRONT_END_PORT = os.environ.get('FRONT_END_PORT')
FRONT_END_URL = f"{FRONT_END_PROTOCOL}://{FRONT_END_HOST}:{FRONT_END_PORT}"
origins = ["*"]

# User Microservice
USER_MS_HOST = os.environ.get('USER_MS_HOST')
USER_MS_PORT = os.environ.get('USER_MS_PORT')
USER_MS_URL = f"http://{USER_MS_HOST}:{USER_MS_PORT}"
print("USER_MS_URL: ", USER_MS_URL)

# Catalogue Microservice
CATALOGUE_MS_HOST = os.environ.get('CATALOGUE_MS_HOST')
CATALOGUE_MS_PORT = os.environ.get('CATALOGUE_MS_PORT')
CATALOGUE_MS_URL = f"http://{CATALOGUE_MS_HOST}:{CATALOGUE_MS_PORT}"
print("CATALOGUE_MS_URL: ", CATALOGUE_MS_URL)


# Recommendation Microservice
RECOMMENDATION_MS_HOST = os.environ.get('RECOMMENDATION_MS_HOST')
RECOMMENDATION_MS_PORT = os.environ.get('RECOMMENDATION_MS_PORT')
RECOMMENDATION_MS_URL = f"http://{RECOMMENDATION_MS_HOST}:{RECOMMENDATION_MS_PORT}"

# Rating Microservice
RATING_MS_HOST = os.environ.get('RATING_MS_HOST')
RATING_MS_PORT = os.environ.get('RATING_MS_PORT')
RATING_MS_URL = f"http://{RATING_MS_HOST}:{RATING_MS_PORT}"
print("RATING_MS_URL: ", RATING_MS_URL)