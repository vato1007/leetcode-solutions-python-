class Robot:
    TO_DIR = {
        0: "East",
        1: "North",
        2: "West",
        3: "South"
    }

    def __init__(self, width, height):
        self.moved = False
        self.idx = 0
        self.pos = []
        self.dirs = []

        for i in range(width):
            self.pos.append((i, 0))
            self.dirs.append(0)

        for i in range(1, height):
            self.pos.append((width - 1, i))
            self.dirs.append(1)

        for i in range(width - 2, -1, -1):
            self.pos.append((i, height - 1))
            self.dirs.append(2)

        for i in range(height - 2, 0, -1):
            self.pos.append((0, i))
            self.dirs.append(3)

        self.dirs[0] = 3

    def step(self, num):
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self):
        return list(self.pos[self.idx])

    def getDir(self):
        if not self.moved:
            return "East"
        return Robot.TO_DIR[self.dirs[self.idx]]