---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/software-timers.html
---

# Software timers
<a name="software-timers"></a>

A software timer allows a function to be executed at a set time in the future. The function executed by the timer is called the timer’s *callback function*. The time between a timer being started and its callback function being executed is called the timer’s *period*. The FreeRTOS kernel provides an efficient software timer implementation because:
+ It does not execute timer callback functions from an interrupt context.
+ It does not consume any processing time unless a timer has actually expired.
+ It does not add any processing overhead to the tick interrupt.
+ It does not walk any link list structures while interrupts are disabled.
