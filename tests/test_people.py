from unittest import TestCase
from unittest.mock import patch, MagicMock
import pytest
from People import People
from pprint import pprint


def test_init():
    """
    Make sure we can access this Object
    :return:
    """
    p = People()
    assert p is not None


def test_real_query():
    """"
    Do the test Using
    """
    p = People()
    assert p is not None
    assert len(p.query()) == 3

#Package.Class.method
@patch('People.People.query')
def test_fake_query(mock_function):
    """"
    Do the test using fake data.
    """
    mock_function.return_value = [('Superman', ' 1'), ('Avengers', '2')]
    p = People()
    assert p is not None

    pprint(p.query())
    print("Hi can be seen with -s flag")
    assert len(p.query()) == 2
    names=[rec[0] for rec in p.query()]
    assert "Superman" in names
    assert "Avengers" in names

#Class.method
@patch.object(People,"query",
              return_value=[('Superman', ' 1'), ('Avengers', '2')])
def test_fake_query2(mock_function):
    """"
    Do the test using fake data.
    Slightly different call than the previous version.
    But with the same result
    """
    #mock_function.return_value = [('Superman', ' 1'), ('Avengers', '2')]
    p = People()
    assert p is not None
    pprint(p.query())
    print("Hi can be seen with -s flag")
    assert len(p.query()) == 2
    names=[rec[0] for rec in p.query()]
    assert "Superman" in names
    assert "Avengers" in names
    assert "tim" not in names


def test_real_query_2():
    """"
    Do the test Using the read Database
    """
    p = People()
    assert p is not None
    assert len(p.query()) == 3

if __name__ == "__main__":
    pytest.main()
