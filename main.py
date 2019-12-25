import time
import asyncio

def is_prime(x: int) -> bool:
  return not any(x%i==0 for i in range(x-1,1,-1))


async def highest_prime_below(y: int) -> int:
  #print('largest prime under {}'.format(y))
  for x in range(y-1,1,-1):
    if is_prime(x):
      print("high:{} {}".format(y,x))
      return x
    time.sleep(.01)
  return None
    

async def main():
 await asyncio.wait([
   highest_prime_below(10),
   highest_prime_below(10000000),
   highest_prime_below(10000),
   highest_prime_below(100)
  ])

asyncio.run(main())
# loop = asyncio.get_event_loop() 
# loop.run_until_complete(main())