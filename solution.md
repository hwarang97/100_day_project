## What does this error "SyntaxError: EOL while scanning string literal" mean?
SyntaxError means error occus while interpreter complie source code to byte code. EOL means 'this is stands for End of Line which means something make error in end of line.' In this case, Omitting dougle quate or closing parenthesis is almost reason.
scanning is can converted to interpreting code. String literal means string which is written in source code. It looks like similar between literal and value. Value is stored in memory, literal is written in source code.

## Why is f-string needed?
When we concatanate string to string using int value, type conversion is needed to avoid type error. It's not handy. But if you use f-string, python implicitly convert int to str type so you don't need to convert it using str() manually.

### print
```python
score = input("What is your score? )
print("Your score is " + str(score))
```

### f-string
```python
score = input("What is your score? )
print(f"Your score is " + {score})
```

