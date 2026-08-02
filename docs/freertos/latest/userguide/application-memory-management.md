---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/application-memory-management.html
---

# Manage application memory
<a name="application-memory-management"></a>

When applications need memory, they can allocate it from the FreeRTOS heap. FreeRTOS offers several heap management schemes that range in complexity and features. You can also provide your own heap implementation.

The FreeRTOS kernel includes five heap implementations:

**`heap_1`**
Is the simplest implementation. Does not permit memory to be freed.

**`heap_2`**
Permits memory to be freed, but not does coalesce adjacent free blocks.

**`heap_3`**
Wraps the standard `malloc()` and `free()` for thread safety.

**`heap_4`**
Coalesces adjacent free blocks to avoid fragmentation. Includes an absolute address placement option.

**`heap_5`**
Is similar to heap\_4. Can span the heap across multiple, non-adjacent memory areas.
