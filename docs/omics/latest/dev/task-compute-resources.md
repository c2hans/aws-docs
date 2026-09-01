---
source_url: https://docs.aws.amazon.com/omics/latest/dev/task-compute-resources.html
---

# Task compute and resources
<a name="task-compute-resources"></a>

When you define tasks in a HealthOmics workflow, you specify the compute, memory, and container resources that each task requires. HealthOmics allocates the appropriate instance type for each task based on the resources you request.

In the workflow definition, define the following for each task:
+ **CPU and memory** – The number of vCPUs and amount of memory for standard, compute-optimized, or memory-optimized instances. See [Task resources in a HealthOmics workflow definition](task-resources.md).
+ **Container image** – The Amazon ECR container image for the task. See [Container images for private workflows](workflows-ecr.md).
+ **GPU accelerators** – Optionally, a GPU accelerator type to allocate an accelerated-computing instance (G4, G5, G6, or G6e) for tasks that benefit from GPU processing. See [Task accelerators in a HealthOmics workflow definition](task-accelerators.md).
+ **Custom compute fallback** – Optionally, an ordered list of accelerator types (GPU) to search and execute at run time. HealthOmics tries each accelerator profile in order until one succeeds, enabling graceful fallback from one accelerator type to another or from accelerators to CPU. See [Custom compute and fallback](custom-compute-fallback.md).

**Note**
HealthOmics matches instance types to fit the compute and memory requirements that you specify. If you don't specify any compute or memory requirements, HealthOmics defaults to 1 vCPU and 1 GiB of memory for a CPU instance.

**Topics**
+ [Task resources in a HealthOmics workflow definition](task-resources.md)
+ [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md)
+ [Task accelerators in a HealthOmics workflow definition](task-accelerators.md)
+ [Custom compute and fallback](custom-compute-fallback.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
