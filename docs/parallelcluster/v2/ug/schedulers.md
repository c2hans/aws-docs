---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/schedulers.html
---

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# Schedulers supported by AWS ParallelCluster
<a name="schedulers"></a>

AWS ParallelCluster supports several schedulers, set using the [`scheduler`](cluster-definition.md#scheduler) setting.

**Note**
Starting with version 2.11.5, AWS ParallelCluster doesn't support the use of SGE or Torque schedulers. You can continue using them in versions up to and including 2.11.4, but they aren't eligible for future updates or troubleshooting support from the AWS service and AWS Support teams.

**Topics**
+ [Son of Grid Engine](schedulers.sge.md)
+ [Slurm Workload Manager](schedulers.slurm.md)
+ [Torque Resource Manager](schedulers.torque.md)
+ [AWS Batch](awsbatchcli.md)
