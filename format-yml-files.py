import sys

stdin_fileno = sys.stdin
stdout_fileno = sys.stdout

stdout_fileno.write(stdin_fileno)
