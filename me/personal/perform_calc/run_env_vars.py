import os

def __main__():
    os.environ['first_var'] = 'hello'
    print(" ### from run_env_vars")
    for key , value in os.environ.items():
        print(f"{key}    {value}")

if __name__ == "__main__":
    __main__()
