---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/kernel-memory-allocation.html
---

# Kernel memory allocation
<a name="kernel-memory-allocation"></a>

The RTOS kernel needs RAM each time a task, queue, or other RTOS object is created. The RAM can be allocated:
+ Statically at compile time.
+ Dynamically from the RTOS heap by the RTOS API object creation functions.

When RTOS objects are created dynamically, using the standard C library `malloc()` and `free()` functions is not always appropriate for a number of reasons:
+ They might not be available on embedded systems.
+ They take up valuable code space.
+ They are not typically thread-safe.
+ They are not deterministic.

For these reasons, FreeRTOS keeps the memory allocation API in its portable layer. The portable layer is outside of the source files that implement the core RTOS functionality, so you can provide an application-specific implementation appropriate for the real-time system you're developing. When the RTOS kernel requires RAM, it calls `pvPortMalloc()` instead of `malloc()`(). When RAM is being freed, the RTOS kernel calls `vPortFree()` instead of `free()`.
