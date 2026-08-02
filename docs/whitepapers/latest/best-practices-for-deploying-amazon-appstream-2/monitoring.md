---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/monitoring.html
---

# Monitoring
<a name="monitoring"></a>

## Using dashboards
<a name="using-dashboards"></a>

 Monitoring fleet utilization is a regular activity that can be performed through CloudWatch metrics and creating a dashboard. Alternatively, from the WorkSpaces Applications console, use the **Fleet Usage** tab. Regularly monitor your fleet usage, as user behavior is not always predictable, and demand can exceed even first-rate upfront planning. A full listing of WorkSpaces Applications metrics and dimensions for CloudWatch can be found in the WorkSpaces Applications administration guide under [https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html#monitoring-with-cloudwatch](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html#monitoring-with-cloudwatch).

## Anticipating growth
<a name="anticipating-growth"></a>

 Whenever there is a large jump in `PendingCapacity`, an auto scaling event has occurred. It is important to confirm that `AvailableCapacity` and `PendingCapacity` have an inverse relationship while new WorkSpaces Applications fleet instances become available to host user sessions. Create a CloudWatch Alarm for `InsufficientCapacityError` for each WorkSpaces Applications fleet to notify administrators to ensure automatic scaling is not falling behind demand.

 If demand exceeds capacity and `InsufficientCapacityError` metric values are common, consider raising the minimum capacity through a Scheduled Scaling policy for the start of the work day. In addition, have a second Scheduled Scaling policy to lower the minimum capacity after the demand has been satisfied. Keep in mind that lowering the value for minimum capacity does not impact existing sessions. Lowering the minimum capacity prior to the end of the work day effectively enables scale to function as intended by lowering the value for `ActualCapacity`. This optimizes cost.

 If demand is consistently unpredictable, use [https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html#autoscaling-target-tracking](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html#autoscaling-target-tracking) to ensure that there is adequate `AvailableCapacity` in the WorkSpaces Applications fleet to meet demand while determining usage patterns. Continue to monitor as Target Tracking uses a percentage of fleet consumption. As the total number of fleet instances grows, the total number of unused fleet instances multiplies. This can become wasteful unless the maximum capacity is set to a conservative value. Use multiple types of scaling policies (for example, Scheduled and Target Tracking) to balance reliability with cost optimization.

## Monitoring user usage
<a name="monitoring-user-usage"></a>

 Monitoring unique users, as there is a [https://aws.amazon.com/appstream2/pricing/](https://aws.amazon.com/appstream2/pricing/). This user fee cost is due to Image Assistant (RDS) subscriber access licenses (SAL). Evaluating unique users can either be performed through reporting from the IdP where authentication is performed, or through [https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-usage-reports.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/enable-usage-reports.html).

 Usage reports are stored as separate `.csv` files in your S3 bucket, which you can download and analyze using third-party business intelligence (BI) tools. You can analyze your usage data in AWS without downloading your reports or create reports over custom date ranges without concatenating multiple `.csv` files. For example, you can [https://aws.amazon.com/blogs/desktop-and-application-streaming/analyze-your-amazon-appstream-2-0-usage-reports-using-amazon-athena-and-amazon-quicksight/](https://aws.amazon.com/blogs/desktop-and-application-streaming/analyze-your-amazon-appstream-2-0-usage-reports-using-amazon-athena-and-amazon-quicksight/).

## Persisting application and Windows event logs
<a name="persisting-application-and-windows-event-logs"></a>

 When a WorkSpaces Applications instance session is complete, the instance is ended. This means all application and Windows event logs used in the session are lost. If there is a requirement to persist these application and Windows event logs, one method is to use [https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) to [https://aws.amazon.com/blogs/desktop-and-application-streaming/monitoring-amazon-appstream-2-0-with-amazon-es-and-amazon-kinesis-data-firehose/](https://aws.amazon.com/blogs/desktop-and-application-streaming/monitoring-amazon-appstream-2-0-with-amazon-es-and-amazon-kinesis-data-firehose/) and search with [https://aws.amazon.com/opensearch-service/](https://aws.amazon.com/opensearch-service/) (OpenSearch Service). If queries are not anticipated to be frequent, to optimize on cost, use [https://aws.amazon.com/athena/](https://aws.amazon.com/athena/) to search as opposed to running Amazon OpenSearch Service.

## Auditing network and administrative activity
<a name="auditing-network-and-administrative-activity"></a>

 If not already set up, it is a best practice to configure [https://aws.amazon.com/cloudtrail/](https://aws.amazon.com/cloudtrail/) for the AWS account with Amazon WorkSpaces Applications. To audit WorkSpaces Applications API calls specifically, use the filter event source with a value of `appstream.amazonaws.com`.

 Enable VPC flow logs to audit access into customer-managed resources. VPC flow logs can be [https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html) to perform queries when auditing is required.

 Monitoring subnet IP allocation is important as WorkSpaces Applications fleets grow. Report on IP assignment by running the [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-subnets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-subnets.html) CLI to report the available IP addresses in each subnet assigned to fleets. Ensure that your organization has sufficient IP address capacity to meet the demand of all fleets running at maximum capacity.
