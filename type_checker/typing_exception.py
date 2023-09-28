class TypingException(Exception):
    def __init__(self, arg_name: str, expected_type: type, actual_type: type) -> None:
        self.message = f"""Arg '{arg_name}' expects {expected_type.__name__} type, but actually is {actual_type.__name__} type!"""
        super().__init__(self.message)