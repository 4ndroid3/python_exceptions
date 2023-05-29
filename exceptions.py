class UsernameException(Exception):
    
    def __init__(self, username):
        self.username = username
        self.message = f"Username '{self.username}' is not valid"

        super().__init__(self.message)


def validate_username(username):
    if len(username) < 6:
        raise UsernameException(username)
    return True

try:
    username = "sao"
    result = validate_username(username)

    print(result)

except UsernameException as e:
    print(e.message)
