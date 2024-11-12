# SQL Injection attack

- SQL = Structured Query Language
- Many web applications take user input from a form
- Often this user input is used literally in the construction
of a SQL query submitted to a database.
- SQL four commands
  - SELECT (for printing out the content)
  - DROP TABLE (for deleting tables)
  - INSERT (to add new data to database)
  - UPDATE (to modify data in database)

Examples:

Return full DB:
```
blah' OR 'x'='x
```

Drop the table prodinfo

```
'blah'; DROP TABLE prodinfo; --'
```

### sqlmap

Download guide at: https://sqlmap.org/

"SQL injection scanner." Automates the process of detection and exploitation of SQL injection. 

Example command:

```
python sqlmap.py -u "http://192.168.64.7/index.php?id=1" --batch

```



### Defenses

Use provided functions for escaping strings:
- Many attacks can be thwarted by simply using the SQL string escaping mechanism
  - Instead of ‘ use \’
  - Instead of “ use \”
- Or use mysql_real_escape_string() as the preferred function for this
Not a silver bulllet:
- Consider:
  - SELECT fields FROM table WHERE id = 23 OR 1=1
  - No quotes^

- Check syntax of input for validity
  - Validate dates, names, emails...
  - Consider quates in text such as : "O'Reilly"
- Have length limits on input
- Scan code for INSERT, DROP, etc. 
- Limit DB permissions and segregate users
  - If a user only reads, don't permit write. 
  - Never connect as a DB admin in the application. 
- Bind inputs to variables if possible. 
- Error reporting
