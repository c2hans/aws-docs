---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/appendix.html
---

# Appendix: Amazon EBS SSD storage types
<a name="appendix"></a>

Amazon Elastic Block Store (Amazon EBS) provides the following solid state drive (SSD) backed volumes. For the most recent information, see [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) in the AWS documentation.

|
|
| Category | General purpose SSD | Provisioned IOPS SSD |
| --- |--- |--- |
| Volume Type | `gp3` | `gp2` | `io2 Block Express`[1] | `io2` | `io1` |
| Durability | 99.8% - 99.9% durability (0.1% - 0.2% annual failure rate) | 99.8% - 99.9% durability (0.1% - 0.2% annual failure rate) | 99.999% durability (0.001% annual failure rate) | 99.999% durability (0.001% annual failure rate) | 99.8% - 99.9% durability (0.1% - 0.2% annual failure rate) |
| Use cases | + Low-latency interactive apps<br />+ Development and test environments | + Low-latency interactive apps<br />+ Development and test environments | Workloads that require sub-millisecond latency, and sustained IOPs performance or more than 64,000 IOPs or 1,000 MIB/s of throughput | + Workloads that require sustained IOPs performance or more than 16,000 IOPs<br />+ I/O-intensive database workloads | + Workloads that require sustained IOPs performance or more than 16,000 IOPs<br />+ I/O-intensive database workloads |
| Volume size | 1 GiB - 16TiB | 1 GiB - 16TiB | 4 GiB - 64 TiB | 4 GiB - 16 TiB | 4 GiB - 16 TiB |
| Max IOPS per volume (16 KiB I/O) | 16,000 | 16,000 | 256,000 | 64,000[2] | 64,000[2] |
| Max throughput per volume | 1,000 MiB/s | 250 MiB/s[3] | 4,000 MiB/s | 1,000 MiB/s | 1,000 MiB/s |
| Amazon EBS Multi-attach | Not supported | Not supported | Supported | Supported | Supported |
| Boot volume | Supported  | Supported | Supported | Supported | Supported |

1  `io2 Block Express` volumes are supported with `R5b` instances only. `io2` volumes attached to an `R5b` instance during or after launch automatically run on Block Express. For more information, see [io2 Block Express volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#io2-block-express) in the Amazon EC2 documentation.

2 Maximum IOPS and throughput are guaranteed only on [instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances) provisioned with more than 32,000 IOPS. Other instances guarantee up to 32,000 IOPS and 500 MiB/s. `io1` volumes that were created before December 6, 2017 and that have not been modified since creation might not reach full performance unless you [modify the volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html).

3 The throughput limit is between 128 MiB/s and 250 MiB/s, depending on the volume size. Volumes smaller than or equal to 170 GiB deliver a maximum  throughput of 128 MiB/s. Volumes larger than 170 GiB but smaller than 334 GiB deliver a maximum throughput of 250 MiB/s if burst credits are available. Volumes larger than or equal to 334 GiB deliver 250 MiB/s regardless of burst credits. `gp2` volumes that were created before December 3, 2018 and that have not been modified since creation might not reach full performance unless you [modify the volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
