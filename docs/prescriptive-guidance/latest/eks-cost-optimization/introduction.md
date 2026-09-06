---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/eks-cost-optimization/introduction.html
---

# EKS cost optimization: Scaling, sizing, and savings
<a name="introduction"></a>

*abhay kumar, Akash Kumar, Vinodkumar Mandalapu, and Viyoma Sachdeva, Amazon Web Services*

[Amazon Elastic Kubernetes Service (Amazon EKS) ](https://aws.amazon.com/eks/)makes running Kubernetes easier, but without deliberate cost management, compute spend can grow quickly. Idle nodes, over-provisioned pods, extended support charges, and high-cardinality metrics all add up silently. This guide walks through practical strategies to identify and eliminate that waste. From [Karpenter](https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html) consolidation and [Graviton](https://aws.amazon.com/ec2/graviton/) adoption to right-sizing pod requests and cutting observability overhead, we cover the full cost surface. Every recommendation includes real [kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) commands, [AWS CLI](https://aws.amazon.com/cli/) examples, and [CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) so you can measure impact immediately. Whether you're running 3 clusters or 300, these patterns apply at any scale.

Code repository: The shell scripts and Kubernetes manifests for this guide are available in the [eks-cost-optimization-guide](https://github.com/aws-samples/sample-eks-cost-optimization-guide) repository on GitHub.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for platform engineers, DevOps engineers, and cloud architects who manage Amazon EKS clusters and are responsible for controlling compute and observability costs.

## Business challenge
<a name="overview"></a>

Organizations running Amazon EKS clusters often face significant and compounding cost challenges that erode cloud ROI:
+ **Idle resources** : Clusters running without active application workloads continue consuming compute capacity, accumulating charges with zero business value.
+ **Over-provisioning** : Applications configured with excessive CPU and memory requests reserve capacity they never use, preventing efficient bin-packing across nodes.
+ **Inefficient autoscaling :** Traditional Cluster Autoscaler configurations with conservative or suboptimal settings respond slowly to demand changes, keeping unnecessary nodes running for extended periods.
+ **Legacy architectures **: Workloads remain pinned to x86 instances by default, missing the 20% price-performance improvement available through AWS Graviton processors.
+ **Monitoring overhead** : High-cardinality custom metrics, verbose logging, and unfiltered Container Insights generate substantial CloudWatch and observability platform costs that grow linearly with cluster size.
+ **Manual management **: Without automation for resource optimization, node lifecycle, and off-hours scheduling, cost inefficiencies persist undetected and unresolved.

These challenges compound across environments. Typical Kubernetes clusters operate at only 20–30% resource utilization while paying for 100% of provisioned capacity, meaning up to 70% of compute spend delivers no workload value. At scale, this translates to tens or hundreds of thousands of dollars in annual cloud waste per organization.

## Service limitations
<a name="service-limitations"></a>

Some AWS services aren't available in all AWS Regions. For Region availability, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page in the AWS documentation, and choose the link for the service.

## Pricing disclaimer
<a name="pricing-disclaimer"></a>

The pricing examples in this guide are based on prices at the time of publication. Prices are subject to change. Additionally, your costs may vary depending on your AWS Region, AWS service quotas, and other factors related to your cloud environment.
