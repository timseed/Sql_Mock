# Mocking Db calls

This is a short test to show 

  - simple Db access
    - create
    - insert
    - query
    
 But I wanted to also develop some tests, especially Database Mocks.
 
 ## DB
 
 This code creates a *sqlite3*, which is placed in the modules installed folder.
 
 The database is called *People.db*, and it has 1 table called *Phone*, which has 2 fields (Name, Dial).
 
 ### Real Query 
 
 This is what the real query looks like.
 
 ```python 

def test_real_query():
    """"
    Do the test Using
    """
    p = People()
    assert p is not None
    assert len(p.query()) == 3
```

### Mock way 1 

This is done with 

```python
from People import People
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
```

### Mock way 2

A slight difference. 

```python
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
```
 
 
I hope this assists you in developing your own tests/mocks.

 ### Why Mock ?
 
 Sometimes testing is slow, need specific values (difficult in real time systems), requires complex infrastructure to be on-line.
 
 ### Is mocking easy ?
 
 Yes, and no.... 
 
 It rather depends how your code has been written, if you are using a non-class delivery mechanism, then Mocks are quite straightforward.
 
 # Testing 
 
 In the **tests/** folder you should see some example tests.
 
 I have "Real" ones that hit the database (sqlite3), and fake/mocked ones, one's that give the data that I want to persist in the tests.
 
 I would suggest that in real-life these could be implemented as two sets of tests.
 
   - Laptop/Test/Quick. I.e. Mocked
   - Real. In the Beta Env.
   
 
 