import numpy as np


def is_collinear(p1, p2, p3):
    # make vectors out of the points
    vec1 = p2-p1
    vec2 = p3-p1
    # transform the vec1 to matrix (for the cross product between the two vectors)
    # so vec1 X vec2 => vec1x dot vec2
    vec1x = np.array([[0, -vec1[2], vec1[1]], [vec1[2], 0, -vec1[0]], [-vec1[1], vec1[0], 0]])
    line = vec1x.dot(vec2)
    # the cross product of two collinear vector is 0 (sin(0))
    return np.sum(np.abs(line))


def point_input():
    print('put 3 numbers to set the 3d point')
    point = list()
    for j in range(3):
        n = input('')
        point.append(int(n))
    return np.array(point)


if __name__ == '__main__':
    point1 = point_input()
    point2 = point_input()
    point3 = point_input()
    if is_collinear(point1, point2, point3) == 0:
        print('the points are collinear')
    else:
        print('the point are not collinear')
