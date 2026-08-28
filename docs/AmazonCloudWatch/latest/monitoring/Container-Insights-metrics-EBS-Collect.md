---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-EBS-Collect.html
---

# Collect Amazon EBS NVMe driver metrics
<a name="Container-Insights-metrics-EBS-Collect"></a>

For CloudWatch agent to collect AWS NVMe driver metrics for Amazon EBS volumes attached to an Amazon EC2 instance, add the `diskio` section inside the `metrics_collected` section of the CloudWatch agent configuration file.

Additionally, the CloudWatch agent binary requires `ioctl` permissions for NVMe driver devices to collect metrics from attached Amazon EBS volumes.

The following metrics can be collected.

| Metric | Metric name in CloudWatch | Description |
| --- | --- | --- |
| `ebs_total_read_ops` | `diskio_ebs_total_read_ops` | The total number of completed read operations. |
| `ebs_total_write_ops` | `diskio_ebs_total_write_ops` | The total number of completed write operations. |
| `ebs_total_read_bytes` | `diskio_ebs_total_read_bytes` | The total number of read bytes transferred. |
| `ebs_total_write_bytes` | `diskio_ebs_total_write_bytes` | The total number of write bytes transferred. |
| `ebs_total_read_time` | `diskio_ebs_total_read_time` | The total time spent, in microseconds, by all completed read operations. |
| `ebs_total_write_time` | `diskio_ebs_total_write_time` | The total time spent, in microseconds, by all completed write operations. |
| `ebs_volume_performance_exceeded_iops` | `diskio_ebs_volume_performance_exceeded_iops` | The total time, in microseconds, that IOPS demand exceeded the volume's provisioned IOPS performance. |
| `ebs_volume_performance_exceeded_tp` | `diskio_ebs_volume_performance_exceeded_tp` | The total time, in microseconds, that throughput demand exceeded the volume's provisioned throughput performance. |
| `ebs_ec2_instance_performance_exceeded_iops` | `diskio_ebs_ec2_instance_performance_exceeded_iops` | The total time, in microseconds, that the EBS volume exceeded the attached Amazon EC2 instance's maximum IOPS performance. |
| `ebs_ec2_instance_performance_exceeded_tp` | `diskio_ebs_ec2_instance_performance_exceeded_tp` | The total time, in microseconds, that the EBS volume exceeded the attached Amazon EC2 instance's maximum throughput performance. |
| `ebs_volume_queue_length` | `diskio_ebs_volume_queue_length` | The number of read and write operations waiting to be completed. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
