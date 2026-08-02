---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-emr-hardware/scaling.html
---

# Choosing the automatic scaling approach
<a name="scaling"></a>

Elasticity is one of the major advantages of using Amazon EMR. There are two main options for automatically scaling your resources:
+ Managed scaling
+ A custom scaling policy

With either managed scaling or a custom automatic scaling policy, you can scale in and out your nodes so that you use only the resources you need. Scaling out is used to add more resources when you need more capacity. Scaling in results in cost efficiency by removing resources that are not being used. Within the Amazon EMR service, Amazon CloudWatch metrics are enabled to monitor your resources so you can scale your cluster. CloudWatch takes data points every 5 minutes.

There are different considerations for each of the automatic scaling approaches.

## Amazon EMR managed scaling
<a name="emr-managed-scaling"></a>

Use [Amazon EMR managed scaling](https://docs.aws.amazon.com/emr/latest/ManagementGuide/managed-scaling-console.html) if your workload meets the following criteria:
+ A managed experience is needed.
+ Amazon EMR 5.330 or later is used.
+ You need an evaluation frequency of 1 minute.
+ The solution uses instance fleets to have between one and five instance options.
+ The applications are based on Apache Spark, Apache Hive, or Apache Hadoop YARN.

## Custom automatic scaling
<a name="custom-automatic-scaling"></a>

Use a custom automatic scaling policy if your workload meets the following criteria:
+ You must control the metric for scaling.
+ Amazon EMR 4.0\+ is used.
+ There is no need for a high evaluation frequency.
+ There is no requirement to control the cooldown periods between consecutive resizes.
+ It is important to control how many instances to add or remove when scaling.
+ The solution needs custom scaling actions. For example, you might want to scale more than one node in one 5-minute period. Or you might want to adjust the cooldown period.
+ There is no restriction on using different instant types in an instance group.

## Tips when adding automatic scaling to your cluster
<a name="tips-when-adding-automatic-scaling-to-your-cluster"></a>
+ Be aware of the amount of data that you will process. Forecast using the case with the biggest size of data.
+ [Right-size](capacity.md) your cluster.
+ Choose a [storage type](storage.md) that fits your needs.
+ Understand the [metrics](https://docs.aws.amazon.com/emr/latest/ManagementGuide/UsingEMR_ViewingMetrics.html) for an Amazon EMR cluster.
+ Understand how to determine the [right metric](https://aws.amazon.com/blogs/big-data/best-practices-for-resizing-and-automatic-scaling-in-amazon-emr/) for scaling your cluster.
+ Decide whether you will be using Spot Instances, uniform instance groups, or instance fleets.
+ Based on the information and limitations, decide which type of scaling approach you prefer, Amazon EMR managed scaling or a custom automatic scaling policy.
+ Configure the managed scaling or custom policy.
+ If you selected a custom automatic scaling policy, monitor the Amazon EMR metrics for tuning the policy's thresholds.
