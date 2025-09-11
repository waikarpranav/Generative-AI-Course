## Lecture 1: Python Syntax & Semantics)

- **Syntax** → rules for arranging symbols/words (structure of code); errors = _syntax errors_
    
- **Semantics** → meaning of code (what it does when run); errors = _logic errors_
    
- **Comments** → single-line (`#`) and multi-line (`""" ... """`, only in `.py` files)
    
- **Case Sensitivity** → `name` ≠ `Name` (different variables)
    
- **Indentation** → Python uses indentation (4 spaces / tab) instead of braces to define code blocks
    
- **Line Continuation** → use `\` to split long statements
    
- **Multiple Statements on One Line** → separate with `;`
    
- **Type Inference** → Python assigns variable type at runtime (dynamic typing)

## Lecture 2: Variables in Python)

- **Variables** → named containers for storing data, created upon assignment (no explicit declaration).
    
- **Declaration & Assignment** → e.g. `age = 32`, `height = 6.1`, `name = "Krish"`, `is_student = True`.
    
- **Naming Conventions**
    
    - Start with letter or `_`
        
    - Can contain letters, numbers, `_`
        
    - Case-sensitive (`name` ≠ `Name`)
        
    - Should be descriptive (`first_name`, not `fn`)
        
- **Variable Types** → int, float, str, bool; determined at runtime (dynamic typing).
    
- **Type Checking & Conversion** → use `type()`, convert with `int()`, `float()`, `str()`, `bool()`.
    
- **Dynamic Typing** → variable type can change during execution.
    
- **Input Function** → `input()` always returns string → convert if needed.
    
- **Example App** → simple calculator (sum, difference, product, quotient).

## Lecture 3:Data Types

#### 🔑 Key Points

- **Definition**: Data types classify data and tell Python how to use it.
    
- **Why Important**:
    
    - Store data efficiently.
        
    - Allow correct operations.
        
    - Prevent errors/bugs.
        
    - Help in memory management.
        
- **Basic Data Types**:
    
    - **Integer (`int`)** → whole numbers (e.g., 35).
        
    - **Float (`float`)** → decimal numbers (e.g., 5.11).
        
    - **String (`str`)** → text (e.g., `"Krish"`).
        
    - **Boolean (`bool`)** → True/False values.
        
- **Errors & Fixes**:
    
    - Adding a string + number causes error.
        
    - Fix with **typecasting** (`str(5)` → `"5"`).
        
- **Advanced Data Types** (to come later): lists, tuples, sets, dictionaries.


## Lecture 4: Python Operators

### 🔹 Introduction

- Operators let us perform **arithmetic, comparison, and logical operations** in Python.
    
- They are essential in every project → without them we can’t do calculations or logic checks.
    

---

### 1️⃣ Arithmetic Operators

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`+`|Addition|`10 + 5`|15|
|`-`|Subtraction|`10 - 5`|5|
|`*`|Multiplication|`10 * 5`|50|
|`/`|Division (float)|`10 / 5`|2.0|
|`//`|Floor Division|`21 // 5`|4|
|`%`|Modulus (remainder)|`10 % 5`|0|
|`**`|Exponentiation|`2 ** 3`|8|

💻 **Example Code**

`a = 10 b = 5  
print("Addition:", a + b) 
print("Subtraction:", a - b)
print("Multiplication:", a * b) 
print("Division:", a / b) 
print("Floor Division:", a // b) 
print("Modulus:", a % b) 
print("Exponentiation:", a ** b)`

---

### 2️⃣ Comparison Operators

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`==`|Equal to|`10 == 10`|True|
|`!=`|Not equal to|`10 != 5`|True|
|`>`|Greater than|`10 > 5`|True|
|`<`|Less than|`10 < 5`|False|
|`>=`|Greater than or equal to|`10 >= 10`|True|
|`<=`|Less than or equal to|`5 <= 10`|True|

💻 **Example Code**

`x = 10 y = 15  
print(x == y)  False 
print(x != y)   True 
print(x > y)    # False 
print(x < y)    # True 
print(x >= y)   # False
print(x <= y)   # True`

⚠️ Works with **strings too** (case-sensitive).

`print("Hello" == "Hello")  # True 
 print("Hello" == "hello")  # False`

---

### 3️⃣ Logical Operators

|Operator|Meaning|Example|Result|
|---|---|---|---|
|`and`|True if both are True|`True and False`|False|
|`or`|True if at least one is True|`True or False`|True|
|`not`|Inverts the value|`not True`|False|

💻 **Example Code**

`x = True y = False  
print(x and y)  # False 
print(x or y)   # True 
print(not x)    # False


## Lecture 5: Python Control Flow – Conditional Statements

### 🌟 Introduction

- Control flow decides **which part of code runs** based on conditions.
- Conditional statements in Python:
    - `if`
    - `else`
    - `elif` (else-if)
    - Nested conditionals
---
### 🟢 `if` Statement

- Checks a condition.
- If `True` → run the block inside.
- If `False` → skip it.

**Example:**

`age = 20 
    if age >= 18:    
        print("You are allowed to vote in the elections")`

👉 Output: `You are allowed to vote in the elections`

---
### 🔵 `else` Statement

- Runs when the `if` condition is `False`.
**Example:**

`age = 16  
    if age >= 18:    
        print("You are eligible for voting") 
    else:     
        print("You are a minor")`

👉 Output: `You are a minor`

---

### 🟣 `elif` Statement (else-if)

- Checks **multiple conditions in order**.
- First match wins, rest are skipped.

**Example:**

`age = 17  
    if age < 13:     
        print("You are a child")
     elif age < 18:    
        print("You are a teenager")
     else:    
         print("You are an adult")`

👉 Output: `You are a teenager`

---

### 🟡 Nested Conditional Statements

- You can put an `if` (or `else`, `elif`) **inside another if**.
- Useful for multi-level checks.

**Example: Check even/odd & positive/negative**

`num = int(input("Enter a number: "))  
    if num > 0:     
        print("The number is positive")   
          if num % 2 == 0:         
            print("The number is even")    
         else:         
            print("The number is odd") 
    else:     
        print("The number is zero or negative")`

👉 Example runs:

- Input: `12` → Positive & Even
- Input: `11` → Positive & Odd
- Input: `-1` → Zero or Negative


## Lecture 6: 🔁 Loops in Python

### 🌟 Introduction
- Loops = repeat a block of code multiple times.
- Types in Python:
    - `for` loop → iterate over sequences (range, string, list, dict, etc.)
    - `while` loop → run until a condition is false

- Loop control statements:
    - `break` → exit loop early
    - `continue` → skip current iteration
    - `pass` → do nothing (placeholder)

- Can also use **nested loops** (loop inside loop).

---
### 🟢 `for` Loop & `range()`

### Syntax:
`for i in range(start, stop, step):    
 print(i)`
### Key Points:
- `range(n)` → generates `0 … n-1`.
- `range(start, stop)` → from start to stop-1.
- `range(start, stop, step)` → can jump forward/backward.

**Examples:**
`for i in range(5):       # 0–4    
    print(i)  
 for i in range(1, 6):    # 1–5   
     print(i)  
