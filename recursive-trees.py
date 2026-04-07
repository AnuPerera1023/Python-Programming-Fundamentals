def tree(branch, level=0):
    if level > 4:
        return
    print(" " * (20 - level * 3) + "🌿" * branch)
    tree(branch + 1, level + 1)
    tree(branch + 1, level + 1)

tree(1)