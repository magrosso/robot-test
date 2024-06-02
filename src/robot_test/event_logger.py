ROBOT_LISTENER_API_VERSION = 2


def start_suite(name, attrs):
    print(f"START SUITE: {name=}, id={attrs["id"]=}, start={attrs["starttime"]}")


def end_suite(name, attrs):
    print(
        f"END SUITE: {name=}, id={attrs["id"]=}, start={attrs["starttime"]}, end={attrs["endtime"]}"
    )


def start_test(name, attrs):
    print(
        f"START TEST: {name=} id={attrs["id"]}, tags={attrs["tags"]}, start={attrs["starttime"]}"
    )


def end_test(name, attrs):
    print(
        f"END TEST: {name=} id={attrs["id"]}, tags={attrs["tags"]}, start={attrs["starttime"]}, end={attrs["endtime"]}"
    )


def start_keyword(name, attrs):
    print(
        f"START KEYWORD: {name} {" ".join(attrs["args"])}, start={attrs["starttime"]}"
    )


def end_keyword(name, attrs):
    print(
        f"END KEYWORD: {name} {" ".join(attrs["args"])}, start={attrs["starttime"]}, end={attrs["endtime"]}"
    )
