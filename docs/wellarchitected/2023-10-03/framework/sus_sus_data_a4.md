---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sus_sus_data_a4.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP03 Use policies to manage the lifecycle of your datasets
<a name="sus_sus_data_a4"></a>

Manage the lifecycle of all of your data and automatically enforce deletion to minimize the total storage required for your workload.

 **Common anti-patterns:**
+  You manually delete data.
+  You do not delete any of your workload data.
+  You do not move data to more energy-efficient storage tiers based on its retention and access requirements.

 **Benefits of establishing this best practice:** Using data lifecycle policies ensures efficient data access and retention in a workload.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Datasets usually have different retention and access requirements during their lifecycle. For example, your application may need frequent access to some datasets for a limited period of time. After that, those datasets are infrequently accessed.

 To efficiently manage your datasets throughout their lifecycle, configure lifecycle policies, which are rules that define how to handle datasets.

 With Lifecycle configuration rules, you can tell the specific storage service to transition a dataset to more energy-efficient storage tiers, archive it, or delete it.

 **Implementation steps**
+  [Classify datasets in your workload.](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a2.html)
+  Define handling procedures for each data class.
+  Set automated lifecycle policies to enforce lifecycle rules. Here are some examples of how to set up automated lifecycle policies for different AWS storage services:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sus_sus_data_a4.html)
+  Delete unused volumes, snapshots, and data that is out of its retention period. Leverage native service features like Amazon DynamoDB Time To Live or Amazon CloudWatch log retention for deletion.
+  Aggregate and compress data where applicable based on lifecycle rules.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Optimize your Amazon S3 Lifecycle rules with Amazon S3 Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html)
+  [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)

 **Related videos:**
+  [Simplify Your Data Lifecycle and Optimize Storage Costs With Amazon S3 Lifecycle](https://www.youtube.com/watch?v=53eHNSpaMJI)
+ [ Reduce Your Storage Costs Using Amazon S3 Storage Lens ](https://www.youtube.com/watch?v=A8qOBLM6ITY)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
