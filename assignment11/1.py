class MathHelper:
    def __init__(self):
        self.factorial_cache = {}
    
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("error")
        
        if n in self.factorial_cache:
            return self.factorial_cache[n]
        
        if n == 0 or n == 1:
            self.factorial_cache[n] = 1
        else:
            self.factorial_cache[n] = n * self.factorial(n - 1)
        
        return self.factorial_cache[n]
    
