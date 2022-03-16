from donut_generator import create_image


def main():
    print("\nСколько изображений сгенерировать?")
    amount = int(input("-> "))
    for number in range(amount):
        img_num = number + 1
        create_image(img_num)
        print(f"[image#{img_num}][{img_num}/{amount}] - successfully created")


if __name__ == "__main__":
    main()
