size = 7
m = [[0] * size for _ in range(size)]
start = size // 2
total = size * size
current = 1

i = j = start
direction = 0
current_leg_length = 1
leg_length_now = 0
current_leg_count = 0

while current <= total:
    m[i][j] = current
    current += 1
    leg_length_now += 1

    if direction == 0:
        j -= 1
    elif direction == 1:
        i += 1
    elif direction == 2:
        j += 1
    else:
        i -= 1

    if leg_length_now == current_leg_length:
        leg_length_now = 0
        direction = (direction + 1) % 4

        if current_leg_count == 1:
            current_leg_length += 1
            current_leg_count = 0
        else:
            current_leg_count += 1

for i in range(size):
    print(m[i])
