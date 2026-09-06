---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/dev-guide-freertos-kernel.html
---

# FreeRTOS kernel fundamentals
<a name="dev-guide-freertos-kernel"></a>

The FreeRTOS kernel is a real-time operating system that supports numerous architectures. The fundamentals of it are ideal for building embedded microcontroller applications. It provides:
+ A multitasking scheduler.
+ Multiple memory allocation options (including the ability to create completely statically-allocated systems).
+ Intertask coordination primitives, including task notifications, message queues, multiple types of semaphore, and stream and message buffers.
+ Support for symmetric multiprocessing (SMP) on multi-core microcontrollers.

The FreeRTOS kernel never performs non-deterministic operations, such as walking a linked list, inside a critical section or interrupt. The FreeRTOS kernel includes an efficient software timer implementation that does not use any CPU time unless a timer needs servicing. Blocked tasks do not require time-consuming periodic servicing. Direct-to-task notifications allow fast task signaling, with practically no RAM overhead. They can be used in most inter task and interrupt-to-task signaling scenarios.

The FreeRTOS kernel is designed to be small, simple, and easy to use. A typical RTOS kernel binary image is in the range of 4000 to 9000 bytes.

For the most up-to-date documentation about the FreeRTOS kernel, see [ FreeRTOS.org](https://freertos.org/). FreeRTOS.org offers a number of detailed tutorials and guides about using the FreeRTOS kernel, including a [FreeRTOS FreeRTOS Kernel Quick Start Guide](https://freertos.org/Documentation/01-FreeRTOS-quick-start/01-Beginners-guide/02-Quick-start-guide) and the more in-depth [ RTOS Implementation](https://freertos.org/Documentation/02-Kernel/05-RTOS-implementation-tutorial/01-RTOS-implementation) in the *FreeRTOS Documentation*.
