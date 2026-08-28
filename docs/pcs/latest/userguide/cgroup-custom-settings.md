---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/cgroup-custom-settings.html
---

# Configuring custom cgroup settings in AWS PCS
<a name="cgroup-custom-settings"></a>

Slurm uses the Linux cgroup subsystem to manage and constrain resources for jobs, including memory, CPU cores, devices, and swap space. AWS PCS lets you customize `cgroup.conf` settings at the cluster level through the `CgroupCustomSettings` property of `SlurmConfiguration` during cluster creation or update.

## Configuring cgroup settings
<a name="cgroup-custom-settings-configure"></a>

Cgroup custom settings can be configured through the AWS Console, CLI, or SDKs during cluster creation or modified later through update operations.

------
#### [ AWS Management Console ]

Navigate to **Additional scheduler settings** in the create or edit page for a cluster resource.

**To add a new setting**

1. Choose **Add new setting**.

1. Select a **Parameter** name from the dropdown (which includes brief parameter descriptions).

1. Provide the corresponding value.

**To unset a custom setting**

1. Choose **Remove** next to the relevant parameter/value pair.

1. Create or update the resource.

------
#### [ AWS CLI ]

For programmatic management of cgroup settings, use the `CgroupCustomSettings` field in create or update cluster operations.

**Example – Setting `ConstrainRAMSpace` on a cluster**

```
aws pcs update-cluster --cluster-identifier {{my-cluster}} \
--slurm-configuration \
'CgroupCustomSettings=[{parameterName=ConstrainRAMSpace,parameterValue="yes"}]'
```

------

## Supported cgroup settings for clusters
<a name="cgroup-custom-settings-cluster"></a>

The following custom cgroup settings are supported at the cluster level:
+ [AllowedRAMSpace](https://slurm.schedmd.com/cgroup.conf.html#OPT_AllowedRAMSpace)
+ [AllowedSwapSpace](https://slurm.schedmd.com/cgroup.conf.html#OPT_AllowedSwapSpace)
+ [ConstrainCores](https://slurm.schedmd.com/cgroup.conf.html#OPT_ConstrainCores)
+ [ConstrainDevices](https://slurm.schedmd.com/cgroup.conf.html#OPT_ConstrainDevices)
+ [ConstrainRAMSpace](https://slurm.schedmd.com/cgroup.conf.html#OPT_ConstrainRAMSpace)
+ [ConstrainSwapSpace](https://slurm.schedmd.com/cgroup.conf.html#OPT_ConstrainSwapSpace)
+ [IgnoreSystemd](https://slurm.schedmd.com/cgroup.conf.html#OPT_IgnoreSystemd)
+ [MaxRAMPercent](https://slurm.schedmd.com/cgroup.conf.html#OPT_MaxRAMPercent)
+ [MaxSwapPercent](https://slurm.schedmd.com/cgroup.conf.html#OPT_MaxSwapPercent)
+ [MinRAMSpace](https://slurm.schedmd.com/cgroup.conf.html#OPT_MinRAMSpace)
+ [SignalChildrenProcesses](https://slurm.schedmd.com/cgroup.conf.html#OPT_SignalChildrenProcesses)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
