---
source_url: https://docs.aws.amazon.com/omics/latest/dev/expanded-accelerator-search.html
---

# Expanded accelerator search

With expanded accelerator search, you can search multiple accelerator types and instance sizes by specifying the range of vCPUs and memory that a task can use. When you specify a comma-separated list of accelerator types or bundles, HealthOmics searches every matching instance type in the Region at the same time. The task runs on a matching instance type that has capacity. Use a predefined accelerator bundle or an `omicsResourceFallbackOrder` list to try one family or profile at a time. Expanded accelerator search is available for WDL and Nextflow.

Use expanded search when your task can run on several accelerator types or instance sizes without changes to its command.

## How it works
<a name="expanded-accelerator-search-how-it-works"></a>

Expanded accelerator search places a task as follows:

1. You list one or more accelerator types, the number of GPUs, and the minimum and maximum vCPUs and memory for the task.

1. HealthOmics finds every instance type in the Region that matches, including any `disks` requirement you set. If no instance type has exactly the number of GPUs you request, HealthOmics uses the instance types with the next larger number of GPUs.

1. HealthOmics requests capacity across all matching instance types in a single search. The search repeats until an instance launches or the wait timeout ends.

1. The task runs on the instance type that launched. If HealthOmics doesn't find capacity within the wait timeout, the task fails with reason `INSTANCE_RESERVATION_FAILED`.

## Field reference
<a name="expanded-accelerator-search-fields"></a>

Expanded accelerator search uses the following fields in addition to the standard task resource fields. Set `acceleratorCount` (required, at least 1), `cpu` (WDL) or `cpus` (Nextflow), and `memory` as you would for any GPU task. These values set the minimums. For more information, see [Task accelerators in a HealthOmics workflow definition](task-accelerators.md).

The following table describes the expanded search fields.

| Field | Type | Default when omitted | Notes |
| --- | --- | --- | --- |
| acceleratorType | String | Required | A comma-separated list of accelerator types, for example "nvidia-l4,nvidia-tesla-a10g". A predefined accelerator bundle, such as nvidia-l4-a10g, adds each of its accelerator types to the list. |
| omicsMaxCpu | Integer | No upper limit | The maximum number of vCPUs. Must be at least the minimum vCPUs. |
| omicsMaxMemory | String, in the same format as memory | No upper limit | The maximum memory. Must be at least the minimum memory. |
| omicsResourceWaitTimeoutInMin | Integer | 20 minutes | How long HealthOmics searches for capacity before the task fails. The allowed range is 20–10080 minutes (7 days). HealthOmics sets a value below 20 to 20 and a value above 10080 to 10080, and writes a warning to the run log. |

A task with a single accelerator type and `omicsMaxCpu` or `omicsMaxMemory` also uses expanded search. If a task lists several accelerator types and omits both maximums, HealthOmics searches every size at or above your minimums. Without either field, a single accelerator type works as described in [Task accelerators in a HealthOmics workflow definition](task-accelerators.md).

