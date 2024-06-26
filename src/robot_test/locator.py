from enum import Enum


class LocKey(Enum):
    ID = "id"
    CLASS = "class"
    TYPE = "type"
    NAME = "name"

    def __str__(self) -> str:
        return self.value


class LocVal(Enum):
    BUTTON = "button"

    def __str__(self) -> str:
        return self.value


def make_loc(key: LocKey, val: str | LocVal) -> str:
    if isinstance(val, LocVal):
        val = str(val)
    if " " in val:
        val = f'"{val}"'
    return f"{key:{val}}"


def main() -> int:
    locstr: str = make_loc(key=LocKey.ID, val=LocVal.BUTTON)


if __name__ == "__main__":
    exit(main())
