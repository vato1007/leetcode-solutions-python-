class Solution:
    def robotSim(self, commands, obstacles):
        obstacle_set = set(map(tuple, obstacles))

        # North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x = 0
        y = 0
        direction = 0

        max_distance = 0

        for command in commands:

            # Turn left
            if command == -2:
                direction = (direction - 1) % 4

            # Turn right
            elif command == -1:
                direction = (direction + 1) % 4

            # Move
            else:
                dx, dy = directions[direction]

                for _ in range(command):
                    nx = x + dx
                    ny = y + dy

                    if (nx, ny) in obstacle_set:
                        break

                    x = nx
                    y = ny

                    max_distance = max(
                        max_distance,
                        x * x + y * y
                    )

        return max_distance