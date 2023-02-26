import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
print(base_dir)

load_dotenv(os.path.join(base_dir,'.env'))
print(os.environ.get("SOME_VAR"))