from type_checker.type_checker_impl import TypeChecker


def check_type(func):
    def inner(*args, **kwargs):
        """Check if method arguments type matched.
        Raise TypingException if type mismatch.
        """
        
        type_checker = TypeChecker(args, kwargs)
        type_checker.check(func)
        return func(*args, **kwargs)
    
    return inner     