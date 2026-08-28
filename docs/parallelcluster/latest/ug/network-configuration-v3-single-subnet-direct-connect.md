---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/network-configuration-v3-single-subnet-direct-connect.html
---

# AWS ParallelCluster in a single private subnet connected using AWS Direct Connect
<a name="network-configuration-v3-single-subnet-direct-connect"></a>

When [`Scheduling`](Scheduling-v3.md) / [`SlurmQueues`](Scheduling-v3.md#Scheduling-v3-SlurmQueues) / [`Networking`](Scheduling-v3.md#Scheduling-v3-SlurmQueues-Networking) / [`AssignPublicIp`](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-Networking-AssignPublicIp) is set to `false`, the subnets must be correctly set up to use the Proxy for all traffic. Web access is required for both head and compute nodes.

 ![ParallelCluster in a single private subnet connected using Direct Connect](http://docs.aws.amazon.com/parallelcluster/latest/ug/images/single-private-DirectConnect.png)

 The configuration for this architecture requires the following settings:

```
# Note that all values are only provided as examples
HeadNode:
  ...
  Networking:
    SubnetId: subnet-34567890 # subnet with proxy
    Proxy:
      HttpProxyAddress: http://proxy-address:port
  Ssh:
    KeyName: ec2-key-name
Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - ...
      Networking:
        SubnetIds:
          - subnet-34567890 # subnet with proxy
        AssignPublicIp: false
        Proxy:
          HttpProxyAddress: http://proxy-address:port
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