for i in range(1, 10, 2):  # odd numbers    
    print(i)  
 for i in range(10, 0, -1): # countdown  
    print(i)`

---
### 🔡 Iterating Over Strings

Strings = collections of characters → can loop directly.

`name = "Krish Nayak" 
 for ch in name:     
    print(ch)`

👉 Output: each letter printed separately.
👦 “It’s like reading a word letter by letter instead of the whole word.”

---
### 🔵 `while` Loop

- Runs **as long as condition is True**.

**Example:**
`count = 0 
while count < 5:  
    print(count)   
    count += 1`

👉 Prints `0 1 2 3 4`.

⚠️ Forgetting to update the variable → infinite loop.
👦 “It’s like saying: keep eating candy until the jar is empty.”

---
### 🟡 Loop Control Statements

### 1. `break` → exit loop completely

`for i in range(10):     
    if i == 5:         
        break   
	print(i)`

👉 Prints `0 1 2 3 4`, then stops.

---
### 2. `continue` → skip current iteration

`for i in range(10):     
    if i % 2 == 0:        
        continue     
    print(i)`

👉 Prints only odd numbers.

---

### 3. `pass` → placeholder (does nothing)

`for i in range(5):    
     if i == 3:       
        pass   # do nothing here   
      print(i)`

👦 “Pass is like a blank page in a notebook – nothing written, but still there.”

---
### 🟣 Nested Loops

Loop inside another loop.

`for i in range(3):    
    for j in range(2):        
        print(f"i = {i}, j = {j}")`

👉 Output pairs `(0,0) (0,1) (1,0) (1,1) (2,0) (2,1)`

👦 “Imagine classrooms (outer loop) and students inside (inner loop). You go class by class, student by student.”

## Lecture 7:🗂️ Python Data Structures – Lists

### 📌 What is a List?
- **Definition**: Ordered, mutable collection of items.
- **Key properties**:
    - Ordered → items have an index (starts at 0).
    - Mutable → items can be changed/updated.
    - Can store **mixed data types** (e.g., int, string, float, bool).

👦 _Think of a list as a backpack: you can put books, snacks, water, or even a toy. You can rearrange or swap items inside anytime._

---
### 🛠️ Creating Lists
```python
empty_list = []  
names = ["Krish", "Jack", "Jacob"]  
mixed = [1, "hello", 3.14, True]
```

- Empty list → `[]`
- Add elements directly inside square brackets.
- Lists can hold different data types.
---
### 🔍 Accessing List Items

- Indexing starts from **0**.
- Negative indexes count from the **end** (`-1` = last item).

```python
fruits = ["apple", "banana", "cherry", "kiwi", "guava"]
print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[-1])  # guava
```

👦 _Imagine seats in a row: first seat is index 0, last seat is -1 if you count backwards._

---
### ✂️ Slicing Lists
```python
print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[1:])    # from index 1 to end
print(fruits[:3])    # from start to index 2
print(fruits[::2])   # every 2nd item
print(fruits[::-1])  # reverse list
```

- `start:stop` → includes start, excludes stop.
- `::step` → skip elements with step size.
---
### 🔄 Modifying Lists
```python
fruits[1] = "watermelon"   # replace banana
```

- Direct assignment replaces items at a given index.
- Slices can also be replaced, but watch out (strings may split character by character).
---
### ⚙️ Common List Methods

| Method         | Use                       | Example                     |
| -------------- | ------------------------- | --------------------------- |
| `append(x)`    | Add at end                | `fruits.append("orange")`   |
| `insert(i, x)` | Add at index              | `fruits.insert(1, "melon")` |
| `remove(x)`    | Remove first occurrence   | `fruits.remove("banana")`   |
| `pop()`        | Remove & return last item | `fruits.pop()`              |
| `index(x)`     | Find index of item        | `fruits.index("cherry")`    |
| `count(x)`     | Count occurrences         | `fruits.count("banana")`    |
| `sort()`       | Sort ascending            | `fruits.sort()`             |
| `reverse()`    | Reverse order             | `fruits.reverse()`          |
| `clear()`      | Remove all items          | `fruits.clear()`            |

👦 _Think of these as magic tricks: add new fruit, throw one away, sort them alphabetically, or empty the basket._

---
### 🔁 Iterating Over Lists

```python
for fruit in fruits:
    print(fruit)

# With index
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
```

- Use `for` loops to go item by item.
- `enumerate()` gives both index and value.

---
### ⚡ List Comprehensions

- **Compact way** to create lists with expressions + conditions.
### Syntax

- Basic: `[expression for item in iterable]`
- With condition: `[expression for item in iterable if condition]`
### Examples
```python
# Squares
squares = [x**2 for x in range(10)]

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
```

👦 _It’s like saying: “Make me a new basket of fruits, but only the red ones” — all in one step._

---
### ⚠️ Common Errors
- `IndexError`: accessing out of range.
- Replacing slice with string → inserts characters individually.
- Infinite loops if using `while` incorrectly.
`

## Lecture 8:🗂️ Python Data Structures – Tuples

### 📌 What are Tuples?
- **Ordered, immutable collection** of items.
- Similar to lists, but **cannot be changed** once created.
- Can contain **mixed data types** (int, float, string, bool, etc.).
- Defined using **round brackets `()`** instead of `[]`.

👦 _Think of a tuple like a **photo album**: once you print the photos and put them in, you can look at them, but you can’t change the photos inside._

🎓 _In industry, immutability prevents accidental data changes. Tuples are widely used when you need **guaranteed fixed data**—like coordinates, dictionary keys, or function return values._

---

### 🛠️ Creating Tuples

```python
# Empty tuples
empty = ()
empty2 = tuple()

# With elements
nums = (1, 2, 3, 4, 5, 6)
mixed = (1, "hello", 3.14, True)

# Converting types
tuple_from_list = tuple([1, 2, 3])
list_from_tuple = list((1, 2, 3))
```

---
### 🔍 Accessing Elements

- Indexing: `t[0]`, `t[-1]`
- Slicing works like lists: `t[1:4]`, `t[::-1]`

```python
nums = (1, 2, 3, 4, 5, 6)
print(nums[0])     # 1
print(nums[-1])    # 6
print(nums[1:4])   # (2, 3, 4)
print(nums[::-1])  # (6, 5, 4, 3, 2, 1)
```

👦 _It’s like picking seats in a movie theater: `0` is the first seat, `-1` is the last seat._

---
### ➕ Tuple Operations

- **Concatenation**: `t1 + t2` → combines tuples.
- **Repetition**: `t * 3` → repeats tuple.

```python
a = (1, 2, 3)
b = ("x", "y")
print(a + b)   # (1, 2, 3, 'x', 'y')
print(a * 3)   # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

---
### 🔒 Immutability

- Tuples **cannot be modified** once created.
- Attempting `t[0] = "new"` → `TypeError`.
- Workaround: convert to list → edit → convert back.

🎓 _This makes tuples safe for multi-threaded environments where shared data must not change._

---
### ⚙️ Tuple Methods

Only 2 main methods:
- `count(x)` → how many times `x` appears.
- `index(x)` → first index where `x` appears.

```python
nums = (1, 2, 3, 4, 1, 1)
print(nums.count(1))   # 3
print(nums.index(3))   # 2
```

---
### 📦 Packing & Unpacking

- **Packing**: Automatically groups values into a tuple.
- **Unpacking**: Assign tuple values to variables.
- Can use `*` for variable-length unpacking.

```python
# Packing
packed = (1, "hello", 3.14)

# Unpacking
a, b, c = packed
print(a, b, c)   # 1 hello 3.14

# Star unpacking
nums = (1, 2, 3, 4, 5, 6)
first, *middle, last = nums
print(first)   # 1
print(middle)  # [2, 3, 4, 5]
print(last)    # 6
```

👦 _Packing is like putting toys into a box; unpacking is like taking them out one by one._

---
### 🔗 Nested Tuples

- Tuples can contain other tuples (like lists inside lists).
- Access with multiple indexes.

```python
nested = ((1, 2, 3), ("a", "b", "c"), (True, False))
print(nested[0])      # (1, 2, 3)
print(nested[1][2])   # 'c'

# Iterating
for sub in nested:
    for item in sub:
        print(item, end=" ")
```

---
### ✅ Use Cases & Conclusion

- Tuples are best when you need:
    - **Fixed data** (e.g., coordinates, RGB values).
    - **Dictionary keys** (lists cannot be keys).
    - **Function returns** (return multiple values).
- Immutable = safer, more predictable.
- Often used in **data pipelines, ML feature storage, configs**.

---



## Lecture 9:🗂️ Python Data Structures – Dictionaries

### 📌 Introduction

- **Dictionaries** = unordered collection of items in **key-value pairs**.
- Keys → must be **unique & immutable** (string, number, tuple).
- Values → can be of **any type** and **mutable**.
- Defined with **curly braces `{}`** or `dict()` constructor.

👦 _Think of a dictionary like a **real-life dictionary**: the word is the key, and the definition is the value._

🎓 _In industry, dictionaries map relationships (user_id → profile, config_name → setting). Key uniqueness ensures **fast lookups** like in NoSQL DBs (MongoDB, Cassandra)._

---
### 🛠️ Creating Dictionaries

```python
# Empty dictionaries
d1 = {}
d2 = dict()

# With values
student = {"name": "Krish", "age": 32, "grade": "A"}

# Duplicate keys → last one overwrites
dup = {"name": "Krish", "name": "Updated"}
print(dup)  # {'name': 'Updated'}
```

⚠️ Keys must be **unique**, otherwise values get **overwritten**.

---
### 🔍 Accessing Elements

- Direct lookup: `dict[key]`
- Safe lookup: `dict.get(key, default)`

```python
print(student["age"])          # 32
print(student.get("grade"))    # A
print(student.get("lastname")) # None
print(student.get("lastname", "Not Available"))  # Not Available
```

---
### ✏️ Modifying Elements

- Dictionaries are **mutable**.
- Add/update: `dict[key] = value`
- Delete: `del dict[key]`

```python
student["age"] = 33
student["address"] = "India"
del student["grade"]
```

---
### ⚙️ Common Methods

- `keys()` → all keys
- `values()` → all values
- `items()` → all key-value pairs (as tuples)
- `copy()` → shallow copy

```python
print(student.keys())    # dict_keys(['name','age','address'])
print(student.values())  # dict_values(['Krish', 33, 'India'])
print(student.items())   # dict_items([('name','Krish'),('age',33)])
```

⚠️ **Shallow Copy vs Reference**

```python
copy_ref = student   # points to same memory
copy_safe = student.copy()  # separate memory
```

---
### 🔁 Iterating Dictionaries

```python
# Keys
for k in student.keys():
    print(k)

