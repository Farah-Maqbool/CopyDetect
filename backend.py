import os
import uuid
import time
from dotenv import load_dotenv
from copyleaks import CopyleaksCloud
from copyleaks.consts import eProduct, SubmissionProperties

load_dotenv()
EMAIL = os.getenv("COPYLEAKS_EMAIL")
API_KEY = os.getenv("COPYLEAKS_API_KEY")

copyleaks = CopyleaksCloud(eProduct.Education)
