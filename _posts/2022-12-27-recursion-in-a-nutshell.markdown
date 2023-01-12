---
layout: post
title:  "Recursion - A superpower "
categories: algorithms
usemathjax: true
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


`add([1,2,3,4,5]) = 1 + add([2,3,4,5]) = 1 + (2 + add([3,4,5]) .....  = 1 + (2 + (3 + (4 + (5 + add([]))))`
what does `add([])` mean here, Ah! the base case. which means the function can simply return zero.

## A more mathematical form

Consider mathematical induction 

lets say you want to prove that the sum of first n natural numbers is <br>
$$ S(n) = 1 + 2 + 3 + .... n = n \frac{(n+1)}2 $$ <br>

We can also prove then <br>
$$ S(k) = S(k - 1) + k $$ <br>

$$ k \frac{(k + 1)}2  = (k - 1)\frac{k} 2 + k$$ <br>
Simplifying this <br>
$$ k \frac{(k + 1)}2  = k^2/2  - k/2 + k$$

The right hand side of the equation is then becomes equal to the left hand side
we proved therefore a recursive relationship in the series

Another thing we need is the value of $$ S(0) $$, in some cases this is trivial (here it is logically zero)
But in some other functions it may be something else.

So for an array of numbers $$ \textstyle{ \sum_{n=1}^N A_i  = \sum_{n=1}^{(N - 1)} A_i + A_N} $$
and for an empty array $$ S([]) = 0 $$ 

## Mathematical hacks for a recursive algorithms

So you may or may not be familiar with the fibonacci series <br>

$$ S(n) = 1, 1, 2, 3, 5 .. $$

<br> 

The recursive relationship would then be <br>

$$ S(n) = S(n - 1) + S(n - 2) $$

Algorithmically this can be calculated recursively or iteratively (you already know which one i prefer) 
the below algorithms find the nth fibonacci number

Recursive
```python
# The array
def fib(n: int):
    if n == 0:
        return 1    
    return fib(n - 1) + fib(n - 2)
```
```python
def fib(n):
    a,b = 1,1
    for i in range(n - 1):
        a,b = b, a + b
    return b

```



Another mathetical tool we can use comes from the world of Digital Signal Processing called the Z transform.

$$ X(z)={Z}\{x[n]\}=\sum _{n=-\infty }^{\infty }x[n]z^{-n} $$

what the Z transform allows is for conversion for digital signal to the unit impulse response

One peculiar and usefule property of this transform is its ability to strip recursive relationships in recursive discrete functions.

$$ Z \{x[n-k]\} = z^{-k} X[z]  $$ <br>

Another useful property  is the inverse Z transform, which you can find below [here](https://en.wikipedia.org/wiki/Z-transform) <br>

Using the two properties we can convert the fibonacci series into a closed form equation

$$ Z\{S[n]\} =  X[z] = z^{-2}X[z] + z^{-1}X[z] + 1 $$ <br> 
given inital conditions of X[0] = 1 and X[1] = 1 <br>
Moving everying on one side and apply an inverse z transform using a partial fractions method we get <br>
$$ S[n] = \frac{1}{\sqrt{5}}((\frac{(1 + \sqrt{5})}2)^n - (\frac{(1 - \sqrt{5})}2)^n) $$ <br>

## But why is recursion so slow ?

Since each function call allocates a stack. Recursive function are often expensive to run and do not do any favours for cache friendliness.

But we have a trick up our sleeves, to use this trick we need to move to a compiled language, I will use C, but most statically compiled functional (keyword here being functional) do this.

take the simple fibnacci function again.

```C
#include "stdio.h"
int fib(int n) {
    if (n == 0){
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}


int main() {
    printf("%d", fib(100));
}
```

instead of compiling to a binary we can use clang to emit the llvm IR, this should let us see what the compiler is doing when trying to optimize this

first lets do a normal compile with no optimization flag 
`clang -S -emit-llvm test.c `
on my machine I can copy the fib function here for more analysis

```
define i32 @fib(i32 %0) #0 {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  %4 = load i32, i32* %3, align 4
  %5 = icmp eq i32 %4, 0
  br i1 %5, label %6, label %7

6:                                                ; preds = %1
  store i32 1, i32* %2, align 4
  br label %15

7:                                                ; preds = %1
  %8 = load i32, i32* %3, align 4
  %9 = sub nsw i32 %8, 1
  %10 = call i32 @fib(i32 %9)
  %11 = load i32, i32* %3, align 4
  %12 = sub nsw i32 %11, 2
  %13 = call i32 @fib(i32 %12)
  %14 = add nsw i32 %10, %13
  store i32 %14, i32* %2, align 4
  br label %15

15:                                               ; preds = %7, %6
  %16 = load i32, i32* %2, align 4
  ret i32 %16
}
```

It seems llvm does what the code is doing with nothing special,
lets try running the compilation with `-O3`
`clang -S -emit-llvm -O3 test.c`

```
define i32 @fib(i32 %0) local_unnamed_addr #0 {
  %2 = icmp eq i32 %0, 0
  br i1 %2, label %13, label %3

3:                                                ; preds = %1, %3
  %4 = phi i32 [ %8, %3 ], [ %0, %1 ]
  %5 = phi i32 [ %9, %3 ], [ 0, %1 ]
  %6 = add nsw i32 %4, -1
  %7 = tail call i32 @fib(i32 %6)
  %8 = add nsw i32 %4, -2
  %9 = add nsw i32 %7, %5
  %10 = icmp eq i32 %8, 0
  br i1 %10, label %11, label %3

11:                                               ; preds = %3
  %12 = add i32 %9, 1
  br label %13

13:                                               ; preds = %11, %1
  %14 = phi i32 [ 1, %1 ], [ %12, %11 ]
  ret i32 %14
}
```
Now it seems to have done something different. It has added a `tail call` attribute to the function call

lets examine the assembly to see what that means, (you can do that by going to [here](https://godbolt.org/)

```assembly
fib:                                    # @fib
        push    rbp
        push    rbx
        push    rax
        test    edi, edi
        je      .LBB0_1
        mov     ebp, edi
        add     ebp, -1
        xor     ebx, ebx
.LBB0_3:                                # =>This Inner Loop Header: Depth=1
        mov     edi, ebp
        call    fib
        add     ebx, eax
        add     ebp, -2
        cmp     ebp, -1
        jne     .LBB0_3
        add     ebx, 1
        jmp     .LBB0_5
.LBB0_1:
        mov     ebx, 1
.LBB0_5:
        mov     eax, ebx
        add     rsp, 8
        pop     rbx
        pop     rbp
        ret
```
This oddly looks like the iterative algorithm for the fibonnacci series (albeit with one extra recursive call)! How did the compiler know to do this ? 

The technique is called tail call optimization and the compiler detects this when a function has its last statement to be a function call. 
This would mean that technically any recursive function which is converted to a tail call style function can be converted to an iterative form and thus does not need to pay the "stack" memory + allocation time cost, while maintaining readability.

There are some caveats though, some algorithms cannot be tail call optimized, so you are stuck with the old algorithm. But its nice to know the compiler has our back when trying to write this type of code.

## Possibly using a queue for a function call ?

By nature the stack is the most natural form for a function and rightly so. A stack conveniently holds the return address to the previous functions state therefore holding the invariant that nested functions return in reverse order or follow the mathematical form of function composition

$$ f(g(x)) = y $$

Another data structure which could be used is a queue, How would a language behave if functions could specify what kind of data structure to use for return addresses ? 
