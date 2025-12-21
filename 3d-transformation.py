import numpy as np
import matplotlib.pyplot as plt

def translation(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

def scaling(sx, sy, sz):
    return np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])

def rotation_z(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])

point = np.array([1, 2, 3, 1])

S = scaling(2, 2, 2)
R = rotation_z(np.radians(45))
T = translation(3, 4, 5)

# Combine transformations
M = T @ R @ S

# Apply transformation
new_point = M @ point

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Original point
ax.scatter(point[0], point[1], point[2], color='blue', s=60, label='Original Point')

# Transformed point
ax.scatter(new_point[0], new_point[1], new_point[2],
           color='red', s=60, label='Transformed Point')

# Draw a line between them
ax.plot([point[0], new_point[0]],
        [point[1], new_point[1]],
        [point[2], new_point[2]],
        linestyle='dashed', color='gray')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Transformation Visualization')

ax.legend()
plt.show()

print("Original Point:", point[:3])
print("Transformed Point:", new_point[:3])
