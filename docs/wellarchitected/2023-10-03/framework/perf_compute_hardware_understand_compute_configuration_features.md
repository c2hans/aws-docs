---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_compute_hardware_understand_compute_configuration_features.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP02 Understand the available compute configuration and features
<a name="perf_compute_hardware_understand_compute_configuration_features"></a>

 Understand the available configuration options and features for your compute service to help you provision the right amount of resources and improve performance efficiency.

 **Common anti-patterns:**
+  You do not evaluate compute options or available instance families against workload characteristics.
+  You over-provision compute resources to meet peak-demand requirements.

** Benefits of establishing this best practice:** Be familiar with AWS compute features and configurations so that you can use a compute solution optimized to meet your workload characteristics and needs.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Each compute solution has unique configurations and features available to support different workload characteristics and requirements. Learn how these options complement your workload, and determine which configuration options are best for your application. Examples of these options include instance family, sizes, features (GPU, I/O), bursting, time-outs, function sizes, container instances, and concurrency. If your workload has been using the same compute option for more than four weeks and you anticipate that the characteristics will remain the same in the future, you can use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)  to find out if your current compute option is suitable for the workloads from CPU and memory perspective.

## Implementation steps
<a name="implementation-steps"></a>

1.  Understand workload requirements (like CPU need, memory, and latency).

1.  Review AWS documentation and best practices to learn about recommended configuration options that can help improve compute performance. Here are some key configuration options to consider:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_compute_hardware_understand_compute_configuration_features.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Cloud Compute with AWS ](https://aws.amazon.com/products/compute/?ref=wellarchitected)
+  [Amazon EC2 Instance Types ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html?ref=wellarchitected)
+  [Processor State Control for Your Amazon EC2 Instance ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html?ref=wellarchitected)
+  [Amazon EKS Containers: Amazon EKS Worker Nodes ](https://docs.aws.amazon.com/eks/latest/userguide/worker.html?ref=wellarchitected)
+  [Amazon ECS Containers: Amazon ECS Container Instances ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html?ref=wellarchitected)
+  [Functions: Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html?ref=wellarchitected#function-configuration)

 **Related videos:**
+  [Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0&ref=wellarchitected)
+  [Powering next-gen Amazon EC2: Deep dive into the Nitro system ](https://www.youtube.com/watch?v=rUY-00yFlE4&ref=wellarchitected)
+  [Optimize performance and cost for your AWS compute](https://www.youtube.com/watch?v=zt6jYJLK8sg&ref=wellarchitected)

 **Related examples:**
+  [Rightsizing with Compute Optimizer and Memory utilization enabled](https://www.wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/5_ec2_computer_opt/)
+  [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
