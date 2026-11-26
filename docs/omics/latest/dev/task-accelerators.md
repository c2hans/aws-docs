---
source_url: https://docs.aws.amazon.com/omics/latest/dev/task-accelerators.html
---

# Task accelerators in a HealthOmics workflow definition

In the workflow definition, you can optionally specify a GPU accelerator for a task. HealthOmics supports the following accelerator types, along with the instance family that each one uses:

| Accelerator type | Accelerator family |
| --- | --- |
| nvidia-tesla-t4 | G4 |
| nvidia-tesla-a10g | G5 |
| nvidia-l4 | G6 |
| nvidia-l40s | G6e |

HealthOmics places the task on an instance type that matches the accelerator type you specify and the vCPUs and memory configured for your task. For instance sizes, see [Accelerated-computing instances](memory-and-compute-tasks.md#workflow-task-accelerated-computing-instances).

## Predefined accelerator bundles
<a name="task-accelerators-predefined-bundles"></a>

An accelerator bundle is a predefined accelerator value that covers more than one instance family. When you specify a bundle, HealthOmics searches one family at a time and selects an instance type based on available capacity. If more than one family has capacity, HealthOmics gives preference to the lower-cost instance. The `nvidia-t4-a10g-l4` bundle is the exception, and it gives preference to the latest generation available.

| Accelerator bundle | Accelerator families | Search mode | Priority |
| --- | --- | --- | --- |
| nvidia-tesla-t4-a10g | G4 and G5 | Sequential | Lowest cost |
| nvidia-l4-a10g | G5 and G6 | Sequential | Lowest cost |
| nvidia-t4-a10g-l4 | G4, G5, and G6 | Sequential | Latest generation |

Expanded accelerator search, described later on this page, searches several accelerator types at the same time rather than one family at a time.

## Example task configurations
<a name="task-accelerators-examples"></a>

HealthOmics uses the accelerator type, accelerator count, vCPUs, and memory that you request to select an instance type. The following examples show how each value affects placement.

In the following example, the workflow definition specifies `nvidia-l4` as the accelerator:

------
#### [ WDL ]

```
task my_task {
 runtime {
    ...
    acceleratorCount: 1
    acceleratorType: "{{nvidia-l4}}"
 }
 ...
}
```

------
#### [ Nextflow ]

```groovy
process my_task {
 ...
 accelerator 1, type: "{{nvidia-l4}}"
 ...
}
```

------
#### [ CWL ]

```yaml
cwlVersion: v1.2
class: CommandLineTool
requirements:
  ...
  cwltool:CUDARequirement:
      cudaDeviceCountMin: 1
      cudaComputeCapability: "{{nvidia-l4}}"
      cudaVersionMin: "1.0"
```

------

**An exact configuration:** HealthOmics places the task on an instance type that matches the accelerator type, accelerator count, vCPUs, and memory you request. The following WDL task runs on an `omics.g6e.2xlarge` instance, which has 8 vCPUs, 64 GiB of memory, and 1 GPU:

```
task my_task {
   runtime {
      acceleratorType: "nvidia-l40s"
      acceleratorCount: 1
      cpu: 8
      memory: "64 GiB"
   }
}
```

**By accelerator count:** HealthOmics treats the accelerator count as a strict placement requirement, so the number of GPUs takes precedence over the vCPUs and memory you request. The following WDL task requests 4 GPUs with 8 vCPUs and 64 GiB of memory. The smallest `nvidia-l40s` instance type with 4 GPUs is `omics.g6e.12xlarge`, so the task runs on an instance with 48 vCPUs and 384 GiB of memory. When no instance type has exactly the number of GPUs you request, HealthOmics uses the instance type with the next larger number of GPUs.

```
task my_task {
   runtime {
      acceleratorType: "nvidia-l40s"
      acceleratorCount: 4
      cpu: 8
      memory: "64 GiB"
   }
}
```

**Disk-aware placement:** GPU instance types use local NVMe storage for task scratch data. With expanded accelerator search, HealthOmics only selects an instance type whose NVMe storage is at least the `disks` value you set. Without a `disks` value, the following WDL task would run on `omics.g6e.2xlarge`, which has 450 GB of NVMe storage. The 500 GiB request moves the task to `omics.g6e.4xlarge`, which has 600 GB.

```
task my_task {
   runtime {
      acceleratorType: "nvidia-l40s"
      acceleratorCount: 1
      cpu: 8
      memory: "64 GiB"
      omicsMaxCpu: 16
      disks: "500 GiB"
   }
}
```

For more information about local ephemeral storage, see [Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md).

## Expanded accelerator search
<a name="task-accelerators-expanded-search"></a>

With expanded accelerator search, you can specify a list of accelerators compatible with your task. HealthOmics searches for every matching instance type in a Region at the same time and runs the task on one that has capacity. This differs from the approach taken by predefined accelerator bundles, which search one instance family at a time. Expanded accelerator search is available for WDL and Nextflow.

HealthOmics uses expanded search for a task in the following cases:
+ The `acceleratorType` value lists more than one accelerator type or predefined bundle, separated by commas, for example `"nvidia-l4,nvidia-tesla-a10g"`.
+ The task sets `omicsMaxCpu` or `omicsMaxMemory`. HealthOmics then searches every size of the listed accelerator types between your minimum and maximum values, for example `nvidia-l4` with 8–32 vCPUs.

The following WDL task can run on any instance type with one `nvidia-l4` or `nvidia-tesla-a10g` GPU, 8–16 vCPUs, and 32–64 GiB of memory. Four instance types match the request: `omics.g6.2xlarge`, `omics.g6.4xlarge`, `omics.g5.2xlarge`, and `omics.g5.4xlarge`.

```
task align {
   runtime {
      acceleratorType: "nvidia-l4,nvidia-tesla-a10g"
      acceleratorCount: 1
      cpu: 8
      memory: "32 GiB"
      omicsMaxCpu: 16
      omicsMaxMemory: "64 GiB"
      omicsResourceWaitTimeoutInMin: 30
   }
}
```

Expanded search will place your tasks on any matching instance types that have capacity. List only the accelerator types that meet your task's performance requirements. To try accelerator types in a fixed order, or to fall back to CPU, use `omicsResourceFallbackOrder` instead.

For the field reference, validation rules, and Nextflow examples, see [Expanded accelerator search](expanded-accelerator-search.md).

## Choose a placement method
<a name="task-accelerators-placement-methods"></a>

The following table compares the ways that a task can request GPU capacity.

| Method | Task Configuration | How HealthOmics searches | Instance type selected |
| --- | --- | --- | --- |
| Single accelerator type | acceleratorType: "nvidia-l4" | One accelerator type | The smallest size that fits the request |
| Predefined accelerator bundle | acceleratorType: "nvidia-l4-a10g" | One instance family at a time | First available matching instance |
| Expanded accelerator search | A comma-separated acceleratorType, or omicsMaxCpu or omicsMaxMemory | Every matching type and size at the same time | First available matching instance |
| Resource fallback | omicsResourceFallbackOrder | One profile at a time, each up to its wait timeout | The first profile in your order that gets capacity, including an optional final CPU profile |

## Advanced resource configuration
<a name="task-accelerators-fallback"></a>

You can also configure a task to reserve accelerators in your preferred priority order with the `omicsResourceFallbackOrder` directive, which is available for WDL and Nextflow. HealthOmics tries each profile in the order you define until one gets capacity, including an optional final CPU profile.

This is useful in the following scenarios:
+ GPU to GPU fallback – List accelerator types in priority order, for example `nvidia-l40s` first and then `nvidia-l4`.
+ GPU to CPU fallback – Add a final CPU-only profile so that the task completes when no GPU capacity is available in the Region.

Expanded accelerator search is available within a profile. Set a comma-separated list of accelerator types or bundles, `omicsMaxCpu`, or `omicsMaxMemory` in a profile to search several accelerator types or sizes at the same time before HealthOmics moves to the next profile.

For the per-profile field reference, validation rules, and complete WDL and Nextflow examples, see [Advanced resource configuration](advanced-resource-configuration.md).
