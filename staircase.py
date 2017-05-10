# Solution for a popular problem about outputting staircase of spaces and hash signs


def print_staircase(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '#' * (i + 1))

# Test
m = 5
print_staircase(m)
