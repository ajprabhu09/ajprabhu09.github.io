---
layout: post
title:  "Recursion - A superpower "
categories: algorithms
---

Ever thought about how recursion works, why functions use a stack (why not a queue ?) and how people seemingly are able to weild this super power to solve some problems which at first look like they cant be solved at all.

## The Super Power of Ignorance

In most problems in computer science which use iteration and/or math, the logic or 'meat' of the algorithm is clear as day, take a simple example of adding the elements of an array

```python
# The array
def add(a: list[int]):
    sum = 0 # variable to store the result
    for i in range(len(a)): # iteration
        sum = sum + a[i] # add each element to the
        
    return sum
```
Thats how most algorithms are written, Think about the logic, map out the needed variables, conditions and invariants and translate them into code.

look at this recusive version (albeit recursion is overkill here)

```python
def add(a):
    if not a: 
        return 0    
    return a[0] + add(a[1:]) # what sorcery is this ?!?

```

The code is smaller (a big plus in my opinion) and achieves the same behaviour

a key feature here is that add calls itself with a subset of the problem. 

Its almost as if `add` assume that it is working and simply calls itself for a slightly smaller problem.

Another key feature here is that add not only does that but specifies a base case when a is empty. which would logically be zero ie. the sum of an empty array is 0.

(Note that is implicity handled in the iterative version `range(len([]))` is no iteration at all  but base cases quickly start to get ugly in iterative solutions )

So how does `add` (or the programmer) just go ahead and assume that `add` works without writing add ?

## Down the rabit hole

let take an example `add([1,2,3,4,5])`

arrows signi

`add([1,2,3,4,5]) = 1 + add([2,3,4,5]) = 1 + (2 + add([3,4,5]) .....  = 1 + (2 + (3 + (4 + (5 + add([]))))`
what does `add([])` mean here









