list_of_lists = [
    ["right", 100, "right", 101, "left", 102],
    ["left", 200, "right", 201, "birateral", 203],
    ["right", 300, "birateral", 301, "left", 303]
]

results = []

for lst in list_of_lists:
    R = None
    L = None

    # 最初に出てきた要素を検索し、その値をRかLに代入
    for i in range(len(lst)):
        if lst[i] == "right":
            R = lst[i+1]
            break
        elif lst[i] == "left":
            L = lst[i+1]
            break
        elif lst[i] == "birateral":
            R = lst[i+1]
            L = lst[i+1]
            break

    # 処理済みの要素は削除
    del lst[:i+2]

    results.append((R, L))

for index, (R, L) in enumerate(results, start=1):
    print(f"List {index}:")
    print("R:", R)
    print("L:", L)
    print()