class MyClass():
    
    def fatorial(n: int) -> float:
        i = fat = 1
        if n < 0:
            return 0

        while i <= n:
            fat = fat * i
            i = i + 1
        return fat