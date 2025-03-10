#Project Euler problem 7

def is_prime(n):
  """Check if a number is prime."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
    
  return True
  
def find_nth_prime(n):
    """Find the nth prime number."""
    count = 0
    num = 1
    while count < n:
      num += 1
      if is_prime(num):
        count += 1
    return num
  
def main():
      nth_prime = find_nth_prime(10001)
      print(f"The 10001st prime number is {nth_prime}.")


if __name__ == '__main__':
    main()