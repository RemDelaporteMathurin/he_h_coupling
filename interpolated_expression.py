from scipy.interpolate import interp1d
from fenics import UserExpression


class InterpolatedExpression(UserExpression):
    def __init__(self, data_x, data_y) -> None:
        super().__init__()
        self.interpolated_object = interp1d(
            data_x, data_y, fill_value=0, bounds_error=False
        )

    def eval(self, value, x):
        value[0] = self.interpolated_object(x)
