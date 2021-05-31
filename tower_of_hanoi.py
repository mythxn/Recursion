def tower_of_hanoi(n, source="A", auxiliary="B", destination="C"):
    if n == 1:
        print("from", source, "to", destination)
    else:
        tower_of_hanoi(n - 1, source, destination, auxiliary)
        print("from", source, "to", destination)
        tower_of_hanoi(n - 1, auxiliary, source, destination)