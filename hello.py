import os

print('Hello from python executing inside Jenkins')
print(f'APP_ENV is {os.getenv("APP_ENV")})')
print(f'BUILD_OWNER is {os.getenv("BUILD_OWNER")})')