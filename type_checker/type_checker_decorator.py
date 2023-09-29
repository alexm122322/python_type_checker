from type_checker.type_checker_impl import TypeChecker


def check_type(func):
    def inner(*args, **kwargs):
        """Check if method arguments type matched.
        
        Args:
            args: Arguments of checking function.
            kwargs: Dictionary arguments of checking function.

        Raises:
            TypingException: if some type of method argument is mismatch.
        """
        
        type_checker = TypeChecker(args, kwargs)
        type_checker.check(func)
        return func(*args, **kwargs)
    
    return inner     