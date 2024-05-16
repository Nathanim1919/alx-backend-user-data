# 0x00. Personal data
`Back-end`  `Authentification`

!(image)[https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/12/5c48d4f6d4dd8081eb48.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240516%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240516T175330Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0477f866369ce6586df4867069e17022f5ac023eab21619fd241158a1cddf1ba]

## Resources

### Read or watch:

- [What Is PII, non-PII, and Personal Data?](https://intranet.alxswe.com/rltoken/jf71oYqiETchcVhPzQVnyg)
- (logging documentation)[https://intranet.alxswe.com/rltoken/W2JiHD6cbJY1scJORyLqnw]
- (bcrypt package)[https://intranet.alxswe.com/rltoken/41oaQXfzwnF1i-wT8W0vHw]
- ( Logging to Files, Setting Levels, and Formatting)[https://intranet.alxswe.com/rltoken/XCpI9uvguxlTCsAeRCW6SA]


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google:**

- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables



## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions should be type annotated


## Tasks
0. Regex-ing
1. Log formatter
2. Create logger
3. Connect to secure database
4. Check valid password
5. Encrypting passwords
6. Check valid password


### Task 0: Regex-ing
Write a function called `filter_datum` that returns the log message obfuscated:
- Arguments: 
    - `fields`: a list of strings - fields to obfuscate
    - `redaction`: a string - representing by what the field will be obfuscated
    - `message`: a string - log message
    - `separator`: a string - separating all fields in the log message

- The function should use a regex to replace occurrences of certain field values.
- `filter_datum` should return the log message with all of the fields redacted.

```bob@dylan:~$ cat main.py
    #!/usr/bin/env python3
    """
    Main file
    """

    filter_datum = __import__('filtered_logger').filter_datum

    fields = ["password", "date_of_birth"]
    messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))

    bob@dylan:~$
    bob@dylan:~$ ./main.py
    name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
    name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
    bob@dylan:~$
```


## AUTHOR
**_Nathanim Tadele_**