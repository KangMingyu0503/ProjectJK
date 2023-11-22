h, b, c, s = map(int, input().split()) 
storage_space = h * b * c * s / 8 / 1024 / 1024
print(f"{storage_space:.1f} MB")