# Key-Value Python Store
The purpose of this app create a simple key-value store in Python.
All data will be stored in memory for simplicity.
## Run app
```
$ python -m venv venv
(venv) $ pip install -r requirements.txt
(venv) $ python script.py

🐍Welcome to the Simple Storage System!🐍

You can use the following commands:

        BEGIN           🔸 start a new transaction
                SET             Set a key-value pair.
                UNSET           Unset a key
                GET             Get the value associated with a key.
                NUMEQUALTO      Returns the number of keys that are
                                associated with the given value.
        COMMIT          🔸 commit the current transaction.
        ROLLBACK        🔸 rollback the current
                           transaction.
        HELP            🔸 show this help message
        END             🔸 end the program
[13:31:24] DEBUG    Transactions: None                                                                                    script.py:24
Enter the command:  (HELP):
```
## Run Unittest
```
python -m pytest
======================================================== test session starts
platform linux -- Python 3.10.3, pytest-7.1.2, pluggy-1.0.0
plugins: cov-3.0.0
collected 40 items

tests/test_client.py .......                                                                                                   [ 17%]
tests/test_common.py ..................                                                                                        [ 62%]
tests/test_script.py ......                                                                                                    [ 77%]
tests/test_storage.py .........                                                                                                [100%]

========================================================= 40 passed in 0.18s

```
## Alternative
```
$ make test
or
$ make app
```
