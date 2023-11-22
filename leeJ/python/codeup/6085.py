w, h, b = map(int, input().split())
storage_space = w * h * b / 8 / 1024 / 1024
print(f"{storage_space:.2f} MB")