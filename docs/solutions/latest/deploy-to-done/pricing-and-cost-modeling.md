---
source_url: https://docs.aws.amazon.com/solutions/latest/deploy-to-done/pricing-and-cost-modeling.html
---

# Pricing and Cost Modeling
<a name="pricing-and-cost-modeling"></a>

Elastic Beanstalk has no service fee in either deployment mode. You pay only for the underlying AWS resources your applications consume. Both modes run your application on Amazon EC2 compute, billed at standard EC2 rates, and you can use On-Demand Instances, Reserved Instances, Savings Plans, or Spot Instances.

**What you pay for:**

**What you pay for**

| Resource | Standard Mode | Cluster Mode |
| --- | --- | --- |
| Compute | EC2 instances you select, billed at standard EC2 rates | EC2 compute matched to the CPU and memory you allocate, billed at standard EC2 rates |
| Load balancing | Application, Network, or Classic Load Balancer for load-balanced environments (a single-instance environment has none) | One Application Load Balancer per environment |
| Storage | EBS volumes per instance | Container image storage (Amazon ECR) |
| Managed foundation | None | Two additional charges: a flat Amazon EKS control-plane fee per cluster, and an Amazon EKS Auto Mode management fee on the compute it provisions |
| Monitoring | CloudWatch (basic instance metrics included; custom metrics and logs at standard rates) | CloudWatch, metered per pod and container; Amazon Managed Service for Prometheus available as a lower-cost alternative at scale |

**Understanding the Cluster Mode managed foundation charges:**

Cluster Mode runs your applications on a managed Amazon EKS foundation, which adds two charges that Standard Mode does not have:
+ **Amazon EKS control-plane fee:** a flat hourly fee per cluster for the managed control plane. It does not scale with instance size, node count, or the number of applications. Applications deployed into the same subnet share a cluster, so you generally pay one cluster fee rather than one per application.
+ **Amazon EKS Auto Mode management fee:** a fee on top of the EC2 instance cost for provisioning, scaling, and patching the underlying nodes. This management fee is charged independently of your EC2 purchase option, so Reserved Instances, Savings Plans, and Spot discounts reduce the instance cost but not the Auto Mode fee.

**When each mode is more cost-efficient:**

For a single application at low traffic, Standard Mode on dedicated compute is typically more cost-efficient, because the EKS control-plane fee and Auto Mode management fee add a baseline that a single application cannot offset. AWS guidance places this crossover around workloads spending under $500 per month. The cost advantage of Cluster Mode emerges at portfolio scale, where multiple applications share managed infrastructure and can use less total compute than running each on its own dedicated instance.

**Free tier:** The AWS Free Tier offer applies to Standard Mode only, for new AWS accounts during the 6-month Free Tier period. Cluster Mode is not Free Tier eligible.

**Cost optimization levers:**
+ **Reserved Instances, Savings Plans, or Spot Instances** reduce EC2 compute costs for predictable or fault-tolerant workloads (note these discounts apply to the instance cost, not the Cluster Mode Auto Mode management fee)
+ **Shared infrastructure in Cluster Mode** lets multiple applications share nodes, so a portfolio can use less total compute than one dedicated instance per application
+ **Right-sizing** through managed scaling ensures you are not over-provisioning during low-traffic periods
+ **Amazon Managed Service for Prometheus** is available as a lower-cost alternative to CloudWatch for metrics at scale in Cluster Mode
+ **No platform fee** means your only costs are the AWS resources your applications actually use

## Go Deeper
<a name="pricing-go-deeper"></a>

**Go Deeper**
[AWS Elastic Beanstalk Pricing](https://aws.amazon.com/elasticbeanstalk/pricing/) - Official pricing page, including the managed foundation charges
[Amazon EKS Pricing](https://aws.amazon.com/eks/pricing/) - EKS control-plane and Auto Mode fee details
[AWS Elastic Beanstalk FAQs: Pricing Section](https://aws.amazon.com/elasticbeanstalk/faqs/) - Common cost questions
