---
layout: post
title:  "Clean Bit/Byte Operations in C"
categories: algorithms
usemathjax: true
---

## Motivation

C is a language which most accurately represents the hardware, other assembly ofcourse. But I have often seen code which does not take advantage of the features C provides for bit and byte manipulation. Therefore Im trying to document certain ways of doing operations which utilise the compiler instead of the programmer having to do calculations in your head.

## MMIO structs and padding.

Starting with a classical systems/kernel problem of interfacing with MMIO registers and memory.

### Structs are your friends
Lets say you have a MMIO register at `0xBAADBEEF` and has 4 32 bit from this base address
The "normal way" of doing this is  
```C
#include "stdint.h"
void main() {
    volatile uint32_t* base = (uint32_t*)(0xBAADBEEF);
    *base = 1;
    *(base + 1) = 1;
    *(base + 2) = 1;
    *(base + 3) = 1;
}
```
This is a perfectly fine way of doing this. The disadvantage is that now the programmer has to explicitly write the MMIO register offsets. Additionaly this API is not extensible to multiple instances of the same peripheral. And finally any mistake in the offset leads to unexpected behaviour which is difficult to debug as the state of the whole peripheral cannot be printed in GDB.

An arguable better way
```C
typedef struct {
    volatile uint32_t A;
    volatile uint32_t B;
    volatile uint32_t C;
    volatile uint32_t D;
} mmio_peripheral_t;

void main() {
    mmio_peripheral_t* p1 = (mmio_peripheral_t*) (0xBAADBEEF);
    p1->A = 1;
    p2->B = 1;
    p2->C = 1;
    p3->D = 1;
}
```
Note the volatile keyword everywhere since we don't want write-back caches to cause a write only if a cache eviction occurs but a immediate write to the memory location.

The above code is more readable. `ABCD` can represent command registers in the peripheral and can be named so. The compiler automatically calculates offset based on the type of the members. (Note that we must be careful here to mix 32 bit types and 64 bit types on 64 bit systems, which may get aligned to 64 bits and lead to unexpected behaviour, to ensure this,a compile-time assertion on the size and alignment of the struct can be done).
Another instance of the same peripheral can be instantiated in a similar way without having to rewrite any existing code.
This struct can even be printed using GDB!








