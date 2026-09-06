---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_select_compute_right_sizing.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP04 Determine the required configuration by right-sizing
<a name="perf_select_compute_right_sizing"></a>

 Analyze the various performance characteristics of your workload and how these characteristics relate to memory, network, and CPU usage. Use this data to choose resources that best match your workload's profile. For example, a memory-intensive workload, such as a database, could be served best by the r-family of instances. However, a bursting workload can benefit more from an elastic container system.

 **Common anti-patterns:**
+  You choose the largest instance available for all workloads.
+  You standardize all instances types to one type for ease of management.

 **Benefits of establishing this best practice:** Being familiar with the AWS compute offerings allows you to determine the correct solution for your various workloads. After you have selected the various compute offerings for your workload, you have the agility to quickly experiment with those compute offerings to determine which ones meet the needs of your workload.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Modify your workload configuration by right sizing: To optimize both performance and overall efficiency, determine which resources your workload needs. Choose memory-optimized instances for systems that require more memory than CPU, or compute-optimized instances for components that do data processing that is not memory-intensive. Right sizing enables your workload to perform as well as possible while only using the required resources

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
+  [Cloud Compute with AWS](https://aws.amazon.com/products/compute/)
+  [EC2 Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
+  [ECS Containers: Amazon ECS Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html)
+  [EKS Containers: EKS Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html)
+  [Functions: Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-configuration)
+  [Processor State Control for Your EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html)

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
