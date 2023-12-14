from typing import Any


class Vector:
    """Very awesome Vector class."""
    @classmethod
    def triple_product(cls, a, b, c) -> float:
        '''scalar and vector product'''
        return a*(b ^ c)

    @classmethod
    def are_complanar(cls, a, b, c) -> bool:
        '''return if vectors are complanar'''
        return Vector.triple_product(a, b, c) == 0

    def __init__(self, *args: Any) -> None:
        '''create vector class'''
        if not len(args):
            self.x, self.y, self.z = 0, 0, 0
        elif len(args) == 1 and isinstance(args[0], int) or \
                isinstance(args[0], float):

            self.x = args[0]
            self.y = args[0]
            self.z = args[0]

        elif len(args) == 3:

            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

        elif isinstance(args[0], list) or isinstance(args[0], tuple):
            self.x, self.y, self.z = args[0][0], args[0][1], args[0][2]

        elif len(args) > 3:
            raise Exception("idk")

    def __abs__(self) -> float:
        '''return |vector|'''
        return self.lenght()

    def lenght(self) -> float:
        '''return |vector|'''
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __str__(self) -> str:
        '''printing vectors coords'''
        return f"{self.x} {self.y} {self.z}"

    def __add__(self, other):
        '''vector + any or vector + vector'''
        if type(other) is Vector:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return Vector(self.x + other, self.y + other, self.z + other)

    def __radd__(self, other):
        '''any + vector'''
        return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        '''vector - any'''
        if type(other) is Vector:
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return Vector(self.x - other, self.y - other, self.z - other)

    def __rsub__(self, other):
        '''any - vector'''
        return Vector(self.x - other, self.y - other, self.z - other)

    def __neg__(self):
        '''vector * (-1)'''
        return Vector(
            self.x * (-1),
            self.y * (-1),
            self.z * (-1),
        )

    def __mul__(self, other):
        '''vector * any'''
        if type(other) is Vector:
            return self.x*other.x + self.y*other.y + self.z*other.z
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        '''any * vector'''
        return Vector(self.x * other, self.y * other, self.z * other)

    def __xor__(self, other):
        '''vectors product'''
        return Vector(
            self.y*other.z-self.z*other.y,
            self.z*other.x-self.x*other.z,
            self.x*other.y-self.y*other.x
        )

    def __or__(self, other) -> bool:
        '''return true if vectors collinear'''
        cross = self ^ other
        return not (cross.x | cross.y | cross.z)


if __name__ == "__main__":
    r = Vector(2, 2, 2)
    t = Vector(2, 2, 2)
    print(r | t)
