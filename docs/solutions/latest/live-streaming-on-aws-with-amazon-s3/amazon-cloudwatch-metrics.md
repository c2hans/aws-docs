---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/amazon-cloudwatch-metrics.html
---

# Amazon CloudWatch metrics
<a name="amazon-cloudwatch-metrics"></a>

The Live Streaming on AWS with Amazon S3 solution activates Amazon CloudWatch metrics to monitor Amazon S3 requests made to the live stream distribution bucket. Out of the 16 metrics available for Amazon S3 requests, the following metrics are used for this solution:
+ All requests
+ PUT requests
+ DELETE requests
+ HEAD requests
+ LIST requests
+ Bytes downloaded
+ Bytes uploaded
+ 4xx errors
+ 5xx errors
+ First byte latency
+ Total request latency

To deactivate CloudWatch metrics for the live stream distribution bucket, remove the metrics filter:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. On the **Stacks** page, select the solution stack.

1. Select the **Outputs** tab.

1. View bucket metrics by selecting the hyperlink for the **BucketMetrics** output.

1. Choose **Manage filters**, then select the filter.

1. Choose **Delete**.
