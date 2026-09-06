---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_compute_right_sizing.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP04 Determine the required configuration by right-sizing
<a name="perf_select_compute_right_sizing"></a>

Analyze the various performance characteristics of your workload and how these characteristics relate to memory, network, I/O, and CPU usage. Use this data to choose resources that best match your workload’s profile. For example, a memory-intensive workload like a database may benefit from a higher memory per core ratio. However, a compute intensive workload may need a higher core count and frequency, but can be satisfied with a lower amount of memory per core.

 **Common anti-patterns:**
+  You choose an instance with the largest values across all performance characteristics available for all workloads.
+  You standardize all instances types to one type for ease of management.
+  You optimize against standard synthetic benchmarks without validating the actual requirements of a particular workload.
+  You keep the same infrastructure for a long period of time without reevaluating and integrating new offerings.

 **Benefits of establishing this best practice:** When you are familiar with the requirements of your workload, you can compare these needs with available compute offerings and quickly experiment to determine which ones meet the needs of your workload most efficiently. This allows for optimal performance without overpaying for resources not required.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Modify your workload configuration by right sizing. To optimize performance, overall efficiency, and cost effectiveness, determine first which resources your workload needs. Choose memory-optimized instances, such as the R-family of instances, for memory-intensive workloads like a database. For workloads that require higher compute capacity, choose the C-family of instances, or choose instances with higher core counts or higher core frequency. Choose I/O performance based on the needs of your workload instead of comparing against standard, synthetic benchmarks. For higher I/O performance, choose instances from the I-family of instances, [select I/O optimized Amazon EBS volumes](https://aws.amazon.com/premiumsupport/knowledge-center/optimize-ebs-provisioned-iops/), or choose instances with [instance store](https://aws.amazon.com/premiumsupport/knowledge-center/instance-store-vs-ebs/). For more detail on particular instance types, see [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/).

 Right sizing verifies that your workloads perform as well as possible while not overpaying on resources not needed.

 **Implementation steps**
+  Know your workload or analyze its resource requirements.
+  Evaluate workloads separately. The AWS Cloud gives you flexibility and agility to right-size each workload on its own without needing to compromise.
+  Create test environments to find the best match of compute offerings against your workload.
+  Continually reevaluate new compute offerings, and compare against your workload’s needs.
+  Routinely review new service offers for better price performance.
+  Regularly conduct Well-Architected Framework Reviews.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [PERF02-BP03 Collect compute-related metrics](perf_select_compute_collect_metrics.md)
+  [PERF02-BP06 Continually evaluate compute needs based on metrics](perf_select_compute_use_metrics.md)

 **Related documents:**
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
+  [Cloud Compute with AWS](https://aws.amazon.com/products/compute/)
+  [Amazon EC2 Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
+  [Amazon ECS Containers: Amazon ECS Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html)
+  [Amazon EKS Containers: Amazon EKS Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html)
+  [Functions: Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-configuration)

 **Related videos:**
+  [Amazon EC2 foundations (CMP211-R2)](https://www.youtube.com/watch?v=kMMybKqC2Y0)
+  [Better, faster, cheaper compute: Cost-optimizing Amazon EC2 (CMP202-R1)](https://www.youtube.com/watch?v=_dvh4P2FVbw)
+  [Deliver high performance ML inference with AWS Inferentia (CMP324-R1)](https://www.youtube.com/watch?v=17r1EapAxpk)
+  [Optimize performance and cost for your AWS compute (CMP323-R1)](https://www.youtube.com/watch?v=zt6jYJLK8sg)
+  [Powering next-gen Amazon EC2: Deep dive into the Nitro system](https://www.youtube.com/watch?v=rUY-00yFlE4)
+  [How to choose compute option for startups](https://aws.amazon.com/startups/start-building/how-to-choose-compute-option/)
+  [Optimize performance and cost for your AWS compute (CMP323-R1)](https://www.youtube.com/watch?v=zt6jYJLK8sg)

 **Related examples:**
+  [Rightsizing with Compute Optimizer and Memory utilization enabled](https://www.wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/5_ec2_computer_opt/)
+  [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
