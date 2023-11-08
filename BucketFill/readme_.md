## README - Bucket Fill Algorithm

### Abstract


The `fill` function is the main contribution of this task. 

Given a 2D image and a seed point, the function fills the region of the image that contains the seed point until it hits boundaries. 

Beyond that, I use `if not - raise error` architecture to regulate the input format.

Secondly, I propose a test function to test if the `fill` function works properly according to different input seed point. I write a random image generation function to compensate the sparsity of the dataset. 

The results shows that the `fill` function works perfectly, and is robust to various types of input. And all cases are passed.  


### Methodology

- **Input**:
  - A 2D nested list representation of an image, where:
    - `0` represents an unfilled pixel.
    - `1` represents a boundary pixel.
  - A 2-element tuple representing the (row, col) coordinates of the seed point to start filling.

- **Output**:
  - A 2D representation of the filled image, where:
    - `0` represents an unfilled pixel.
    - `1` represents a boundary pixel.
    - `2` represents a filled pixel.
  - Mapping
    - `0`: " ",
    - `1`: "*",
    - `2`: "0"
  - Using the mapping method to print the image.
### Method

1. **Recursive Algorithm**: The function uses a recursive approach to fill neighboring pixels until it hits boundaries.
2. **Boundary Handling**: If the seed point is outside of the image or on a boundary pixel, the image remains unchanged.
3. **Deep Copy**: The original image remains unmodified; a filled copy is returned.
4. **Input Regulation**: Check the *value* and *type* of the input tuple. Make sure only the correct input functions: `Tuple`, `int`, `positive number` no more than image size.

### Qualitative Results

```python
image = [
    [1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
seed_point = (1, 1)

filled_image = fill(image, seed_point)
```
----
```
Before filling:
+ - - - - - - - - - +
| *       *       * |
|   *   *   *   *   |
|   * * *   * * *   |
|                   |
+ - - - - - - - - - +

---------------------
After filling:
+ - - - - - - - - - +
| * 0 0 0 *       * |
|   * 0 *   *   *   |
|   * * *   * * *   |
|                   |
+ - - - - - - - - - +
```
#### Other Results
```
Before filling:
+ - - - - - - - - - - - +
|   * * * * * * * * *   |
| *                   * |
| *     *       *     * |
| *   *   *   *   *   * |
| *     *       *     * |
| *                   * |
| *   * * * * * * *   * |
| *   *           *   * |
| *     *       *     * |
| *       * * *       * |
|   * * * * * * * * *   |
+ - - - - - - - - - - - +

-------------------------
After filling:
+ - - - - - - - - - - - +
|   * * * * * * * * *   |
| * 0 0 0 0 0 0 0 0 0 * |
| * 0 0 * 0 0 0 * 0 0 * |
| * 0 *   * 0 *   * 0 * |
| * 0 0 * 0 0 0 * 0 0 * |
| * 0 0 0 0 0 0 0 0 0 * |
| * 0 * * * * * * * 0 * |
| * 0 *           * 0 * |
| * 0 0 *       * 0 0 * |
| * 0 0 0 * * * 0 0 0 * |
|   * * * * * * * * *   |
+ - - - - - - - - - - - +
```
```
Before filling:
+ - - - - - - - - +
|                 |
|                 |
|                 |
| * * * * * * * * |
|                 |
|                 |
|                 |
|                 |
+ - - - - - - - - +

-------------------------
After filling:
+ - - - - - - - - +
| 0 0 0 0 0 0 0 0 |
| 0 0 0 0 0 0 0 0 |
| 0 0 0 0 0 0 0 0 |
| * * * * * * * * |
|                 |
|                 |
|                 |
|                 |
+ - - - - - - - - +
```
```
Before filling:
+ - - - - - - - - - - - - - - - +
|         * * * * *             |
|       *           *           |
|       *             *         |
|     *   *       *   *         |
|     *   *       *     *       |
|     *                 *       |
|       *             *         |
|         * * * * * * *         |
|     * *     *       * *       |
|   *       *         *   *     |
| *     *           *       *   |
| *       * * * * *       *   * |
| *                       *   * |
|   *                   * *   * |
|     * * * * * * * * *     *   |
+ - - - - - - - - - - - - - - - +

-------------------------
After filling:
+ - - - - - - - - - - - - - - - +
| 0 0 0 0 * * * * *             |
| 0 0 0 *           *           |
| 0 0 0 *             *         |
| 0 0 *   *       *   *         |
| 0 0 *   *       *     *       |
| 0 0 *                 *       |
| 0 0 0 *             *         |
| 0 0 0 0 * * * * * * *         |
| 0 0 * *     *       * *       |
| 0 *       *         *   *     |
| *     *           *       *   |
| *       * * * * *       *   * |
| *                       *   * |
|   *                   * *   * |
|     * * * * * * * * *     *   |
+ - - - - - - - - - - - - - - - +
```
```
Before filling:
+ - - - - - - - - - - - - - - - +
|         * * * * *             |
|       *           *           |
|       *             *         |
|     *   *       *   *         |
|     *   *       *     *       |
|     *                 *       |
|       *             *         |
|         * * * * * * *         |
|     * *     *       * *       |
|   *       *         *   *     |
| *     *           *       *   |
| *       * * * * *       *   * |
| *                       *   * |
|   *                   * *   * |
|     * * * * * * * * *     *   |
+ - - - - - - - - - - - - - - - +

-------------------------
After filling:
+ - - - - - - - - - - - - - - - +
|         * * * * *             |
|       * 0 0 0 0 0 *           |
|       * 0 0 0 0 0 0 *         |
|     * 0 * 0 0 0 * 0 *         |
|     * 0 * 0 0 0 * 0 0 *       |
|     * 0 0 0 0 0 0 0 0 *       |
|       * 0 0 0 0 0 0 *         |
|         * * * * * * *         |
|     * *     *       * *       |
|   *       *         *   *     |
| *     *           *       *   |
| *       * * * * *       *   * |
| *                       *   * |
|   *                   * *   * |
|     * * * * * * * * *     *   |
+ - - - - - - - - - - - - - - - +
```

### Potential Application

Imagine you're working with a graphic tool and you have a shape, say a rectangle, which is drawn on the canvas. If you wish to fill the inside of this rectangle with a color, you'd choose the "fill" or "bucket" tool, click inside the rectangle, and see it get filled with the selected color.
