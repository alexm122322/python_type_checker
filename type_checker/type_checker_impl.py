from inspect import Signature, _empty, signature
from typing import List

from type_checker.arg_data import ArgData
from type_checker.typing_exception import TypingException


class TypeChecker:
    """Check type for all method arguments

    Args:
        args: Arguments of checking function.
        kwargs: Dictionary arguments of checking function.

    Attributes:
        args (tuple): Arguments of checking function.
        kwargs (dict): Dictionary arguments of checking function.

    """

    def __init__(self, args: tuple, kwargs: dict) -> None:
        self.args = args
        self.kwargs = kwargs

    def check(self, func):
        """Entry point to TypeChecker

        Args:
            func (function): Checking function

        Raises:
            TypingException: if some type of method argument is mismatch.

        """

        sig = signature(func)
        method_args = self._create_method_args(sig)
        self.check_method_args(method_args)

    def ceate_method_args(self, func_sig: Signature) -> List[ArgData]:
        """Create a list of method arguments wich contain name, value and expecting type.

        Args:
            func_sig: Signature of a checking method.

        Returns: 
            Return a list of complex arguments of method.

        """

        result: List[ArgData] = []
        for i, item in enumerate(func_sig.parameters.items()):
            expected_type = item[1].annotation
            arg_name = item[0]

            if i < len(self.args):
                result.append(ArgData(
                    name=arg_name,
                    value=self.args[i],
                    expected_type=expected_type,
                ))
                continue

            arg = self.kwargs.get(arg_name)
            if arg is not None:
                result.append(ArgData(
                    name=arg_name,
                    value=arg,
                    expected_type=expected_type,
                ))

        return result

    def check_method_args(self, method_args: List[ArgData]):
        """Check all method arguments.

        Args:
            method_args: List of method arguments.

        Raises:
            TypingException: if some type of method argument is mismatch.

        """

        for arg in method_args:
            self.check_and_raise_typing_exception(
                arg_name=arg.name,
                expected_type=arg.expected_type,
                actual_type=type(arg.value),
            )

    def check_and_raise_typing_exception(self, arg_name: str, expected_type: type, actual_type: type):
        """Compare the expected type and the actual type of the method argument.

        Args:
            arg_name: The name of the argument, used for TypingException.
            expected_type: The expected type.
            actual_type: The actual type.

        Raises:
            TypingException: if some type of method argument is mismatch.
            
        """

        if expected_type == _empty:
            return

        if expected_type != actual_type:
            raise TypingException(arg_name, expected_type, actual_type)
