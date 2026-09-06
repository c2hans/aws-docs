---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_type_size_number_resources_cost_modeling.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST06-BP01 Perform cost modeling
<a name="cost_type_size_number_resources_cost_modeling"></a>

 Identify organization requirements and perform cost modeling of the workload and each of its components. Perform benchmark activities for the workload under different predicted loads and compare the costs. The modeling effort should reflect the potential benefit. For example, time spent is proportional to component cost.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Perform cost modeling for your workload and each of its components to understand the balance between resources, and find the correct size for each resource in the workload, given a specific level of performance. Perform benchmark activities for the workload under different predicted loads and compare the costs. The modelling effort should reflect potential benefit; for example, time spent is proportional to component cost or predicted saving. For best practices, refer to the *Review* section of the [Performance Efficiency Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/review.html).

[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) can assist with cost modelling for running workloads. It provides right-sizing recommendations for compute resources based on historical usage. This is the ideal data source for compute resources because it is a free service, and it utilizes machine learning to make multiple recommendations depending on levels of risk. You can also use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) with custom logs as data sources for right sizing operations for other services and workload components.

The following are recommendations for cost modelling data and metrics:
+ The monitoring must accurately reflect the end-user experience. Select the correct granularity for the time period and thoughtfully choose the maximum or 99th percentile instead of the average.
+ Select the correct granularity for the time period of analysis that is required to cover any workload cycles. For example, if a two-week analysis is performed, you might be overlooking a monthly cycle of high utilization, which could lead to under-provisioning.

**Implementation steps **
+ ** Perform cost modeling: **Deploy the workload or a proof-of-concept, into a separate account with the specific resource types and sizes to test. Run the workload with the test data and record the output results, along with the cost data for the time the test was run. Then redeploy the workload or change the resource types and sizes and re-run the test.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
+  [Amazon CloudWatch features](https://aws.amazon.com/cloudwatch/features/)
+  [Cost Optimization: Amazon EC2 Right Sizing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html)
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
