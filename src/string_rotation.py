def string_rotation(candidate: str, container: str) -> bool:
    if len(candidate) != len(container):
        return False

    return candidate in container+container
