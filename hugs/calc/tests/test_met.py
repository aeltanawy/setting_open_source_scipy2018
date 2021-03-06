"""Test the `met` module."""

from hugs.calc import get_wind_dir, get_wind_speed

import numpy as np
from numpy.testing import assert_almost_equal, assert_array_almost_equal
import pytest

def test_speed():
    """Test calculating wind speed."""
    u = np.array([4., 2.,0., 0.])
    v = np.array([0.,2., 4., 0.])

    speed = get_wind_speed(u, v)

    s2 = np.sqrt(2.)
    true_speed = np.array([4., 2 * s2, 4., 0.])

    assert_array_almost_equal(true_speed, speed, 4)


def test_scalar_speed():
    """Test wind speed with scalars."""
    s = get_wind_speed(-3., -4.)
    assert_almost_equal(s, 5., 3)


def test_dir():
    """Test calculating wind direction."""
    u = np.array([4., 2., 0., 0.])
    v = np.array([0., 2., 4., 0.])

    direc = get_wind_dir(u, v)

    true_dir = np.array([270., 225., 180., 270.])

    assert_array_almost_equal(true_dir, direc, 4)

#def test_wind_comps_scalar():
#    '''test wind components calculations with scalars.'''
#    u, v = get_wind_components(0, 150)
#    assert_almost_equal(u, -0, 2)
#    assert_almost_equal(v, 6.9282, 2)

#ef test_warning_direction():
#    '''test the arning is required when wind direction > 360.'''
#    with pytest.warning(UserWarning)


#testing if an exception has Raised