# Values
for v in student.values():
    print(v)

# Key-Value pairs
for k, v in student.items():
    print(f"{k} → {v}")
```

---

### 📦 Nested Dictionaries

- Dictionary inside a dictionary.
- Common in **NoSQL databases**.

```python
students = {
  "student1": {"name": "Krish", "age": 32},
  "student2": {"name": "Peter", "age": 35}
}

print(students["student2"]["age"])  # 35
```

Iterating:

```python
for sid, info in students.items():
    print(sid, info)
    for k, v in info.items():
        print(k, v)
```

---
### 🧠 Dictionary Comprehension

- Compact way to build dictionaries.

```python
# Squares
squares = {x: x**2 for x in range(6)}

# Conditional (even squares only)
evens = {x: x**2 for x in range(10) if x % 2 == 0}
```

👦 _Imagine making a multiplication table where the left side is the number (key) and the right side is the answer (value)._

---
### 🏋️ Practice Tasks

1. Create a dictionary for your profile (`name`, `age`, `city`).
2. Add a new key `"hobby"` and update `"age"`.
3. Write a program to count **word frequencies** in a sentence using a dictionary.
4. Create a nested dictionary for `classroom` with multiple students.
5. Rewrite a loop that builds `{x: x**2}` into a dictionary comprehension.

---
👀 Mentor’s Note:  
Dictionaries are **foundational** for data handling in Python. In Generative AI, they underpin:

- **Token mappings** (`word → token_id`)
- **Model configs** (`param_name → value`)
- **Results storage** (`prompt → output`)

👉 Mastering them now will make **JSON handling, API data, and model configs** far easier later.

---


## Lecture 10:🗂️ Python – Functions

### 📌 What is a Function?

- A **function** = block of code that performs a **specific task**.
- Improves: **code reuse, organization, readability**.
- Syntax:
    ```python
    def function_name(parameters):
        """docstring (optional description)"""
        # function body
        return value  # optional
    ```
    

👦 _Think of a function like a **vending machine**: you press a button (call it), it does some work inside (code), and gives you a result (return)._

🎓 _In real-world AI projects, functions structure pipelines (e.g., `load_data()`, `train_model()`, `generate_text()`). Without functions, projects turn into **unmaintainable spaghetti code**._

---
### 📌 Defining & Calling Functions

```python
def even_or_odd(num):
    """Check if number is even or odd"""
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

# Calling
even_or_odd(24)
```

- Indentation is **mandatory**.
- Calling = use `function_name(arguments)`.

---
### 📌 Parameters & Multiple Parameters

```python
def add(a, b):
    """Return sum of two numbers"""
    return a + b

result = add(2, 4)
print(result)  # 6
```

- Functions can take **one or more parameters**.
- `return` sends back a value (not always required).

---
### 📌 Default Parameters

```python
def greet(name="Guest"):
    print(f"Hello {name}, welcome to the Paradise!")

