---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_compute_use_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP06 Continually evaluate compute needs based on metrics
<a name="perf_select_compute_use_metrics"></a>

Use a data-driven approach to continually evaluate and optimize the compute resources for your workload over time.

 **Desired outcome:** Use system-level metrics to actively monitor the behavior and requirements of your workload over time. Evaluate the demands of your workload against available resources based on the collected data, and make changes to your compute environment to best match your workload's profile. For example, a workload might be observed over time to be more memory-intensive than initially specified, so moving to a different instance family or size could improve both performance and efficiency.

 **Common anti-patterns:**
+  Monitoring system-level metrics to gain insight into your workload and not re-evaluating compute needs.
+  Architecting your compute needs for peak workload requirements.
+  Oversizing the existing compute solution to meet scaling or performance requirements when moving to an alternative compute solution would more efficiently match your workload characteristics.

 **Benefits of establishing this best practice:** Optimized compute resources based on real-world data and your desired balance of cost and performance.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

Use a data-driven approach to optimize compute resources based on observed workload behavior. To achieve maximum performance and efficiency, use the data gathered over time from your workload to continually tune and optimize your resources. Look at the trends in your workload's usage of current resources and determine where you can make changes to better match your workload's needs. When resources are over-committed, system performance degrades, and when resources are not adequately used, the system is operating less efficiently and at a higher cost.

 To optimize performance and resource utilization, you need a unified operational view, real-time granular data, and a historical reference. You can create automated dashboards to visualize this data and derive operational and utilization insights.

 **Implementation steps**

1.  Collect compute-related metrics over time.

1.  Compare workload metrics against available resources in your selected compute solution.

1.  Determine any required configuration changes by right-sizing the existing solution or evaluating alternative compute solutions.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [PERF02-BP01 Evaluate the available compute options](perf_select_compute_evaluate_options.md)
+  [PERF02-BP02 Understand the available compute configuration options](perf_select_compute_config_options.md)
+  [PERF02-BP03 Collect compute-related metrics](perf_select_compute_collect_metrics.md)
+  [PERF02-BP04 Determine the required configuration by right-sizing](perf_select_compute_right_sizing.md)

 **Related documents:**
+  [Cloud Compute with AWS ](https://aws.amazon.com/products/compute/?ref=wellarchitected)
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
+  [EC2 Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
+  [Amazon ECS Containers: Amazon ECS Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html)
+  [Amazon EKS Containers: Amazon EKS Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html)
+ [ Best practices for working with AWS Lambda functions ](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-configuration)

 **Related videos:**
+  [Amazon EC2 foundations (CMP211-R2)](https://www.youtube.com/watch?v=kMMybKqC2Y0)
+  [Better, faster, cheaper compute: Cost-optimizing Amazon EC2 (CMP202-R1)](https://www.youtube.com/watch?v=_dvh4P2FVbw)
+  [Deliver high performance ML inference with AWS Inferentia (CMP324-R1)](https://www.youtube.com/watch?v=17r1EapAxpk)
+  [Optimize performance and cost for your AWS compute (CMP323-R1)](https://www.youtube.com/watch?v=zt6jYJLK8sg)
+  [Powering next-gen Amazon EC2: Deep dive into the Nitro system](https://www.youtube.com/watch?v=rUY-00yFlE4)
+ [ Selecting and optimizing Amazon EC2 instances ](https://www.youtube.com/watch?v=Vz0HZ6hlpgM)

 **Related examples:**
+  [Rightsizing with Compute Optimizer and Memory utilization enabled](https://www.wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/5_ec2_computer_opt/)
+  [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
