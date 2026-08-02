---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_telemetry_workload_telemetry.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP02 Implement and configure workload telemetry
<a name="ops_telemetry_workload_telemetry"></a>

 Design and configure your workload to emit information about its internal state and current status, for example, API call volume, HTTP status codes, and scaling events. Use this information to help determine when a response is required.

 Use a service such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to aggregate logs and metrics from workload components (for example, API logs from [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), [AWS Lambda metrics](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html), [Amazon VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and [other services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/aws-services-sending-logs.html)).

 **Common anti-patterns:**
+  Your customers are complaining about poor performance. There are no recent changes to your application and so you suspect an issue with a workload component. You have no telemetry to analyze to determine what component or components are contributing to the poor performance.
+  Your application is unreachable. You lack the telemetry to determine if it's a networking issue.

 **Benefits of establishing this best practice:** Understanding what is going on inside your workload helps you to respond if necessary.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement log and metric telemetry: Instrument your workload to emit information about its internal state, status, and the achievement of business outcomes. Use this information to determine when a response is required.
  +  [Gaining better observability of your VMs with Amazon CloudWatch - AWS Online Tech Talks](https://youtu.be/1Ck_me4azMw)
  +  [How Amazon CloudWatch works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html)
  +  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
  +  [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
  +  [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
    +  Implement and configure workload telemetry: Design and configure your workload to emit information about its internal state and current status (for example, API call volume, HTTP status codes, and scaling events).
      +  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
      +  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
      +  [What Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
      +  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
+  [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/index.html)
+  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
+  [How Amazon CloudWatch works](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html)
+  [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  [What Is AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
+  [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

 **Related videos:**
+  [Application Performance Management on AWS](https://www.youtube.com/watch?v=5T4stR-HFas)
+  [Gaining Better Observability of Your VMs with Amazon CloudWatch](https://youtu.be/1Ck_me4azMw)
+  [Gaining better observability of your VMs with Amazon CloudWatch - AWS Online Tech Talks](https://youtu.be/1Ck_me4azMw)