greet("Krish")   # Hello Krish, welcome to the Paradise!
greet()          # Hello Guest, welcome to the Paradise!
```

- If no argument is given → default value is used. 

👦 _Like when you enter a game without setting a username → system calls you “Guest” automatically._

---
### 📌 Variable-Length Arguments

#### Positional Arguments (`*args`)

```python
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4, 5)
```

- Collects arguments into a **tuple**.
- Order matters → “positional.

---
#### Keyword Arguments (`**kwargs`)

```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Krish", age=32, country="India")
```

- Collects arguments into a **dictionary**.
- Passed as **key=value pairs**.

---
####  Combining Both

```python
def show_info(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

show_info(1, 2, 3, name="Krish", city="Bangalore")
```

⚠️ Rule: **Positional args must come before keyword args**.

👦 _Imagine ordering food: first say what items you want (positional), then say extra details like “no onions” (keyword)._

---
### 📌 Return Statement

```python
def multiply(a, b):
    return a * b

result = multiply(2, 3)
print(result)  # 6
```

- Functions can **return single or multiple values**.

```python
def return_many(a, b):
    return a, b, a+b

x, y, z = return_many(2, 3)
print(x, y, z)  # 2 3 5
```

---
### 🏋️ Practice Tasks

1. Write a function `square(num)` that returns the square of a number.
2. Create a `calculator(a, b, operation="add")` function with default operation.
3. Use `*args` to create a function that sums any number of inputs.
4. Use `**kwargs` to build a function `profile(**info)` that prints user details.
5. Write a function returning **multiple values** (e.g., min, max, average of a list).

---
🎓 **Mentor’s Note**:  
Functions are the **building blocks of Python projects**. In Generative AI:

- Wrapping preprocessing in functions (`clean_text()`) keeps experiments organized.
- Default parameters are common in **model APIs** (e.g., `generate(prompt, temperature=0.7)`).
- `*args` and `**kwargs` are heavily used in **libraries like PyTorch & TensorFlow** for flexibility.
- Returning multiple values helps when passing around **metrics, predictions, configs**.
---
### 🗂️ Python – Function Examples

#### 📌 1. Temperature Conversion Function

- Convert between **Celsius ↔ Fahrenheit**.
- Uses `if` / `elif` to check the target unit.
- Returns converted value or `None` if no unit given.

```python
def convert_temperature(temp, unit):
    """Converts temperature between Celsius and Fahrenheit"""
    if unit == "C":
        return (temp * 9/5) + 32   # Celsius → Fahrenheit
    elif unit == "F":
        return (temp - 32) * 5/9   # Fahrenheit → Celsius
    else:
        return None

print(convert_temperature(25, "C"))  # 77.0
print(convert_temperature(77, "F"))  # 25.0
```

👦 Like switching between **miles ↔ kilometers**. You just change units.

🎓 _In ML projects, unit conversions matter in preprocessing (e.g., normalizing temperatures, scaling inputs). Bad conversions = bad models._

---
### 📌 2. Password Strength Checker

- Criteria:
    - ≥ 8 characters
    - At least one **digit**, **uppercase**, **lowercase**, **special character**
- Returns `True` if strong, else `False`.

```python
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(ch.isdigit() for ch in password):
        return False
    if not any(ch.islower() for ch in password):
        return False
    if not any(ch.isupper() for ch in password):
        return False
    if not any(ch in "!@#$%^&*()-_=+[]{};:,.<>?/" for ch in password):
        return False
    return True

print(is_strong_password("Password123!"))  # True
print(is_strong_password("weakpwd"))       # False
```

👦 Think of a password like a **castle defense**: walls (length), guards (uppercase), towers (digits), traps (special chars). Without them, attackers walk in.

🎓 _In production, password strength validation is part of **user authentication systems**._

---
### 📌 3. Shopping Cart – Total Cost

- Input: list of dictionaries (`name`, `price`, `quantity`).
- Output: total cost.

```python
def calculate_total_cost(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total

cart = [
    {"name": "Apple", "price": 0.5, "quantity": 4},
    {"name": "Banana", "price": 0.3, "quantity": 6},
    {"name": "Orange", "price": 0.7, "quantity": 3},
]

print(calculate_total_cost(cart))  # 5.9
```

👦 Like adding up the **bill at a grocery store**.

🎓 _Very close to e-commerce systems (Amazon, Flipkart): every checkout = cart calculation._

---
### 📌 4. Palindrome Checker

- Palindrome = word/string that reads same forward & backward.
- Uses string **slicing** for reverse.

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("aba"))                   # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))                 # False
```

👦 Like a word **mirror**. If it looks the same in the mirror, it’s a palindrome.

🎓 _String reversal logic shows up in NLP tasks (symmetry, text pattern detection)._

---
### 📌 5. Factorial Using Recursion

- Factorial(n) = `n * (n-1) * ... * 1`.
- Recursive function calls itself.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # 120
print(factorial(6))  # 720
```

👦 Like **Russian dolls**: each doll contains a smaller one until you hit the smallest.

🎓 _Recursion is foundational for tree-based algorithms & backtracking problems (e.g., parsing, search)._

---
### 📌 6. Word Frequency in a File

- Reads file & counts each word’s frequency.
- Uses `dict.get()` to increment counts.

```python
def count_word_frequency(file_path):
    word_count = {}
    with open(file_path, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower().strip(".,!?")
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(count_word_frequency("sample.txt"))
```

👦 Like counting how many times each **player’s name** appears in a football match commentary.

🎓 _Word frequency = basic **NLP preprocessing step** (bag-of-words, embeddings, TF-IDF)._

---
### 📌 7. Email Validator (Regex)

- Uses regular expressions to validate email format.

```python
import re

def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None

print(is_valid_email("user@gmail.com"))  # True
print(is_valid_email("not-an-email"))    # False
```

👦 Like checking if a **school ID** has the right format (`name@school.edu`).

🎓 _Regex validation is used in **signup forms, APIs, and data cleaning pipelines**._

---
⚡ Mentor’s Insight:  
Each of these examples isn’t just “toy problems” — they’re **real-world micro-problems**:

- Unit conversion = **data preprocessing**
- Password check = **security**
- Cart total = **transaction systems**
- Palindrome = **string manipulation in NLP**
- Factorial recursion = **algorithmic thinking**
- Word frequency = **text analytics**
- Email validation = **user input validation**
---
###  Lambda Functions (with Map Preview)

### 📌 What is a Lambda Function?

- **Lambda = anonymous function** (function without a name).
- Created using `lambda` keyword.
- Can take **any number of arguments**, but only **one expression**.
- Syntax:
    ```python
    lambda arguments: expression
    ```
- Often used for **short operations** or as input to **higher-order functions** (like `map`, `filter`).

👦 _Think of lambda like a “shortcut math button.” Instead of writing a whole function, you just press one quick button._

🎓 _In real projects, lambdas are used for data preprocessing, sorting, and as compact transformations in pipelines._

---
### 📌 Example 1: Addition

Normal function:
```python
def add(a, b):
    return a + b

print(add(2, 3))  # 5
```

Lambda version:
```python
addition = lambda a, b: a + b
print(addition(5, 6))  # 11
```

---
### 📌 Example 2: Even Number Checker

Normal function:
```python
def is_even(num):
    return num % 2 == 0

print(is_even(24))  # True
```

Lambda version:
```python
is_even_lambda = lambda num: num % 2 == 0
print(is_even_lambda(12))  # True
```

👦 _It’s like asking: “Does this number split into two teams equally?” If yes → even._

---
### 📌 Example 3: Multiple Parameters

Normal function:
```python
def addition(x, y, z):
    return x + y + z

print(addition(12, 13, 14))  # 39
```

Lambda version:
```python
addition_lambda = lambda x, y, z: x + y + z
print(addition_lambda(12, 13, 14))  # 39
```

---
### 📌 Example 4: Lambda with `map()`

- `map(function, iterable)` → applies a function to every element of a list (or other iterable).
- Works perfectly with lambda.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Square each number using map + lambda
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)  # [1, 4, 9, 16, 25, 36]
```

👦 _Like having a “magic square machine” that squares every number in the list automatically._

🎓 _This is a precursor to functional programming → useful in data pipelines (e.g., transforming each row of data)._

---
⚡ **Mentor’s Insight:**
- Don’t overuse lambdas—use them when code becomes **shorter and cleaner**.
- If logic grows beyond one line → use `def` instead (better readability).
- In AI/ML pipelines, lambdas often appear in **data preprocessing, transformations, and functional-style code**.

---

### 🧾 Python – `filter()` Function

#### 📌 What is `filter()`?

- `filter()` constructs an **iterator** from elements of an iterable for which a function returns **True**.
- In plain words → it **filters out items** from a list (or any iterable) based on a **condition**.

👉 Syntax:

```python
filter(function, iterable)
```

- `function` → decides whether to keep an element (`True`) or drop it (`False`).
- `iterable` → list, tuple, dictionary, etc.
---

#### 📝 Example 1: Filtering Even Numbers

```python
def is_even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
result = list(filter(is_even, numbers))
print(result)  # [2, 4, 6, 8, 10, 12]
```

✅ Only even numbers are kept.

---
#### 📝 Example 2: Filter with `lambda`
```python
numbers = [1,2,3,4,5,6,7,8,9]

greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(greater_than_5)  # [6, 7, 8, 9]
```

---
#### 📝 Example 3: Multiple Conditions
```python
numbers = [1,2,3,4,5,6,7,8,9]

# Condition → number is even AND greater than 5
result = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(result)  # [6, 8]
```

---
#### 📝 Example 4: Filtering Dictionaries
```python
people = [
    {"name": "Krush", "age": 32},
    {"name": "Jack", "age": 33},
    {"name": "John", "age": 25}
]

def age_greater_than_25(person):
    return person["age"] > 25

result = list(filter(age_greater_than_25, people))
print(result)
# [{'name': 'Krush', 'age': 32}, {'name': 'Jack', 'age': 33}]
```

---
#### 🎯 When to Use `filter()`?
- ✅ Cleaning data (remove unwanted entries)
- ✅ Extracting items based on conditions
- ✅ Works with lists, tuples, dictionaries, sets

---
#### 🧑‍🏫 Mentor Tip

- **Map vs Filter:**
    - `map()` → transforms **all items**
    - `filter()` → keeps only items that match the **condition**
- Often used together in **data pipelines**.

---
Perfect 🚀 You’ve given me the full transcript of the **Modules & Packages** lecture.  
Now let’s polish it into clean **Obsidian-ready notes** with explanations, examples, and a simple 12-year-old explanation.

---


## Lecture 11:🐍 Python – Modules & Packages

### 📌 What are Modules & Packages?

- **Module** → a Python file (`.py`) that contains code (functions, variables, classes).
- **Package** → a **collection of modules** stored in a folder with a special file `__init__.py`.
- Purpose: **Organize & reuse code** instead of rewriting from scratch.
- Python also provides many **built-in modules** (e.g., `math`, `os`, `datetime`).

---
### 🔹 Using Built-in Modules

#### Example: `math` module
```python
import math

print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793
```

#### Importing specific functions
```python
from math import sqrt, pi

print(sqrt(25))  # 5.0
print(pi)        # 3.141592653589793
```

#### Importing _all_ functions
```python
from math import *

print(sqrt(36))  # 6.0
print(pi)        # 3.141592653589793
```

---

### 🔹 Installing External Packages

Some libraries are not built-in (e.g., NumPy, Pandas).  
Install them using **pip**:

```bash
pip install numpy
```

#### Example: NumPy
```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)  # [1 2 3 4]
```

⚡ `np` here is an **alias** (short name).

---
### 🔹 Creating a Custom Package

#### Step 1: Folder structure
```
package/
│── __init__.py   (special file → makes folder a package)
│── maths.py
```

#### Step 2: Define functions (`maths.py`)
```python
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b
```
#### Step 3: Import in another file
```python
from package.maths import addition, subtraction

print(addition(2, 3))      # 5
print(subtraction(4, 3))   # 1
```
#### Alternative import
```python
from package import maths

print(maths.addition(2, 3))      # 5
print(maths.subtraction(4, 3))   # 1
```

---
### 🔹 Sub-Packages

#### Structure

```
package/
│── __init__.py
│── maths.py
│── subpackage/
    │── __init__.py
    │── mult.py
```

#### `mult.py`

```python
def multiply(a, b):
    return a * b
```

### Importing from a subpackage

```python
from package.subpackage.mult import multiply

print(multiply(4, 5))  # 20
```

---

### 🎯 Key Takeaways

- **Module = file**, **Package = folder of modules**.
- Always include `__init__.py` in a package (even if empty).
- You can import:
    - Whole module (`import math`)
    - Specific functions (`from math import sqrt`)
    - Everything (`from math import *`)
- External libraries need to be **installed** (`pip install package_name`).
- You can create your own **custom modules & packages**.

---
Got it ✅ Let’s turn this lecture into **clear Obsidian notes** with code snippets, explanations, and a simple **12-year-old explanation** at the end.

---

## Lecture 12:🐍 Python Standard Library Overview

### 📌 What is the Standard Library?

- Python ships with a huge set of **built-in modules**.
- These modules help with math, random numbers, file handling, JSON, CSV, dates, regex, and more.
- There are **300k+ external libraries**, but the standard ones cover many everyday needs.
---
### 🔹 1. `array` module
- Used to create arrays with a fixed **type** (all elements must be the same type).

```python
import array

arr = array.array('i', [1, 2, 3, 4])  
print(arr)  # array('i', [1, 2, 3, 4])
```

- `'i'` → type code for integer.
- Ensures **efficient storage** compared to lists.
---
### 🔹 2. `math` module
Common math functions:
```python
import math

print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.141592653589793
```

---
### 🔹 3. `random` module
Generate random numbers & selections.
```python
import random

print(random.randint(1, 10))  
# random integer between 1 and 10

fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))  
# picks a random fruit
```

---
### 🔹 4. `os` module
Work with files & directories.
```python
import os

print(os.getcwd())   # current working directory
os.mkdir("test_dir") # create new folder
```
👉 Assignment: Find how to **create a new file** using `os`.

---
### 🔹 5. `shutil` module
High-level file operations.

```python
import shutil

shutil.copyfile("source.txt", "destination.txt")
```

Copies contents of `source.txt` into `destination.txt`.

---

### 🔹 6. `json` module

Convert between **dictionary ↔ JSON string**.

```python
import json

data = {"name": "Krish", "age": 25}

# Dict → JSON
json_str = json.dumps(data)
print(json_str)        # {"name": "Krish", "age": 25}
print(type(json_str))  # <class 'str'>

# JSON → Dict
parsed = json.loads(json_str)
print(parsed["name"])   # Krish
print(type(parsed))     # <class 'dict'>
```

---

### 🔹 7. `csv` module

Work with CSV files.
#### Writing CSV:

```python
import csv

with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Krish", 32])
```

#### Reading CSV:

```python
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---
### 🔹 8. `datetime` module

Work with dates & times.
```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)  

yesterday = now - timedelta(days=1)
print(yesterday)
```

---
### 🔹 9. `time` module

Control execution timing.
```python
import time

print(time.time())   # current timestamp
time.sleep(2)        # pause program for 2 seconds
print("Done waiting!")
```

---
### 🔹 10. `re` module (Regular Expressions)

Find patterns in text.

```python
import re

pattern = r"\d+"   # one or more digits
text = "There are 123 apples"

match = re.search(pattern, text)
if match:
    print(match.group())  # 123
```

---

### 🎯 Key Takeaways

- Python Standard Library = **ready-made tools** for everyday coding.
- You can:
    - Work with math, random, arrays.
    - Manage files & folders (`os`, `shutil`).
    - Handle data formats (`json`, `csv`).
    - Work with dates & time.
    - Use regex for pattern matching.

---

## Lecture 13:📂 Python File Operations

### 🔹 Introduction

- File handling = working with **text** & **binary** files.
    
- Common tasks:
    - Create a file
    - Write data
    - Read data
    - Append new data
    - Work with line-by-line reading
    
- File modes:
    
    - `"r"` → read
    - `"w"` → write (overwrites file)
    - `"a"` → append
    - `"w+"` → read + write (overwrite existing content)
    - `"rb"` / `"wb"` → read/write binary

---
### 🔹 Reading Files

#### Read entire content
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

⚠️ Error if file doesn’t exist.
#### Read line by line

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # removes newline characters
```

---

### 🔹 Writing Files

#### Overwrite existing file (`w`)

```python
with open("example.txt", "w") as file:
    file.write("Hello World\n")
    file.write("This is a new line\n")
```

⚠️ Old content is erased.

#### Append to file (`a`)

```python
with open("example.txt", "a") as file:
    file.write("Appended line\n")
```

#### Write multiple lines

```python
lines = ["First line\n", "Second line\n", "Third line\n"]

with open("example.txt", "a") as file:
    file.writelines(lines)
```

---

### 🔹 Binary Files

- Used for images, audio, executables.
- Work with **bytes**.

#### Write binary
```python
with open("example.bin", "wb") as file:
    file.write(b"Hello World")
```

#### Read binary

```python
with open("example.bin", "rb") as file:
    data = file.read()
    print(data)
```

---

### 🔹 Copy File (Text Example)

```python
with open("example.txt", "r") as src, open("destination.txt", "w") as dest:
    content = src.read()
    dest.write(content)
```

---

### 🔹 Assignment: Count Lines, Words, Characters

```python
def count_file_stats(filepath):
    with open(filepath, "r") as file:
        text = file.read()
    lines = text.splitlines()
    words = text.split()
    chars = len(text)

    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", chars)

count_file_stats("example.txt")
```

---

### 🔹 Read + Write Mode (`w+`)

- Opens file for **reading + writing**.
- Creates file if it doesn’t exist.
- Overwrites existing content.

```python
with open("example.txt", "w+") as file:
    file.write("Hello World\n")
    file.write("This is a new line\n")
    
    file.seek(0)  # move cursor to start
    content = file.read()
    print(content)
```

---

### 🎯 Key Takeaways

- `"r"`, `"w"`, `"a"`, `"w+"`, `"rb"`, `"wb"` are the most used modes.
- **Always use `with open(...)`** → it closes file automatically.
- `"w"` overwrites, `"a"` appends.
- Use `.seek(0)` to reset cursor before reading again.
- Binary files deal with **bytes**, not text.

---

## Lecture 14:📘 File & Directory Handling with `os` in Python

### 🔑 Key Takeaways

- `os.mkdir()` → Create new directories.
- `os.listdir()` → List files/folders in current directory.
- `os.path.join()` → Safely join paths (works across Windows/Linux/Mac).
- `os.path.exists()` → Check if a file/folder exists.
- `os.path.isfile()` / `os.path.isdir()` → Check if path is a file or directory.

- **Relative path** → Path starting from current directory.
- **Absolute path** → Full path from system root.

- `os.getcwd()` → Get current working directory.
- `os.path.abspath()` → Convert relative path to absolute.

---

### 📝 Detailed Notes

#### 1. Creating Directories
```python
import os  

new_dir = "package"  
os.mkdir(new_dir)  
print(f"Directory {new_dir} created")  
```

📌 Creates a new folder named **package** in the current working directory.

---
#### 2. Listing Files & Folders
```python
items = os.listdir(".")  # "." means current directory
print(items)
```

📌 Outputs a list of files & directories inside the current folder.

---
#### 3. Joining Paths (Cross-Platform Safe)

```python
import os  

dir_name = "folder"  
file_name = "file.txt"  

full_path = os.path.join(dir_name, file_name)  
print(full_path)  # folder/file.txt  

# With current working directory
absolute = os.path.join(os.getcwd(), dir_name, file_name)  
print(absolute)
```

📌 Ensures paths work on **Windows, Mac, and Linux** without errors.

---
#### 4. Checking if a Path Exists

```python
path = "example1.txt"

if os.path.exists(path):
    print(f"The path {path} exists")
else:
    print(f"The path {path} does not exist")
```

---
#### 5. Checking if Path is File or Directory

```python
path = "example.txt"

if os.path.isfile(path):
    print("This is a file")
elif os.path.isdir(path):
    print("This is a directory")
else:
    print("Neither a file nor directory")
```

---
#### 6. Absolute vs Relative Path

```python
rel_path = "example.txt"  
abs_path = os.path.abspath(rel_path)  
print(abs_path)  
```

📌 **Relative Path:** `"example.txt"` (from current folder).  
📌 **Absolute Path:** `C:/Users/.../example.txt` (full location).

---
### 💡 Mentor’s Tips

- **Always use `os.path.join()`** instead of hardcoding `/` or `\` → avoids bugs across OS.
- Use `os.path.exists()` before creating/deleting files → prevents crashes.
- Practice by making a script that:
    1. Creates a folder.
    2. Adds a file inside it.
    3. Checks if file exists.
    4. Prints both relative & absolute paths.

---

### 🧑‍💻 Assignment

**Q1.** Write a program that:

1. Creates a folder called `test_dir`.
2. Inside it, creates a file `hello.txt`.
3. Checks if `hello.txt` exists.
4. Prints both the relative and absolute path of `hello.txt`.

✅ **Solution**

```python
import os  

folder = "test_dir"  
file_name = "hello.txt"  

# Step 1: Create folder
if not os.path.exists(folder):
    os.mkdir(folder)

# Step 2: Create file inside folder
file_path = os.path.join(folder, file_name)
with open(file_path, "w") as f:
    f.write("Hello, world!")

# Step 3: Check if file exists
if os.path.exists(file_path):
    print("File exists!")

# Step 4: Print paths
print("Relative Path:", file_path)  
print("Absolute Path:", os.path.abspath(file_path))
```

---


## Lecture 15:📘 Exception Handling in Python

### 🔑 Key Takeaways

- Exceptions are runtime errors that interrupt normal program flow (e.g. `ZeroDivisionError`, `FileNotFoundError`, `ValueError`, `NameError`).
- Handle exceptions with `try` / `except` to avoid crashes and give helpful messages.
- Use `else` for code that runs only when no exception occurred.
- Use `finally` for cleanup that must run whether or not an error occurred (close files, release connections).
- Prefer catching specific exceptions; avoid bare `except:`. Use `with` for files where possible.

---

### 📝 Detailed Notes

 **What is an exception?**  
An exception is an event that occurs during program execution that disrupts the normal flow — e.g. dividing by zero, missing file, wrong input type.

**Basic try / except**

```python
try:
    a = b   # NameError if b not defined
except NameError as e:
    print("Variable not assigned:", e)
```

**Catching specific exceptions**

```python
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
```

**Multiple except blocks / order matters**

- More specific exceptions must come before broader ones (`Exception`).

```python
try:
    # some code
    pass
except ZeroDivisionError:
    print("Zero division")
except ValueError:
    print("Bad value")
except Exception as e:   # catch-all (put last)
    print("Other error:", e)
```

**Catching multiple types together**

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except (ValueError, TypeError) as e:
    print("Bad input:", e)
```

**Using else**
- `else` runs only if the `try` block did not raise an exception.

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
else:
    print("Result is", result)
```

**Using finally**

- `finally` runs regardless of whether an exception happened (good for cleanup).

```python
try:
    f = open("example.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    # always executed
    try:
        f.close()
    except NameError:
        pass
    print("Cleanup done")
```

**Preferred pattern for file handling** — use `with` (context manager), which handles cleanup for you:

```python
try:
    with open("example.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
# no need to explicitly close
```

**Raising exceptions**

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

**Logging & re-raising**

```python
import logging
try:
    ...
except Exception as e:
    logging.exception("Unexpected error")
    raise  # re-raise if upper layers must also handle it
```

**`locals()` trick used in lecture**

- To check if a local variable (like `file`) exists before accessing it:
    

```python
if 'file' in locals() and not file.closed:
    file.close()
```

---

👶 12-Year-Old Explanation  
Think of your program like a road trip. If a pothole (error) appears, instead of crashing the car, `try` is where you drive and `except` is where you have a spare wheel and fix it so the trip continues. `finally` is like locking the car and saving your luggage at the end — you always do it whether the trip went smoothly or not.

---

💡 Mentor’s Tips

- **Catch specific exceptions** first. Only use `except Exception:` when you really mean “anything else”.
- **Don’t swallow errors** silently — at least log them. Silent `except:` hides bugs.
- Prefer `with open(...)` over manual open/close — it’s safer.
- Use `finally` to release external resources (DB connections, sockets) when not using context managers.
- Test your handlers by intentionally causing errors (divide by zero, pass bad filename).
- Small practice: create an input loop that keeps asking for correct input until valid (robust user-facing code).

Mini practice exercises:

- Turn the division example into a function that keeps asking the user until a valid nonzero integer is provided.
    
- Replace `print` messages with `logging` statements in a real project.
    

---

🧑‍💻 Assignments

Q1. **(From lecture)** Read a file. If the file doesn’t exist, handle the exception and print “File not found.”  
**Solution:**

```python
# Solution Q1
try:
    with open("mydata.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
```

Expected output if file missing:

```
File not found
```

---

Q2. **Mini exercise from lecture**: Program that takes a number from the user and:

- handles division by zero,
- prints a message if the input is not a number,
- prints the result if successful.

**Solution (step-by-step)**:

```python
# Solution Q2
while True:
    try:
        s = input("Enter a nonzero integer (or 'q' to quit): ")
        if s.lower() == 'q':
            print("Bye")
            break
        n = int(s)                   # may raise ValueError
        res = 10 / n                 # may raise ZeroDivisionError
    except ValueError:
        print("Not a valid integer. Try again.")
    except ZeroDivisionError:
        print("Denominator must be nonzero. Try again.")
    except Exception as e:
        print("Unexpected error:", e)
        break
    else:
        print("Result:", res)
        break
```

- If user types `abc` → "Not a valid integer. Try again."
    
- If user types `0` → "Denominator must be nonzero. Try again."
    
- If user types `5` → "Result: 2.0"
    

---

Q3. **(Practical example in lecture)** Read a file and ensure it is closed whether an error occurs or not. Provide both ways: manual try/finally and recommended `with`.

**Solution A (try/finally):**

```python
# Solution Q3a - manual open/close with try/finally
try:
    f = open("example_one.txt", "r")
    data = f.read()
    print("Contents:", data)
except FileNotFoundError:
    print("example_one.txt not found")
finally:
    if 'f' in locals() and not f.closed:
        f.close()
        print("File closed in finally")
```

**Solution B (recommended with):**

```python
# Solution Q3b - recommended
try:
    with open("example_one.txt", "r") as f:
        data = f.read()
        print("Contents:", data)
except FileNotFoundError:
    print("example_one.txt not found")
# no finally needed to close the file
```

---

Q4. **(Best practice)** Write a function that validates age and raises a descriptive exception if invalid, and show how to call it safely.

**Solution:**

```python
# Solution Q4
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    age = set_age(-3)
except (TypeError, ValueError) as e:
    print("Invalid age:", e)
```

Expected:

```
Invalid age: Age cannot be negative
```

---


## Lecture 16:📘 Object-Oriented Programming (OOP): Classes & Objects

### 🔑 Key Takeaways

- **OOP** helps model real-world problems with classes (blueprints) and objects (instances).
- A **class** defines attributes (variables) and methods (functions).
- Objects are created (instantiated) from a class and can have different attribute values.
- `__init__` is the **constructor**, used to initialize attributes when creating objects.
- **Instance variables** = object properties, **instance methods** = object behaviors.
- The **self** keyword allows access to instance variables and methods inside the class.

---
### 📝 Detailed Notes
#### What is a Class?
- A **class** is a blueprint for creating objects.
- It groups **attributes (variables)** and **methods (functions)**.

Example:
```python
class Car:
    pass

# Creating objects (instances)
audi = Car()
bmw = Car()
```

Here, `Car` is the **class**, while `audi` and `bmw` are **objects**.

---
### Instance Variables (Attributes)
- Properties of an object.
- Example: number of windows or doors in a car.

```python
audi.windows = 4
print(audi.windows)  # 4
```

⚠️ Problem: Defining attributes like this is messy — each object may not have the same set of attributes.

---
### The Constructor (`__init__`)
- A **special method** automatically called when an object is created.
- Used to initialize attributes.

Example with a Dog class:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age
```

Creating objects:
```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 4)

print(dog1.name, dog1.age)  # Buddy 3
print(dog2.name, dog2.age)  # Lucy 4
```

---
### Instance Methods
- Define the **behavior** of an object.
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()   # Buddy says Woof!
```

---
### Example: Modeling a Bank Account

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance = {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance = {self.balance}")

    def get_balance(self):
        return self.balance
```

Usage:

```python
account = BankAccount("Crush", 5000)
account.deposit(100)   # 100 deposited. New balance = 5100
account.withdraw(300)  # 300 withdrawn. New balance = 4800
print(account.get_balance())  # 4800
```

---

###  👶 12-Year-Old Explanation

Think of a **class** like a **blueprint for a toy**.

- A blueprint (class) says: _"The toy car will have wheels and windows."_
- Each toy (object) built from that blueprint can look slightly different (Audi has 4 windows, Nano has 2).
- The `__init__` is like the toy factory machine — it sets up each new toy with its parts.
- Methods are like **actions** the toy can do (car can honk, dog can bark, bank account can deposit/withdraw).

---
### 💡 Mentor’s Tips

- Always use `__init__` to define attributes clearly → avoids messy undefined attributes.
- Use **CamelCase** for class names (`BankAccount`, `Dog`) → Python convention
- Don’t overcomplicate — start with attributes, then add methods.
- **Mistake to avoid:** Forgetting `self` in method definitions → `TypeError`.

🔗 Real-world link: Any software system (ATM, shopping cart, video game) is built with OOP — modeling real-world things.

---
### 🧑‍💻 Assignments

**Q1. Create a `Circle` class with attribute `radius`. Add methods to calculate area and circumference.**

✅ Solution:

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

c1 = Circle(5)
print("Area:", c1.area())                # 78.54
print("Circumference:", c1.circumference())  # 31.41
```

---

## Lecture 17:📘 Inheritance in Python

### 🔑 Key Takeaways

- **Inheritance** allows one class (child/derived) to use attributes and methods of another class (parent/base).
- **Single Inheritance** → one child inherits from one parent.
- **Multiple Inheritance** → one child inherits from more than one parent.
- `super()` is used to call parent’s constructor/methods inside the child class.
- Child classes can **add new attributes/methods** beyond what they inherit.

---
### 📝 Detailed Notes

#### 🔹 What is Inheritance?
- A way to reuse code: child classes automatically get methods and attributes of the parent class.
- **Real-world analogy**: children inherit property from parents, not vice versa.

---
### 🔹 Example: Parent Class (Car)

```python
class Car:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def drive(self):
        print(f"The person will drive the {self.engine_type} car")
```

Usage:

```python
car1 = Car(4, 5, "Petrol")
car1.drive()   # Output: The person will drive the Petrol car
```

---
#### 🔹 Example: Child Class (Tesla → Single Inheritance)

```python
class Tesla(Car):   # Tesla inherits Car
    def __init__(self, windows, doors, engine_type, is_self_driving):
        super().__init__(windows, doors, engine_type)   # Call parent constructor
        self.is_self_driving = is_self_driving          # New attribute

    def self_drive_feature(self):
        print(f"Tesla supports self driving = {self.is_self_driving}")
```

Usage:

```python
tesla1 = Tesla(4, 5, "Electric", True)
tesla1.drive()              # From parent class
tesla1.self_drive_feature() # Tesla supports self driving = True
```

---
### 🔹 Multiple Inheritance Example

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Subclasses must implement this method")

class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog(Animal, Pet):   # Multiple inheritance
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says Woof!"
```

Usage:

```python
dog = Dog("Buddy", "Krush")
print(dog.speak())        # Buddy says Woof!
print(dog.owner)          # Krush
```

- **Note**: When methods overlap, Python follows **Method Resolution Order (MRO)** → child’s method > parent’s.
    

---
### 👶 12-Year-Old Explanation

Imagine your **dad has a car** 🚗. You (child) automatically get to use that car without buying a new one.

- This is **single inheritance** → one parent, one child.  
    If your **mom has a pet 🐶** and your dad has a car 🚗, you (child) get both!
- This is **multiple inheritance** → one child, two parents.  
    You can also add your own **new toys/gadgets** 🎮 → child class can add its own features.

---
### 💡 Mentor’s Tips
- Always use `super().__init__()` for cleaner code when inheriting a single parent.
- For multiple inheritance, call each parent explicitly (`Parent.__init__`).
- Don’t overuse inheritance → sometimes **composition (has-a relationship)** is better than inheritance (is-a relationship).
- **Mini exercise**:
    - Create a `Bike` class with `wheels` and `type`.
    - Create an `ElectricBike` class that inherits `Bike` and adds `battery_capacity`.
    - Instantiate and print attributes.

---
### 🧑‍💻 Assignments

#### Q1. Create a class `LibraryItem` with attributes `title` and `author`.

Then create a child class `Book` that inherits `LibraryItem` and adds `pages`.

**Solution:**

```python
class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

book1 = Book("Python 101", "John Doe", 350)
print(book1.title, book1.author, book1.pages)
# Output: Python 101 John Doe 350
```

---

## Lecture 18:📘 Polymorphism in Python

### 🔑 Key Takeaways

- **Polymorphism** = "many forms" → same method name but different implementations.
- Achieved in Python through **method overriding** and **abstract base classes (interfaces)**.
- Allows objects of different classes to be treated as objects of a common superclass.
- Increases flexibility, reusability, and maintainability of OOP code.

---

### 📝 Detailed Notes
#### 🔹 Definition
- Polymorphism lets you perform a **single action in different ways**.
- Example: `speak()` method → Dog says "Woof", Cat says "Meow".

---
#### 🔹 Method Overriding Example

```python
class Animal:
    def speak(self):
        return "Some animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
```

👉 Both Dog and Cat override the same `speak()` method differently.

---
### 🔹 Polymorphism with Functions
```python
def animal_speak(animal):
    print(animal.speak())

animal_speak(dog)  # Woof!
animal_speak(cat)  # Meow!
```

- Same function works on different objects (Dog, Cat).

---
### 🔹 Polymorphism with Shapes Example

```python
class Shape:
    def area(self):
        print("Area of shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

def print_area(shape):
    print(f"Area is {shape.area()}")

rect = Rectangle(4, 5)
circle = Circle(3)

print_area(rect)    # Area is 20
print_area(circle)  # Area is 28.26
```

---
### 🔹 Abstract Base Classes (ABC)

- Interfaces in Python are implemented as **abstract base classes**.
- Force derived classes to implement a certain method.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

car = Car()
bike = Motorcycle()

print(car.start_engine())   # Car engine started
print(bike.start_engine())  # Motorcycle engine started
```

👉 Enforces consistency across subclasses.

---
### 👶 Think of **TV remotes** 📺:

- The **button name** is the same → “Power”.
- But the action depends on the TV brand → one TV may beep, another may flash a light, another may show a logo.  
    That’s **polymorphism** → same action, different results.

---
### 💡 Mentor’s Tips

- Use **polymorphism** when multiple classes share a method name but behave differently.
- Don’t confuse it with **overloading** (same method with different parameters — not natively supported in Python).
- **Method overriding** is the most common way to achieve polymorphism in Python
- Abstract Base Classes are great for **enforcing contracts** in large projects.

---

### 🧑‍💻 Assignments

#### Q1. Create a class `Employee` with method `work()`.Then create child classes `Developer` and `Designer` that override the `work()` method.

**Solution:**

```python
class Employee:
    def work(self):
        return "Working..."

class Developer(Employee):
    def work(self):
        return "Writing code"

class Designer(Employee):
    def work(self):
        return "Designing UI"

dev = Developer()
des = Designer()

print(dev.work())  # Writing code
print(des.work())  # Designing UI
```

---

## Lecture 19:📘 Encapsulation in Python
### 🔑 Key Takeaways

- **Encapsulation** = bundling data (variables) + methods (functions) in one unit (class).
- Uses **access modifiers** → `public`, `protected`, and `private`.
- **Getter** methods → safely access private variables.
- **Setter** methods → safely update private variables (with conditions if needed).
- Prevents accidental misuse of sensitive data, improves security & code maintainability.

---
### 📝 Detailed Notes
#### 🔹 Definition
Encapsulation is the process of:
- Wrapping variables and methods into a single class.
- Restricting direct access to sensitive variables.

👉 Think: controlling **what data is visible** and **how it is modified**.

---
### 🔹 Access Modifiers in Python
1. **Public** → No underscore (`self.name`).
    - Can be accessed anywhere outside the class.
2. **Protected** → Single underscore (`self._name`).
    - Should be accessed **only inside class or subclasses** (not enforced, but convention).
3. **Private** → Double underscore (`self.__name`).
    - Cannot be directly accessed outside the class.
    - Python renames it internally as `_ClassName__variable`.

---
#### 🔹 Public Variable Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # public
        self.age = age        # public

p = Person("Krush", 34)
print(p.name)   # ✅ Accessible
print(p.age)    # ✅ Accessible
```

---
#### 🔹 Private Variable Example

```python
class Person:
    def __init__(self, name, age):
        self.__name = name    # private
        self.__age = age      # private

p = Person("Krush", 34)
print(p.__name)  # ❌ Error
print(p.__age)   # ❌ Error

# Internally, stored as:
print(p._Person__name)  # ✅ Krush
print(p._Person__age)   # ✅ 34
```

⚠️ Accessing `_Person__name` is possible but **bad practice**.

---
#### 🔹 Protected Variable Example (Accessible in subclass)
```python
class Person:
    def __init__(self, name):
        self._name = name   # protected

class Employee(Person):
    def show_name(self):
        return self._name   # ✅ accessible inside subclass

emp = Employee("Krush")
print(emp.show_name())  # Krush
```

---
### 🔹 Getter and Setter Methods

Encapsulation uses **getter** (to read) and **setter** (to update safely).

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age with validation
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")

# Usage
p = Person("Krush", 34)
print(p.get_name())   # Krush
print(p.get_age())    # 34

p.set_age(35)
print(p.get_age())    # 35

p.set_age(-5)         # Age cannot be negative
```

---
### 👶 12-Year-Old Explanation

Imagine a **washing machine** 🧺:
- You only see **buttons** (Start, Pause, Wash).
- You **cannot touch the motor or wires inside** (hidden/private).
- The company allows you to press buttons (**getter/setter**) instead of messing with the insides.

That’s **encapsulation** → hide sensitive stuff, give safe access.

---
### 💡 Mentor’s Tips
- ✅ Always use **getter/setter** for sensitive variables.
- ❌ Don’t directly access private vars like `_Class__var` → bad practice.
- 🔑 Use encapsulation when designing **secure and maintainable** classes (e.g., banking system, login info).
- Real-world analogy: **ATM Machine** 💳
    - You don’t handle cash directly inside the bank vault.
    - You only interact with **buttons & screen (methods)**.

---
### 🧑‍💻 Assignments

#### Q1. Create a `Student` class with private variables `__name` and `__marks`.Add getter and setter methods for both.The setter for marks should ensure marks are between `0` and `100`.

**Solution:**

```python
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

# Usage
s = Student("Pranav", 85)
print(s.get_name(), s.get_marks())  # Pranav 85

s.set_marks(95)
print(s.get_marks())  # 95

s.set_marks(120)      # Invalid marks
```

---

## Lecture 20:📘 Abstraction in Python

### 🔑 Key Takeaways

- **Abstraction** hides complex implementation details and shows only essential features.
- Implemented in Python using **Abstract Base Classes (ABC)** and **abstract methods**.
- Abstract methods are **declared but not implemented** in the base class.
- Child classes **must provide their own implementation** for abstract methods.
- Abstraction reduces **complexity** and improves **code flexibility & reusability**.

---
### 📝 Detailed Notes
#### 🔹 What is Abstraction?
- Concept of **hiding how something works internally**, while exposing only **what it does**.
- Reduces programming complexity → focus on usage, not implementation.
- **Examples**:
    - Washing machine → you press buttons, but don’t see the inner motor process.
    - Mobile phone → you tap "call", but don’t see signal transmission logic.
    - Laptop → "Shut down" button hides OS-level cleanup processes.

---
### 🔹 Abstract Classes and Methods

- Abstract classes: created using `ABC` module.
- Abstract methods: defined but **no implementation** (empty body).
- Child classes that inherit from the abstract class **must implement** these methods.

---
#### 🔹 Example Code

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving.")

    @abstractmethod
    def start_engine(self):
        pass  # Abstract method (no implementation)

# Child class implementing the abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

# Function to operate vehicle
def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

# Usage
car = Car()
operate_vehicle(car)
```

**Output:**

```
Car engine started.
The vehicle is used for driving.
```

---

### 👶 12-Year-Old Explanation

Think of a **TV remote** 📺:
- You see buttons (power, volume, channel).
- When you press them, things happen → TV turns on, sound changes.
- But you don’t see the **circuit boards or signals** inside.

👉 That’s abstraction: you use simple buttons, while the **complicated wiring is hidden**.

---
### 💡 Mentor’s Tips

- ✅ Use **abstraction** to design flexible code frameworks.
- ❌ Don’t put implementation details in the abstract class.
- 🔑 Abstract methods = a **contract** → every subclass must follow it.
- **Industry example**: Payment gateways.
    - Abstract method: `process_payment()`.
    - Child classes: implement for `CreditCard`, `PayPal`, `UPI`.


---
### 🧑‍💻 Assignments

#### Q1. Create an abstract class `Animal` with an abstract method `make_sound()`.Implement `Dog` and `Cat` classes that override `make_sound()` differently.

**Solution:**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Woof!
print(cat.make_sound())  # Meow!
```

---
Perfect 🙌 Thanks for sharing the full transcript of the **Magic Methods** lecture.  
Here’s the **complete Obsidian note** in your finalized template:

---

## Lecture 21:📘 Magic Methods (Dunder Methods) in Python

### 🔑 Key Takeaways
- Magic methods = **dunder methods** (start & end with `__`).
- They define how objects behave with **built-in operations** (arithmetic, comparison, printing, etc.).
- Examples:
    - `__init__`: constructor, runs when object is created.
    - `__str__`: defines string representation (user-friendly).
    - `__repr__`: official string representation (debugging).

- Default implementations exist, but you can **override them** for custom behavior.
- Helps in **operator overloading** and customizing how objects interact.

---
### 📝 Detailed Notes
#### 🔹 What are Magic Methods?
- Special methods in Python surrounded by **double underscores**.
- Automatically invoked by Python when certain operations are performed.
- Purpose: make classes behave like **built-in types**.
---
### 🔹 Common Magic Methods

1. **`__init__`** → constructor, initializes object.
2. **`__str__`** → user-readable string (used in `print()`).
3. **`__repr__`** → developer-readable string (used in debugging/console).
4. Many more: `__add__`, `__len__`, `__eq__`, etc.

---
#### 🔹 Example 1: Basic Magic Methods
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Object creation calls __init__
p1 = Person("Krish", 34)
print(p1)  # Default output: <__main__.Person object at 0x000...>
```

---
#### 🔹 Example 2: Overriding `__str__`
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p1 = Person("Krish", 34)
print(p1)
```

**Output:**
```
Krish, 34 years old
```

---
#### 🔹 Example 3: Overriding `__repr__`
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p1 = Person("Krish", 34)
print(repr(p1))
```
**Output:**
```
Person(name='Krish', age=34)
```

---
#### 🔹 Key Difference between `__str__` and `__repr__`
- `__str__`: readable for **users**.
- `__repr__`: readable for **developers/debugging**.
- If `__str__` is missing, Python falls back to `__repr__`.

---
### 👶 12-Year-Old Explanation
Imagine your **school report card**:
- On the **cover page**, it just says:  
    _"Pranav, Class 10"_ → this is like `__str__` (simple, user-friendly).
- Inside the **teacher’s file**, it says:  
    _"Student(name='Pranav', age=15, grade='A')"_ → this is like `__repr__` (detailed, for official use).

👉 Magic methods are just **hidden shortcuts** that let you decide how your object should look/behave in different situations.

---
### 💡 Mentor’s Tips
- ✅ Always implement `__repr__` in custom classes → makes debugging easier.
- ✅ Use `__str__` when you want user-friendly display.
- ❌ Avoid unnecessary overriding → only override when needed.
- 🔗 Magic methods connect strongly with **operator overloading** (next lecture).

🔎 **Mini Practice Exercise**
- Create a `Book` class.
    - Use `__init__` to set `title` and `author`.
    - Override `__str__` to return `"Title by Author"`.
    - Override `__repr__` to return `"Book(title='...', author='...')"`

---
### 🧑‍💻 Assignments
#### Q1. Create a `Student` class with `__init__`, `__str__`, and `__repr__`.`__str__` should print → `"Student Name: X, Age: Y"`.`__repr__` should print → `"Student(name='X', age=Y)"`.

**Solution:**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

s1 = Student("Pranav", 19)
print(s1)         # Student Name: Pranav, Age: 19
print(repr(s1))   # Student(name='Pranav', age=19)
```

---
## Lecture 22:📘 Operator Overloading in Python

### 🔑 Key Takeaways

- Operator overloading allows **custom behavior for standard operators** (`+`, `-`, `*`, `==`, `>`, etc.) on user-defined objects.
- Implemented using **magic (dunder) methods**:
    - `__add__` → `+`
    - `__sub__` → `-`
    - `__mul__` → `*`
    - `__truediv__` → `/`
    - `__eq__` → `==`
    - `__gt__` → `>`

- Useful for **mathematical operations on objects** like vectors, matrices, complex numbers, etc.
- Magic methods can be **overridden** to customize object behavior.

---
### 📝 Detailed Notes
### 🔹 What is Operator Overloading?
- Customizes the behavior of standard Python operators for **user-defined classes**.
- Achieved by **overriding corresponding magic methods**.
- Example: adding two vectors using `+` operator.

---
### 🔹 Common Magic Methods for Operator Overloading

| Operator | Magic Method  | Purpose                 |
| -------- | ------------- | ----------------------- |
| `+`      | `__add__`     | Addition                |
| `-`      | `__sub__`     | Subtraction             |
| `*`      | `__mul__`     | Multiplication          |
| `/`      | `__truediv__` | Division                |
| `==`     | `__eq__`      | Equality comparison     |
| `<`      | `__lt__`      | Less than comparison    |
| `>`      | `__gt__`      | Greater than comparison |

---
#### 🔹 Example 1: Vector Addition
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)   # Vector(6, 8)
print(v1 - v2)   # Vector(-2, -2)
print(v1 * 3)    # Vector(6, 9)
print(v1 == v2)  # False
```

---
#### 🔹 How It Works
1. `v1 + v2` → Calls `v1.__add__(v2)` → returns a new `Vector` object.
2. `v1 - v2` → Calls `v1.__sub__(v2)` → returns a new `Vector` object.
3. `v1 * 3` → Calls `v1.__mul__(3)` → scales the vector.
4. `v1 == v2` → Calls `v1.__eq__(v2)` → returns `True` or `False`.
5. `__repr__` gives **developer-friendly string** when printing the object.
    

---
### 🔹 Real-World Analogy

- Think of a **calculator**:
    - `+` for numbers is standard addition.
    - If you give it **matrices or vectors**, it won’t work unless you **teach the calculator how to handle them** → operator overloading.

---
#### 🔹 Assignments / Practice

1. **Complex Numbers**:
    - Implement `__add__`, `__sub__`, `__mul__` for a `ComplexNumber` class.
    - Real + Imaginary operations should follow standard math rules.
2. **Matrix Operations**:
    - Implement `+` and `*` for a `Matrix` class using operator overloading.
3. **Comparison Overloading**:
    - Create a `Student` class.
    - Overload `>` to compare students by marks.
---
#### 🔹 Mentor’s Tips
- ✅ Always implement `__repr__` → makes debugging easier.
- ✅ Use operator overloading only when it **makes sense for your objects**.
- ❌ Avoid overloading operators in ways that are **unexpected for users**.

---