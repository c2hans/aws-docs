---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_select_compute_elasticity.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP05 Use the available elasticity of resources
<a name="perf_select_compute_elasticity"></a>

 The cloud provides the flexibility to expand or reduce your resources dynamically through a variety of mechanisms to meet changes in demand. Combined with compute-related metrics, a workload can automatically respond to changes and use the optimal set of resources to achieve its goal.

 Optimally matching supply to demand delivers the lowest cost for a workload, but you also must plan for sufficient supply to allow for provisioning time and individual resource failures. Demand can be fixed or variable, requiring metrics and automation to ensure that management does not become a burdensome and disproportionately large cost.

 With AWS, you can use a number of different approaches to match supply with demand. The Cost Optimization Pillar whitepaper describes how to use the following approaches to cost:
+  Demand-based approach
+  Buffer-based approach
+  Time-based approach

 You must ensure that workload deployments can handle both scale-up and scale-down events. Create test scenarios for scale-down events to ensure that the workload behaves as expected.

 **Common anti-patterns:**
+  You react to alarms by manually increasing capacity.
+  You leave increased capacity after a scaling event instead of scaling back down.

 **Benefits of establishing this best practice:** Configuring and testing workload elasticity will help save money, maintain performance benchmarks, and improves reliability as traffic changes. Most non-production instances should be stopped when they are not being used. Although it's possible to manually shut down unused instances, this is impractical at larger scales. You can also take advantage of volume-based elasticity, which allows you to optimize performance and cost by automatically increasing the number of compute instances during demand spikes and decreasing capacity when demand decreases.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Take advantage of elasticity: Elasticity matches the supply of resources you have against the demand for those resources. Instances, containers, and functions provide mechanisms for elasticity either in combination with automatic scaling or as a feature of the service. Use elasticity in your architecture to ensure that you have sufficient capacity to meet performance requirements at all scales of use. Ensure that the metrics for scaling up or down elastic resources are validated against the type of workload being deployed. If you are deploying a video transcoding application, 100% CPU utilization is expected and should not be your primary metric. Alternatively, you can measure against the queue depth of transcoding jobs waiting to scale your instance types. Ensure that workload deployments can handle both scale up and scale down events. Scaling down workload components safely is as critical as scaling up resources when demand dictates. Create test scenarios for scale-down events to ensure that the workload behaves as expected.

## Resources
<a name="resources"></a>

 **Related documents:**
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

 **Related examples:**
+  [Amazon EC2 Auto Scaling Group Examples](https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples)
+  [Amazon EFS Tutorials](https://github.com/aws-samples/amazon-efs-tutorial)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
