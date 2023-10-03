from inspect import Signature, _empty, signature
from typing import List, Tuple

from type_checker.typing_exception import TypingException


__all__ = ['TypeChecker']


class TypeChecker:
    """Check type for all method arguments

    Args:
        args: Arguments of checking function.
        kwargs: Dictionary arguments of checking function.

    Attributes:
        args (tuple): Arguments of checking function.
        kwargs (dict): Dictionary arguments of checking function.

    """

    def __init__(self, args: tuple, kwargs: dict):
        self._args = args
        self._kwargs = kwargs

    def check(self, func):
        """Entry point to TypeChecker

        Args:
            func (function): Checking function

        Raises:
            TypingException: if some type of method argument is mismatch.

        """

        sig = signature(func)
        method_args = self._create_method_args(sig)
        self._check_method_args(method_args)

    def _create_method_args(self, func_sig: Signature) -> List[Tuple]:
        """Create a list of method arguments wich contain name, value and expecting type.

        Args:
            func_sig: Signature of a checking method.

        Returns: 
            Return a list of complex arguments of method.

        """

        method_args: List[Tuple] = []
        sig_keys = list(func_sig.parameters.keys())
        params = func_sig.parameters

        for i, value in enumerate(self._args):
            key = sig_keys[i]
            method_args.append((key, value, params[key].annotation))

        for key, value in self._kwargs.items():
            method_args.append((key, value, params[key].annotation))

        return method_args

    def _check_method_args(self, method_args: List[Tuple]):
        """Check all method arguments.

        Args:
            method_args: List of method arguments.

        Raises:
            TypingException: if some type of method argument is mismatch.

        """

        for arg in method_args:
            self._check_and_raise_typing_exception(arg_name=arg[0],
                                                    expected_type=arg[2],
                                                    actual_type=type(arg[1]))

    def _check_and_raise_typing_exception(self, arg_name: str,
                                           expected_type: type,
                                           actual_type: type):
        """Compare the expected type and the actual type of the method 
        argument.

        Args:
            arg_name: The name of the argument, used for TypingException.
            expected_type: The expected type.
            actual_type: The actual type.

        Raises:
            TypingException: if some type of method argument is mismatch.

        """

        if expected_type == _empty or actual_type == type(None):
            return

        if expected_type != actual_type:
            raise TypingException(arg_name, expected_type, actual_type)
