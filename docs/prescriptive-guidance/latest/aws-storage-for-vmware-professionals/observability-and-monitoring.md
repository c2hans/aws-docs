---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-storage-for-vmware-professionals/observability-and-monitoring.html
---

# Observability
<a name="observability-and-monitoring"></a>

Monitoring storage performance is vital for maintaining optimal system operations in both VMware and AWS environments. While VMware relies on built-in vSphere tools and third-party integrations to track metrics, AWS provides centralized monitoring through Amazon CloudWatch that covers all its storage services. This section describes various approaches and tools for optimizing storage resources.

**VMware monitoring**
+ **Performance charts –** Display real-time data for CPU, memory, storage, and other system resources.
+ **Command-line utilities –** Access detailed performance information through CLI tools.
+ **Host health –** Identify healthy hosts versus those experiencing problems.
+ **Events, alerts, and alarms –** Configure automated notifications and specify system responses when thresholds are triggered.
+ **System log files –** Save detailed activities for the vSphere environment.

**AWS monitoring**

AWS provides comprehensive monitoring through Amazon CloudWatch, covering all storage services with metrics comparable to VMware's traditional approach. While VMware focuses on latency, throughput, IOPS, and disk group activity through visualization tools, AWS offers similar capabilities including read and write IOPS, throughput, latency, storage, and burst credits.

CloudWatch is the central monitoring hub that provides performance metrics and logs for Amazon EBS volumes, Amazon S3 buckets, and Amazon EFS file systems. Additional tools include the following:
+ **Custom alarms –** Automated notifications and actions based on defined thresholds
+ **Amazon EBS volume performance insights –** Visualized volume health and identify bottlenecks
+ **Service-specific metrics – **Tailored monitoring for S3 and EFS optimization

|
|
| Aspect | VMware | AWS |
| --- |--- |--- |
| Performance monitoring | Third-party tool integrationvCenter monitoring vSAN performance serviceVMware Aria Operations for Logs | CloudWatch metricsEBS volume performance insightsEFS performance metricsS3 analytics |
| Metrics tracking | Disk group activityIOPSLatencyNetwork throughput | Burst creditsLatencyRead and write IOPSStorage utilizationThroughput |

**AWS storage optimizing and metrics**

AWS provides the following native tools for monitoring storage:
+ **Amazon CloudWatch –** CloudWatch provides centralized monitoring for all storage services including EBS, S3, and EFS. Metrics include IOPS, read and write latency, throughput, and storage utilization. Custom alarms trigger notifications or automated actions when performance thresholds are exceeded.
+ **Amazon EBS –** CloudWatch tracks EBS metrics that include read and write IOPS, throughput, latency, and burst credit balance (for gp2/gp3 volumes).
+ **Amazon S3 and Amazon EFS –** CloudWatch provides S3 metrics that include request counts, data transfer rates, error rates, and latency. EFS provides throughput metrics, burst credit balance, and client connection counts to optimize file system performance.
