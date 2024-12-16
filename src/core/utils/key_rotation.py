import os

def rotate_key(config, index):
    if index < len(config.LLAMA_CLOUD_API_KEYS):
        os.environ["LLAMA_CLOUD_API_KEY"] = config.LLAMA_CLOUD_API_KEYS[index]
        print("Rotated LLAMA_CLOUD_API_KEY: ", os.environ["LLAMA_CLOUD_API_KEY"])
        return True
    return False
