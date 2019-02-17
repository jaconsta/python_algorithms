from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcXD13y6mFcL0HXJ5l2dtHW9wLXcIsvL-c6e9Gss3TMh-VlJgs0bqgWjcYBz6l4d7wqmMq8ghTRn36tCvjER1UnTeWPUQfLtAA7mHXPfeDz-A7vIgRyac7EppXc5eAzx4uAOAgjMJJ54nx8mRDVMZYfJ532qC9cBAXu53o3ozm_SMYQxw='

def main():
    print('hello')
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
