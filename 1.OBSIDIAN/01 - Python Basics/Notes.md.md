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


## Python Operators

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


## Python Control Flow – Conditional Statements

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


## 🔁 Loops in Python

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

## 🗂️ Python Data Structures – Lists

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

## 🗂️ Python Data Structures – Tuples

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

