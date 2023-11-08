from bucket_fill import fill, load_image, show_image
import random
pattern = [
    (0, 0),
    (-1, 0),
    (-100000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000),
    (0.5, 0.5),
    ('x', 1),
    (1, 2),
    (5, 5),
    (25, 25),
    (10, 10),
    (100, 100),
    (4, 5),
    [5, 5],
    {1:5, 2:10}
]

def generate_test_image():
    n = random.randint(1, 25)

    image = [[random.randint(0, 1) for i in range(n)] for j in range(n)]
    print(image)
    return image

def test_pattern():
    image = generate_test_image() # load_image('test_image.txt')
    print(image)
    print("--------------------")
    print('Testing...')
    for i in pattern:
        try:
            filled_image = fill(image, seed_point=i)
            if filled_image == image:
                print('Test Passed and Keep Original Image')
            else:
                print('Test passed')
        except:
            print('Test failed')
    image = fill(image=image, seed_point=(-1, 7))

    print("-" * 25)
    print("After filling:")
    show_image(image)


if __name__ == '__main__':
    # This is just an example. Feel free to change this to whatever suits you.
    test_pattern()
