def rata_rata(data):
    if len(data) == 0:
        return None
    total = sum(data)
    return total / len(data)

print(rata_rata([80, 90, 70]))
print(rata_rata([80, 100]))
print(rata_rata([]))