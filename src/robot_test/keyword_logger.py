ROBOT_LISTENER_API_VERSION = 2


def start_keyword(name, attrs):
    print(f"{name} {" ".join(attrs["args"])}")
