---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/smp-support.html
---

# Symmetric multiprocessing (SMP) support
<a name="smp-support"></a>

[SMP support in the FreeRTOS Kernel](https://freertos.org/symmetric-multiprocessing-introduction.html) enables one instance of the FreeRTOS kernel to schedule tasks across multiple identical processor cores. The core architectures must be identical and share the same memory.

The FreeRTOS API remains substantially the same between single-core and SMP versions, except for [these additional APIs](https://freertos.org/symmetric-multiprocessing-introduction.html#smp-specific-apis). Therefore, an application written for the FreeRTOS single-core version should compile with the SMP version with minimal to no effort. However, there might be some functional issues, because some assumptions that were true for single-core applications might no longer be true for multi-core applications.

One common assumption is that a lower priority task can't run while a higher priority task is running. While this was true on a single-core system, it's no longer true for multi-core systems because multiple tasks can run simultaneously. If the application relies on relative task priorities to provide mutual exclusion, it might observe unexpected results in a multi-core environment.

One other common assumption is that ISRs can't run simultaneously with each other or with other tasks. This is no longer true in a multi-core environment. The application writer needs to ensure proper mutual exclusion while accessing data shared between tasks and ISRs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
