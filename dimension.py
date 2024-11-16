def find_dimensions(base_height=8, max_height=1000, ratio=0.76):
    for height in range(base_height, max_height + 1, 8):  # Increment by 8 for divisibility
        width = round(ratio * height / 8) * 8  # Round to nearest multiple of 8
        if width % 8 == 0:
            print(f"Height: {height}, Width: {width}, Ratio: {width / height:.2f}")

find_dimensions()