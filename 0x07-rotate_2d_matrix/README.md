# Rotate 2D Matrix

This function `rotate_2d_matrix(matrix)` rotates an `n x n` 2D matrix 90 degrees clockwise.

- **Prototype:** `def rotate_2d_matrix(matrix):`
- **Return:** None (the matrix is edited in-place)
- **Assumptions:** The matrix will have 2 dimensions and will not be empty.

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

Mado-Term$$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
