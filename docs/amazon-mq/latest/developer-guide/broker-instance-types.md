---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-instance-types.html
---

# Amazon MQ for ActiveMQ broker instance types
<a name="broker-instance-types"></a>

The combined description of the broker instance *class* (`m5`) and *size* (`large`, `medium`) is called the *broker instance type* (for example, `mq.m5.large`). The following table lists the available Amazon MQ broker instance types for ActiveMQ brokers.

Amazon MQ provides at least a 90 day notice before an instance type reaches end of support. We recommend upgrading your broker to a new instance type before the end-of-support date to prevent any disruptions.

**Important**
You cannot create brokers on `t2.micro` or `mq.m4.large` after March 17, 2025.

| Instance Type | vCPU | Memory (GiB) | Recommended Use | Storage | End of support on Amazon MQ |
| --- | --- | --- | --- | --- | --- |
| mq.t3.micro | 2 | 1 |  Evaluation  | EFS |  |
| mq.m5.large | 2 | 8 | Production | EFS or EBS |  |
| mq.m5.xlarge | 4 | 16 | Production | EFS or EBS |   |
| mq.m5.2xlarge | 8 | 32 | Production | EFS or EBS |   |
| mq.m5.4xlarge | 16 | 64 | Production | EFS or EBS |   |

For more information about throughput considerations, see [Choose the Correct Broker Instance Type for the Best Throughput](best-practices-activemq.md#broker-instance-types-choosing).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
