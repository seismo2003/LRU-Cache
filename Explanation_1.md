Explanations on problem 1 - LRU

I applied hash_map concept I learned in the course to maintain a constant length
cache. Once the maximum cache is reached, the least frequent used file will be removed.
I used a linkedlist to make this operation more easier, once a piece of data is
accessed or created, it will be moved to the head automatically, which left the
tail with the least frequent used data. This allow us to easily remove the LRU
and maintain the maximum cache.

The run time will be O(1), since I used a hashmap to quick look up the linkedlist's
node and there's no iteration through out the entire code.

Space complexity of LRU will be: O(capacity)
