---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/appstream-well-architected-framework/cost-optimization.html
---

# Cost optimization pillar
<a name="cost-optimization"></a>

The [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-optimization.html) of the AWS Well-Architected Framework focuses on maximizing business value while minimizing expenditure. It helps ensure that every dollar you spend on cloud resources contributes effectively to achieving your organizational objectives.

Key focus areas for applying this pillar to your WorkSpaces Applications streaming environment:
+ Fleet capacity management and instance type selection
+ Scaling and scheduling optimization
+ Monitoring and analysis of usage patterns
+ Cost allocation and tracking

## Implement cloud financial management
<a name="cost-financial"></a>

Build dedicated organizational capability in cloud financial management and cost optimization through structured programs and processes to maximize cloud value and efficiency.
+ Monitor WorkSpaces Applications costs by using [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) and usage reports to track streaming hours usage, analyze fleet instance costs, and monitor regional cost distribution.
+ Plan and set cost controls by using [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to set alerts for overall WorkSpaces Applications service costs, create budget thresholds for the service, and monitor actual spending against budgeted amounts. For more information, see the AWS blog post [How to use automation to optimize and control cost of Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/how-to-use-automation-to-optimize-and-control-cost-of-amazon-appstream-2-0/).

## Add a consumption model
<a name="cost-consumption"></a>

Scale computing resources and costs based on actual usage patterns. For example, you can shut down non-production environments during off-hours to optimize spending.
+ Choose the appropriate pricing model. For example, use always-on fleets for consistent usage and on-demand fleets for variable workloads.
+ Select optimal instance types. For example, use `stream.standard` instances for general applications and use graphics instances (G4dn) only when required.

## Measure overall efficiency
<a name="cost-efficiency"></a>

Calculate and track the cost-per-unit of business output to quantify efficiency improvements and guide optimization efforts.
+ Track session efficiency.
+ Monitor fleet utilization by using the following CloudWatch metrics:
  + `AvailableCapacity` to track unused capacity
  + `InUseCapacity` to measure actual usage
+ Calculate and track per-session costs such as cost per streaming hour, cost per user, and cost per application.
+ Implement the [Cost Optimizer for WorkSpaces Applications](https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2) to monitor your builders.
+ Compare costs between fleet types. For example, compare:
  + License costs for single sessions and multi-sessions
  + Resource utilization rates
  + User density per instance
+ Use process tracking data to identify underutilized or unnecessary applications. For more information, see the AWS blog post [Track user processes in Amazon WorkSpaces Applications sessions](https://aws.amazon.com/blogs/desktop-and-application-streaming/track-user-processes-in-amazon-appstream-2-0-sessions/).

## Stop spending money on undifferentiated heavy lifting
<a name="cost-heavy-lifting"></a>

AWS manages infrastructure operations and offers managed services so your organization can focus on business objectives instead of IT maintenance.
+ Create and maintain application images by using Image Builder to package your applications, configure application settings, and test application compatibility.
+ Configure fleet specifications by selecting appropriate instance types and defining scaling thresholds and setting desired capacity limits.
+ Set up persistent storage options by configuring home folders in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for Windows-based fleets and shared file systems in [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) for Linux-based fleets. Set storage permissions and define retention policies.

## Analyze and attribute expenditure
<a name="cost-expenditure"></a>

The cloud enables precise tracking of resource usage and costs per workload, which allows for accurate return on investment (ROI) measurements and targeted optimization opportunities.
+ Implement a comprehensive tagging strategy for fleets for cost allocation, images for asset tracking, image builders for environment designation, and stacks for organizational grouping.
+ Use [AWS Cost and Usage Reports (AWS CUR)](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) to break down WorkSpaces Applications costs by tagged resources, and analyze costs per fleet, stack, and image.
+ Use [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) to visualize WorkSpaces Applications spending trends, and compare costs across different dimensions such as Regions and instance types.
+ Monitor and analyze fleet utilization rates, instance type efficiency, and streaming hours by application.
+ Track unused reserved capacity, underutilized fleets or stacks, and idle periods in fleet usage.
+ Calculate and track cost per user for each application, streaming hours per application, and user adoption rates for streamed applications.
+ Set up detailed usage analysis by configuring WorkSpaces Applications usage reports, using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) to query usage data, and creating visualizations in [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) for cost and usage insights.
+ Evaluate total cost considerations such as Windows Server licensing, application licensing models, and per-user licensing compared with per-device licensing.
+ Use Amazon Athena to query and analyze home folder storage costs and usage patterns by user. For more information, see the AWS blog post [How to report Amazon WorkSpaces Applications home folder use with Amazon Athena](https://aws.amazon.com/blogs/desktop-and-application-streaming/how-to-report-amazon-appstream-2-0-home-folder-use-with-amazon-athena/).
