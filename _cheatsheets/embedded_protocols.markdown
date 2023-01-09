---
layout: post
title:  "Protocols cheatsheet"
categories: cheatsheet
---

----

## I2C
### Architecture

- Serial
- Single ended
- for lower speed ICs to processors/intraboard communication
- Voltage +5 V or +3.3 V
- `7 bit/10 bit` addresses for nodes
- Open collector or opend drain lines
    - __serial data (SDA)__
    - __serial clock (SCL)__
- Can be clock stretched

### Protocol

4 potential modes of operation


 - **Controller (master) transmit**: Controller node is sending data to a target (slave).
 - **Controller (master) receive**: Controller node is receiving data from a target (slave).
 - **Target (slave) transmit**: Target node is sending data to the controller (master).
 - **Target (slave) receive**: Target node is receiving data from the controller (master).

### Timing Diagram 
![alttext](https://vanhunteradams.com/Protocols/I2C/tenbit.png)


### Continue Reading 
 - [A Blog](https://vanhunteradams.com/Protocols/I2C/I2C.html#10-bit-Addressing)
 - [nrf52840](https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.0.pdf#page=428)
 
----










