---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-instance-store-Collect.html
---

# Collect Amazon EC2 instance store volume NVMe driver metrics
<a name="Container-Insights-metrics-instance-store-Collect"></a>

For CloudWatch agent to collect AWS NVMe driver metrics for instance store volumes attached to an Amazon EC2 instance, add the `diskio` section inside the `metrics_collected` section of the CloudWatch agent configuration file.

Additionally, the CloudWatch agent binary requires `ioctl` permissions for NVMe driver devices to collect metrics from attached instance store volumes.

The following metrics can be collected.

| Metric | Metric name in CloudWatch | Description |
| --- | --- | --- |
| `instance_store_total_read_ops` | `diskio_instance_store_total_read_ops` | The total number of completed read operations. |
| `instance_store_total_write_ops` | `diskio_instance_store_total_write_ops` | The total number of completed write operations. |
| `instance_store_total_read_bytes` | `diskio_instance_store_total_read_bytes` | The total number of read bytes transferred. |
| `instance_store_total_write_bytes` | `diskio_instance_store_total_write_bytes` | The total number of write bytes transferred. |
| `instance_store_total_read_time` | `diskio_instance_store_total_read_time` | The total time spent, in microseconds, by all completed read operations. |
| `instance_store_total_write_time` | `diskio_instance_store_total_write_time` | The total time spent, in microseconds, by all completed write operations. |
| `instance_store_performance_exceeded_iops` | `diskio_instance_store_performance_exceeded_iops` | The total time, in microseconds, that IOPS demand exceeded the volume's IOPS maximum performance. |
| `instance_store_performance_exceeded_tp` | `diskio_instance_store_performance_exceeded_tp` | The total time, in microseconds, that throughput demand exceeded the volume's maximum throughput performance. |
| `instance_store_volume_queue_length` | `diskio_instance_store_volume_queue_length` | The number of read and write operations waiting to be completed. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
