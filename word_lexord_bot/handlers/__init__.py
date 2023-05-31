from .commands import (
    send_echo, send_hello, send_info, send_commands
)


list_of_commands = [
    (send_hello, ['start']),
    (send_info, ['help']),
    (send_commands, ['commands']),
    (send_echo, None)
]


__all__ = [
    "lits_of_commands"
]
