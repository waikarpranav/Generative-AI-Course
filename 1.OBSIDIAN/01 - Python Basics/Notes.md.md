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