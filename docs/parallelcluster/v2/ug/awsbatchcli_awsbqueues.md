---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/awsbatchcli_awsbqueues.html
---

This documentation references AWS ParallelCluster. For running HPC and AI workloads, we recommend [AWS Parallel Computing Service (AWS PCS)](https://aws.amazon.com/pcs/), our managed Slurm service that lets you focus on running your workloads rather than managing infrastructure.

# `awsbqueues`
<a name="awsbatchcli_awsbqueues"></a>

Shows the job queue that is associated with the cluster.

```
awsbqueues [ - h ] [ - c {{CLUSTER}} ] [ - d ] [ {{job_queues}} [ {{job_queues}} ... ]]
```

## Positional arguments
<a name="awsbatchcli.awsbqueues.arguments"></a>

**{{job\_queues}}**
Specifies the space-separated list of queue names to show. If a single queue is requested, it is shown in a detailed version.

## Named arguments
<a name="awsbatchcli.awsbqueues.namedarguments"></a>

**-c {{CLUSTER}}, --cluster {{CLUSTER}}**
Specifies the name of the cluster to use.

**-d, --details**
Indicates whether to show the details of the queues.
Default: False
