---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/identifying-opportunities-to-right-size.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Identifying Opportunities to Right Size
<a name="identifying-opportunities-to-right-size"></a>

 The first step in right sizing is to monitor and analyze your current use of services to gain insight into instance performance and usage patterns. To gather sufficient data, observe performance over at least a two-week period (ideally, over a one-month period) to capture the workload and business peak. The most common metrics that define instance performance are vCPU utilization, memory utilization, network utilization, and ephemeral disk use. In rare cases where instances are selected for reasons other than these metrics, it is important for the technical owner to review the right-sizing effort.

## Tools for Right Sizing
<a name="tools-for-right-sizing"></a>

 You can use the following tools to evaluate costs and monitor and analyze instance usage for right sizing:
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) – Lets you observe CPU utilization, network throughput, and disk I/O, and match the observed peak metrics to a new and cheaper instance type. You can also regularly monitor [Amazon EC2 Usage Reports](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/usage-reports.html), which are updated several times a day and provide in-depth usage data for all your EC2 instances. Typically, this is feasible only for small environments given the time and effort required.
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) – This free tool lets you dive deeper into your cost and usage data to identify trends, pinpoint cost drivers, and detect anomalies. It includes Amazon EC2 Usage Reports*,* which let you analyze the cost and usage of your EC2 instances over the last 13 months.
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/best-practices/) – Lets you inspect your AWS environment to identify idle and underutilized resources and provides real-time insight into service usage to help you improve system performance and reliability, increase security, and look for opportunities to save money.
+  Third-party monitoring tools, such as CloudHealth, Cloudability, and CloudCheckr, are also an option to automatically identify opportunities and suggest alternate instances. These tools have years of development effort and customer feedback points built into them. They also provide additional cost management and optimization functionality.

## Tips for Developing Your Own Right-Sizing Tools
<a name="tips-for-developing-your-own-right-sizing-tools"></a>

 You can also develop your own tools for monitoring and analyzing performance. The following guidelines can help if you are considering this option:
+  Focus on instances that have run for at least half the time you’re looking at.
+  Focus on instances with lower Reserved Instance coverage.
+  Exclude resources that have been switched off (reducing search effort).
+  Avoid conversions to older-generation instances, where possible.
+  Apply a savings threshold below which right sizing is not worth considering.
+  Make sure the following conditions are met before you switch to a new instance:
  +  The vCPU of the new instance is equal to that of the old instance *or* the application’s observed vCPU is less than 80% of the vCPU capacity of the new instance.
  +  The memory of the new instance is equal to that of the old instance *or* the application’s observed memory peak is less than 80% of the memory capacity of the new instance.

     Note: You can capture memory utilization metrics by using monitoring scripts that report these metrics to Amazon CloudWatch. For more information, see [Monitoring Memory and Disk Metrics for Amazon EC2 Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html).
  +  The network throughput of the new instance is equal to that of the old instance *or* the application’s network peak is less than the network capacity of the new instance.

     Note: Maximum NetworkIn and NetworkOut values are measured in bytes-per-minute. Use the following formula to convert these metrics to megabits per second:

     Maximum NetworkIn (or NetworkOut) x 8 (bytes to bits) /1024/1024/ 60 = Number of Mbps
  +  If the ephemeral storage disk I/O is less than 3,000, you can use [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) storage. If not, use instance families that have ephemeral storage. For more information, see [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html).
