#the code given below  will result in  error  
#library.foo is inconsistent, runtime argument "x" has a default value but stub argument does not...
#error: library.x variable differs from runtime type Literal['hello, stubtest']


# x: int
# def foo(x: int) -> None: ...

#chnaging the code to the code given below will give correct ouput


from typing import Optional
x: str
def foo(x: Optional[int] = None) -> None: ...


#check the code by running : "python -m mypy.stubtest library" in the correct directory
