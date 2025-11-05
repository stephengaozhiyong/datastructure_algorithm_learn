


def moveDisk(fp, tp):
    print(f"moving disk from {fp} to {tp}\n")

def moveTower(height, fromPole, toPole, withPole):
    if height > 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)


moveTower(5, "A", "B", "C")