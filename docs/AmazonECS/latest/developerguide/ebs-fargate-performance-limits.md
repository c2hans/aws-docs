---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-fargate-performance-limits.html
---

# Performance of Amazon EBS volumes for Fargate on-demand tasks
<a name="ebs-fargate-performance-limits"></a>

The baseline Amazon EBS volume IOPS and throughput available for a Fargate on-demand task depends on the total CPU units you request for the task. If you request 0.25, 0.5, or 1 virtual CPU unit (vCPU) for your Fargate task, we recommend that you configure a General Purpose SSD volume (`gp2` or `gp3`) or a Hard Disk Drive (HDD) volume (`st1` or `sc1`). If you request more than 1 vCPU for your Fargate task, the following baseline performance limits apply to an Amazon EBS volume attached to the task. You may temporarily get higher EBS performance than the following limits. However, we recommend that you plan your workload based on these limits.

| CPU units requested (in vCPUs) | Baseline Amazon EBS IOPS(16 KiB I/O) | Baseline Amazon EBS Throughput (in MiBps, 128 KiB I/O) | Baseline bandwidth (in Mbps) |
| --- | --- | --- | --- |
| 2 | 3,000 | 75 | 360 |
| 4 | 5,000 | 120 | 1,150 |
| 8 | 10,000 | 250 | 2,300 |
| 16 | 15,000 | 500 | 4,500 |

**Note**
 When you configure an Amazon EBS volume for attachment to a Fargate task, the Amazon EBS performance limit for Fargate task is shared between the task's ephemeral storage and the attached volume.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
