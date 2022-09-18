import sys
from typing import NoReturn, Pattern
import re

re_any_str: Pattern = re.compile('.*')
def get_arg_value(arg_name: str, error_explanation: str, re_arg_validator: Pattern = re_any_str) -> str | None | NoReturn:
    COMMAND_LINE_ARGUMENTS: list[str] = sys.argv
    if arg_name in COMMAND_LINE_ARGUMENTS:
        arg_index: int = COMMAND_LINE_ARGUMENTS.index(arg_name)
        try:
            arg_value: str = COMMAND_LINE_ARGUMENTS[arg_index + 1]
            if re_arg_validator.search(arg_value):
                return arg_value
            else:
                raise Exception(f'{arg_value} {error_explanation}')

        except IndexError:
            raise Exception(f'You dont provided a value to "{arg_name}".')
    else:
        return None
    
def verify_exclusive_flag(flags: list[str]) -> str | None | NoReturn:
    COMMAND_LINE_ARGUMENTS: list[str] = sys.argv[1: ]

    flag: str
    for flag in flags:
        if flag in COMMAND_LINE_ARGUMENTS:
            if len(COMMAND_LINE_ARGUMENTS) == 1:
                return flag
            else:
                print(COMMAND_LINE_ARGUMENTS)
                raise Exception(f'{flag} flag must be exclusive.')

def verify_not_many_args(supported_args: list[str]) -> None | NoReturn:

    COMMAND_LINE_ARGUMENTS: list[str] = sys.argv[1: ]
    for index, arg in enumerate( COMMAND_LINE_ARGUMENTS ):
        if arg not in supported_args:
            raise Exception(f'The "{arg}" argument is not supported.')
        else:
            # due to each flag supported must have a value, the element next to the 
            # flag is deleted from the COMMAND_LINE_ARGUMENTS to avoid the function 
            # stop because the value is not a flag
            del COMMAND_LINE_ARGUMENTS[index + 1]


