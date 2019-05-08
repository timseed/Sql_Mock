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
   
 
 