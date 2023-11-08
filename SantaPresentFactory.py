from collections import deque

materials = deque(int(x) for x in input().split(' '))
magic_levels = deque(int(x) for x in input().split(' '))

crafted = []
presents_table = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
# presents_table = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}


while materials and magic_levels:
    # if magic_levels[0]: proverqva dali ima element za popvane za magic ,ako da popva material
    # ako ne izobshto ne popvi a printi 0, 0lata shte spre popvaneto na magic i
    # shte se mine na sledvashta iteraciq zaradi if not magic:
    # a dori i da nqma element za magic ako imash nula v materials iskash da q mahnesh
    # or not materials[-1]: ako ne e ostanal material ili nai dqsniqt material e nula go popni za da se mahne
    # else 0: inak vurni nula
    # 0 = False , if magic_levels[0]: vrushta True ili False, ako vurne 0 to vaji i za False
    # zatva tezi usloviq proverqvat ednovremenno dali elementa go ima i dali e 0
    material = materials.pop() if magic_levels[0] or not materials[-1] else 0
    magic = magic_levels.popleft() if material or not magic_levels[0] else 0
    if not magic:
        continue

    result = material * magic
    if presents_table.get(result):
        crafted.append(presents_table[result])
    elif 0 < result:
        materials.append(material + 15)
    elif result < 0:
        materials.append(material + magic)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
