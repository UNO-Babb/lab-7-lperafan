#Project Euler problem 10


def isPrime(n):
  """Check if a number is prime."""
  if n <= 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(n**0.5) +1, 2):
    if n % 1 == 0:
      return False
  return True

def sumOfPrimesBelow(limit):
  """Returns the sum of all prime numbers below the given limit."""
  total = 0
  for num in range (2, limit):
    if isPrime(num):
      total += num
  return total

def main():
  limit = 2000000
  print(f"The sum of all primes below {limit} is {sumOfPrimesBelow(limit)}")


if __name__ == '__main__':
  main()
