---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-lifecycle-best-practices-slurm-what-hyperpod-overrides-in-slurm-conf.html
---

# What particular configurations HyperPod manages in Slurm configuration files
<a name="sagemaker-hyperpod-lifecycle-best-practices-slurm-what-hyperpod-overrides-in-slurm-conf"></a>

When you create a Slurm cluster on HyperPod, the HyperPod agent sets up the [https://slurm.schedmd.com/slurm.conf.html](https://slurm.schedmd.com/slurm.conf.html) and [https://slurm.schedmd.com/gres.conf.html](https://slurm.schedmd.com/gres.conf.html) files at `/opt/slurm/etc/` to manage the Slurm cluster based on your HyperPod cluster creation request and lifecycle scripts. The following list shows which specific parameters the HyperPod agent handles and overwrites.

**Important**
We strongly recommend that you **do not** change these parameters managed by HyperPod.
+ In [https://slurm.schedmd.com/slurm.conf.html](https://slurm.schedmd.com/slurm.conf.html), HyperPod sets up the following basic parameters: `ClusterName`, `SlurmctldHost`, `PartitionName`, and `NodeName`.

  Also, to enable the [Automatic node recovery and auto-resume](sagemaker-hyperpod-resiliency-slurm-auto-resume.md) functionality, HyperPod requires the `TaskPlugin` and `SchedulerParameters` parameters set as follows. The HyperPod agent sets up these two parameters with the required values by default.

  ```
  TaskPlugin=task/none
  SchedulerParameters=permit_job_expansion
  ```
+ In [https://slurm.schedmd.com/gres.conf.html](https://slurm.schedmd.com/gres.conf.html), HyperPod manages `NodeName` for GPU nodes.