In Nextflow, set the accelerator types and number of GPUs with the `accelerator` directive, for example `accelerator 1, type: 'nvidia-l4,nvidia-tesla-a10g'`, and set `omicsMaxCpu`, `omicsMaxMemory`, and `omicsResourceWaitTimeoutInMin` as process directives. To use expanded search inside `omicsResourceFallbackOrder`, set these fields in a profile rather than at the task level. For an example, see [Use expanded search in a fallback profile](#expanded-accelerator-search-fallback).

## Examples
<a name="expanded-accelerator-search-examples"></a>

### Search multiple accelerator types
<a name="expanded-accelerator-search-multiple-types"></a>

The following task can run on any instance type with one `nvidia-l4` or `nvidia-tesla-a10g` GPU, 8–16 vCPUs, and 32–64 GiB of memory.

------
#### [ WDL ]

```wdl
task align {
    runtime {
        docker: "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-gpu-tool:1.0"
        acceleratorType: "nvidia-l4,nvidia-tesla-a10g"
        acceleratorCount: 1
        cpu: 8
        memory: "32 GiB"
        omicsMaxCpu: 16
        omicsMaxMemory: "64 GiB"
        omicsResourceWaitTimeoutInMin: 30
    }
    ...
}
```

------
#### [ Nextflow ]

```groovy
process ALIGN {
    container '123456789012.dkr.ecr.us-east-1.amazonaws.com/my-gpu-tool:1.0'
    accelerator 1, type: 'nvidia-l4,nvidia-tesla-a10g'
    cpus 8
    memory '32 GB'
    omicsMaxCpu 16
    omicsMaxMemory '64 GB'
    omicsResourceWaitTimeoutInMin 30
    ...
}
```

------

The request matches `omics.g6.2xlarge`, `omics.g6.4xlarge`, `omics.g5.2xlarge`, and `omics.g5.4xlarge`, and HealthOmics searches for capacity for up to 30 minutes.

### Search multiple sizes of one accelerator type
<a name="expanded-accelerator-search-multiple-sizes"></a>

To search every size of one accelerator type within a range, list a single accelerator type and set a maximum. The following task matches the four one-GPU `nvidia-l4` sizes from 8 to 64 vCPUs: `omics.g6.2xlarge`, `omics.g6.4xlarge`, `omics.g6.8xlarge`, and `omics.g6.16xlarge`. The 4-GPU sizes, `omics.g6.12xlarge` and `omics.g6.24xlarge`, are excluded because the task requests one GPU.

------
#### [ WDL ]

```wdl
runtime {
    acceleratorType: "nvidia-l4"
    acceleratorCount: 1
    cpu: 8
    memory: "32 GiB"
    omicsMaxCpu: 64
}
```

------
#### [ Nextflow ]

```groovy
process CALL_VARIANTS {
    accelerator 1, type: 'nvidia-l4'
    cpus 8
    memory '32 GB'
    omicsMaxCpu 64
    ...
}
```

------

### Use expanded search in a fallback profile
<a name="expanded-accelerator-search-fallback"></a>

A profile in `omicsResourceFallbackOrder` can use expanded search. HealthOmics searches all accelerator types in that profile at the same time and moves to the next profile when the profile's wait timeout ends. The following task searches `nvidia-l40s` for up to 45 minutes, then searches `nvidia-l4` and `nvidia-tesla-a10g` together with 8–16 vCPUs, and then falls back to a CPU-only profile with 32 vCPUs and 128 GiB of memory.

------
#### [ WDL ]

```wdl
runtime {
    docker: "123456789012.dkr.ecr.us-east-1.amazonaws.com/my-gpu-tool:1.0"
    omicsResourceFallbackOrder: [
        {"acceleratorType": "nvidia-l40s", "acceleratorCount": 1,
         "cpu": 8, "memory": "32 GiB",
         "omicsResourceWaitTimeoutInMin": 45},

        {"acceleratorType": "nvidia-l4,nvidia-tesla-a10g", "acceleratorCount": 1,
         "cpu": 8, "memory": "32 GiB",
         "omicsMaxCpu": 16, "omicsMaxMemory": "64 GiB"},

        {"cpu": 32, "memory": "128 GiB"}
    ]
}
```

------
#### [ Nextflow ]

```groovy
process ALIGN {
    container '123456789012.dkr.ecr.us-east-1.amazonaws.com/my-gpu-tool:1.0'

    omicsResourceFallbackOrder([
        [acceleratorType: 'nvidia-l40s', acceleratorCount: 1, cpus: 8, memory: '32 GB',
         omicsResourceWaitTimeoutInMin: 45],
        [acceleratorType: 'nvidia-l4,nvidia-tesla-a10g', acceleratorCount: 1, cpus: 8, memory: '32 GB',
         omicsMaxCpu: 16, omicsMaxMemory: '64 GB'],
        [cpus: 32, memory: '128 GB']
    ])
    ...
}
```

------

Set `omicsMaxCpu` and `omicsMaxMemory` only in profiles that have an `acceleratorType`. A task that sets expanded search fields at the task level can't also use `omicsResourceFallbackOrder`. When no instance type matches an expanded search profile, HealthOmics skips that profile, writes a warning to the run log, and tries the next profile.

## Find the instance type that a task ran on
<a name="expanded-accelerator-search-verify"></a>

Use the **get-run-task** AWS CLI command or the [GetRunTask](https://docs.aws.amazon.com/omics/latest/api/API_GetRunTask.html) API operation:

```bash
aws omics get-run-task --id {{1234567}} --task-id {{7654321}}
```

The following is a shortened example response:

```json
{
    "taskId": "7654321",
    "name": "align",
    "status": "RUNNING",
    "cpus": 8,
    "memory": 32,
    "gpus": 1,
    "instanceType": "omics.g5.2xlarge"
}
```

`instanceType` is the instance type that the task ran on, and it is the type that HealthOmics bills. It stays empty until the task gets an instance. The `cpus`, `memory`, and `gpus` fields show the minimum values you requested, not the size of the instance. For instance sizes, see [Accelerated-computing instances](memory-and-compute-tasks.md#workflow-task-accelerated-computing-instances).

To check every task in a run:

```bash
aws omics list-run-tasks --id {{1234567}} \
  --query 'items[].{task: taskId, name: name, instance: instanceType, gpus: gpus}'
```

In the task container, `AWS_HEALTHOMICS_RESOURCE_TYPE` holds the accelerator type of the instance that the task runs on, so a command can branch on the GPU it received. For more information, see [Environment variables for HealthOmics workflows](ecr-env-vars.md).

## Considerations
<a name="expanded-accelerator-search-considerations"></a>

Keep the following in mind when you use expanded accelerator search:
+ No preferred GPU: HealthOmics runs the task on the first matching instance type that launches, which might not be the fastest GPU you listed. A T4 instance can run GPU work more slowly than an L4 or A10G instance, so a task that lists `nvidia-tesla-t4` can take longer even though it started sooner. Use `omicsResourceFallbackOrder` when a task should wait for a specific GPU.
+ Skipped accelerator types: HealthOmics leaves out a listed type that is unsupported, not offered in the Region, or has no size in your range, and writes a warning to the run log. The warning names the skipped type and the types that HealthOmics searched instead, for example `acceleratorType: nvidia-l4 is not available in eu-west-1 and was ignored for task 'align'. Searching nvidia-tesla-a10g.` The run fails only when no listed type is left.
+ Duplicate accelerator types: A type listed more than once is searched once, with a warning in the run log.
+ Retries above the maximums: WDL doubles `memory` on an out-of-memory retry, and a Nextflow process can increase it on each attempt, for example `memory { 32.GB * task.attempt }`. HealthOmics rejects a retry that requests more memory than `omicsMaxMemory`, or more vCPUs than `omicsMaxCpu`, with `INVALID_TASK_RESOURCE_VALUE`, and the run fails. Each retry searches all matching instance types again, so it can run on a different instance type than the earlier attempt. Set the maximums to the largest values that any attempt can request.
+ Scatters: Each task in a scatter searches for capacity on its own, so tasks in the same scatter can run on different instance types.
+ Scratch storage: GPU tasks use the instance's local NVMe storage for scratch data. Set `disks` (WDL) or `disk` (Nextflow) to the minimum storage, in GiB, that your task needs, and HealthOmics only matches instance types whose local NVMe storage is at least that size. For more information, see [Ephemeral storage for HealthOmics workflow tasks](workflows-ephemeral-storage.md).

## Limits and quotas
<a name="expanded-accelerator-search-limits"></a>

The following limits apply to expanded accelerator search:
+ Wait timeout range: 20–10080 minutes (default 20)
+ Minimum `acceleratorCount`: 1
+ Maximum matching instance types per task: 40. A request that matches more is rejected when HealthOmics creates the task, with reason `INVALID_TASK_RESOURCE_VALUE`.

All other HealthOmics service limits and quotas apply. For more information, see [HealthOmics service quotas](service-quotas.md).

## Troubleshooting
<a name="expanded-accelerator-search-troubleshooting"></a>

### Run fails with UNSUPPORTED\_GPU\_INSTANCE\_TYPE
<a name="expanded-accelerator-search-ts-unsupported"></a>

None of the listed accelerator types can be used in the Region, `acceleratorType` lists no accelerators, or the run uses the ARM64 runtime platform. The message lists the accelerator types available in the Region, for example `No matching instance types for nvidia-l4, nvidia-l40s are available in eu-west-1.` Add an accelerator type from that list, run the workflow in a Region that offers the types you need, or run the task on x86.

### Run fails with INVALID\_TASK\_RESOURCE\_VALUE
<a name="expanded-accelerator-search-ts-invalid"></a>

The task's resource values can't be resolved to an instance type. The message names the cause:
+ No instance size matches the vCPU and memory range, the number of GPUs, or the `disks` minimum. Widen the range or add an accelerator type.
+ The request matches more than 40 instance types. Narrow the vCPU and memory range with `omicsMaxCpu` and `omicsMaxMemory`, or list fewer accelerator types.
+ `acceleratorCount` is missing. Set it to 1 or more.
+ `omicsMaxCpu` is less than `cpu`, or `omicsMaxMemory` is less than `memory`. This also happens when a retry raises `memory` above `omicsMaxMemory`. For more information, see [Considerations](#expanded-accelerator-search-considerations).
+ The task sets expanded search fields at the task level and also uses `omicsResourceFallbackOrder`. Move the fields into a profile.
+ A CPU profile sets `omicsMaxCpu` or `omicsMaxMemory`. Remove them from the CPU profile.

### Task fails with INSTANCE\_RESERVATION\_FAILED
<a name="expanded-accelerator-search-ts-reservation"></a>

No matching instance type had capacity within the wait timeout. The message lists the accelerator types searched, for example `There is insufficient instance capacity for nvidia-tesla-a10g, nvidia-l4 within 30 minutes to complete the workflow run.` Retry the run after some time, increase `omicsResourceWaitTimeoutInMin`, or add accelerator types or sizes so that more instance types match. To fall back to CPU when no GPU is available, use `omicsResourceFallbackOrder` with a final CPU profile.

### WDL workflow fails to create
<a name="expanded-accelerator-search-ts-wdl-create"></a>

WDL checks expanded search values when you call `CreateWorkflow` and rejects the workflow for an unsupported accelerator type, an empty entry in `acceleratorType` (for example, a doubled or trailing comma), a maximum below its minimum, or a negative wait timeout. The workflow status message names the value. Correct it and create the workflow again.

### Nextflow run fails with WORKFLOW\_RUN\_FAILED
<a name="expanded-accelerator-search-ts-nextflow"></a>

Nextflow reports invalid expanded search values in the workflow status message at `CreateWorkflow`, but the workflow still becomes `ACTIVE`, because a module or subworkflow can override the value. The run fails when the task starts, and the reason appears only in the engine log stream, `run/{{runId}}/engine`. Check the workflow status message and the engine log, then correct the value.

### Task runs on a different GPU than expected
<a name="expanded-accelerator-search-ts-different-gpu"></a>

HealthOmics selects the first matching instance type that launches, not the newest GPU. Check `instanceType` with `GetRunTask`, and check the run log for skipped accelerator types. Remove accelerator types that don't meet your performance requirements, or use `omicsResourceFallbackOrder` to set an order of preference.

## Limitations
<a name="expanded-accelerator-search-limitations"></a>

The following limitations apply:
+ Workflow languages: Expanded accelerator search is supported for WDL and Nextflow. CWL isn't supported.
+ x86 instance types only: Runs that use the ARM64 runtime platform fail with `UNSUPPORTED_GPU_INSTANCE_TYPE`.
+ No order of preference: HealthOmics doesn't apply the order in which you list accelerator types. Use `omicsResourceFallbackOrder` to set an order.
+ One configuration method per task: Expanded search fields at the task level can't be combined with `omicsResourceFallbackOrder`. Set them in a profile instead.
