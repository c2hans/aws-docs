---
source_url: https://docs.aws.amazon.com/omics/latest/dev/task-accelerators.html
---

# Task accelerators in a HealthOmics workflow definition
<a name="task-accelerators"></a>

In the workflow definition, you can optionally specify the GPU accelerator-spec for a task. HealthOmics supports the following accelerator-spec values, along with the supported instance types:

| Accelerator spec | Healthomics instance types |
| --- | --- |
| nvidia-tesla-t4 | G4 |
| nvidia-tesla-t4-a10g | G4 and G5 |
| nvidia-tesla-a10g | G5 |
| nvidia-t4-a10g-l4 | G4, G5, and G6 |
| nvidia-l4-a10g | G5 and G6 |
| nvidia-l4 | G6 |
| nvidia-l40s | G6e |

If you specify an accelerator type that supports multiple instance types, HealthOmics selects the instance type based on available capacity. If both instance types are available, HealthOmics gives preference to the lower cost instance. The exception is for the nvidia-t4-a10g-l4 task accelerator which gives preference to the latest generation instance available.

For details about the instance types, see [Accelerated-computing instances](memory-and-compute-tasks.md#workflow-task-accelerated-computing-instances).

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
#### [ NextFlow ]

```
process my_task {
 ...
 accelerator 1, type: "{{nvidia-l4}}"
 ...
}
```

------
#### [ CWL ]

```
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
