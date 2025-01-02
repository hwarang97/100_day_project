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

## When do we use list?
List is a collections that keep order. If there are objects and they have relationship, you can store them in list. Also, there are order within items, list is the appreciate collection.
```python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
```
The states is items of america and if you want to store them in some order, list is good choice.
