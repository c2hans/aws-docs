---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/kernel-mglru-al2023.html
---

# Using Multi-Gen LRU (MGLRU) on AL2023 kernels
<a name="kernel-mglru-al2023"></a>

 The [Multi-Gen LRU](https://docs.kernel.org/admin-guide/mm/multigen_lru.html) is a modern page reclamation algorithm in the Linux kernel, designed to improve memory management performance under memory pressure. It replaces the traditional LRU (Least Recently Used) mechanism used for determining which memory pages to reclaim when the system runs low on memory.

 The traditional LRU mechanism uses a two-list model (active and inactive) to track page usage, which can become inefficient in modern workloads with large working sets. MGLRU replaces this with multiple "generations" of pages, allowing the kernel to make smarter decisions based on finer-grained aging information.

 Benefits of MGLRU include:
+  **Better reclaim decisions:** More accurate identification of cold (unused) pages.
+  **Lower latency and improved throughput:** Especially for workloads with large address spaces or many concurrent processes.
+  **Improved cache retention:** Pages that are used recently are less likely to be evicted prematurely.
+  **Scalable and lock-efficient design:** Performs better on machines with many CPUs.

## Configuration and Tuning
<a name="kernel-mglru-config-2023"></a>

 The kernel configuration `CONFIG_LRU_GEN` is enabled on AL2023 kernels. This compiles in MGLRU but does not enable it by default.

 MGLRU can be enabled and tuned using the `/sys/kernel/mm/lru_gen/enabled` file. The value is a bitmask. *It is recommended to enable all components unless some of them have undesirable side effects.*

| Bit | Components |
| --- | --- |
| 0 | The main switch for the multi-gen LRU. |
| 1 |  Clearing the accessed bit in leaf page table entries in large batches, when MMU sets it (e.g., on x86). This behavior can theoretically worsen lock contention (mmap\_lock). If it is disabled, the multi-gen LRU will suffer a minor performance degradation for workloads that contiguously map hot pages, whose accessed bits can be otherwise cleared by fewer larger batches.  |
| 2 |  Clearing the accessed bit in non-leaf page table entries as well, when MMU sets it (e.g., on x86). This behavior was not verified on x86 varieties other than Intel and AMD. If it is disabled, the multi-gen LRU will suffer a negligible performance degradation.  |
| [yYnN] |  Enable/disable all the components above.  |

 An example of how MGLRU can be enabled:

```
[ec2-user ~]$ echo y >/sys/kernel/mm/lru_gen/enabled
```

 This enables all the components:

```
[ec2-user ~]$ cat /sys/kernel/mm/lru_gen/enabled
0x0007
```
