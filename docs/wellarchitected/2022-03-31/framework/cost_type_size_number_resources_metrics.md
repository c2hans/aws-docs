---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_type_size_number_resources_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST06-BP03 Select resource type, size, and number automatically based on metrics
<a name="cost_type_size_number_resources_metrics"></a>

 Use metrics from the currently running workload to select the right size and type to optimize for cost. Appropriately provision throughput, sizing, and storage for services such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon DynamoDB, Amazon Elastic Block Store (Amazon EBS) (PIOPS), Amazon Relational Database Service (Amazon RDS), Amazon EMR, and networking. This can be done with a feedback loop such as automatic scaling or by custom code in the workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Create a feedback loop within the workload that uses active metrics from the running workload to make changes to that workload. You can use a managed service, such as [AWS Auto Scaling](https://aws.amazon.com/autoscaling/), which you configure to perform the right sizing operations for you. AWS also provides [APIs, SDKs](https://aws.amazon.com/developer/tools/), and features that allow resources to be modified with minimal effort. You can program a workload to stop-and-start an Amazon Elastic Compute Cloud(Amazon EC2) instance to allow a change of instance size or instance type. This provides the benefits of right-sizing while removing almost all the operational cost required to make the change.

Some AWS services have built in automatic type or size selection, such as [Amazon Simple Storage Service(Amazon S3) Intelligent-Tiering](https://aws.amazon.com/about-aws/whats-new/2018/11/s3-intelligent-tiering/). Amazon S3 Intelligent-Tiering automatically moves your data between two access tiers: frequent access and infrequent access, based on your usage patterns.

**Implementation steps**
+ ** Configure workload metrics: **Ensure you capture the key metrics for the workload. These metrics provide an indication of the customer experience, such as the workload output, and align to the differences between resource types and sizes, such as CPU and memory usage.
+ ** View rightsizing recommendations: **Use the rightsizing recommendations in AWS Compute Optimizer to make adjustments to your workload.
+ ** Select resource type and size automatically based on metrics: **Using the workload metrics, manually or automatically select your workload resources. Configuring AWS Auto Scaling or implementing code within your application can reduce the effort required if frequent changes are needed, and it can potentially implement changes sooner than a manual process.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
+  [Amazon CloudWatch features](https://aws.amazon.com/cloudwatch/features/)
+  [CloudWatch Getting Set Up](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html)
+  [CloudWatch Publishing Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
+  [Cost Optimization: Amazon EC2 Right Sizing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html)
+  [Getting Started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html)
+  [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/about-aws/whats-new/2018/11/s3-intelligent-tiering/)
+  [Launch an EC2 Instance Using the SDK](https://docs.aws.amazon.com/sdk-for-net/v2/developer-guide/run-instance.html)
