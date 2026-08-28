---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_compute_elasticity.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP05 Use the available elasticity of resources
<a name="perf_select_compute_elasticity"></a>

The cloud provides the flexibility to expand and reduce your resources dynamically through a variety of mechanisms to meet changes in demand. Combining this elasticity with compute-related metrics, a workload can automatically respond to changes to use the resources it needs and only the resources it needs.

 **Common anti-patterns:**
+  You overprovision to cover possible spikes.
+  You react to alarms by manually increasing capacity.
+  You increase capacity without considering provisioning time.
+  You leave increased capacity after a scaling event instead of scaling back down.
+  You monitor metrics that don’t directly reflect your workloads true requirements.

 **Benefits of establishing this best practice:** Demand can be fixed, variable, follow a pattern or be spiky. Matching supply to demand delivers the lowest cost for a workload. Monitoring, testing, and configuring workload elasticity will optimize performance, save money, and improve reliability as usage demands change. Although a manual approach to this is possible, it is impractical at larger scales. An automated and metrics-based approach assures resources meet demands and any given time.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Metric based automation should be used to take advantage of elasticity with the goal that the supply of resources you have matches the demand of the resources your workload requires. For example, you can use [Amazon CloudWatch metrics to monitor your resources](https://aws.amazon.com/startups/start-building/how-to-monitor-resources/), or use Amazon CloudWatch metrics for your Auto Scaling groups.

 Combined with compute-related metrics, a workload can automatically respond to changes and use the optimal set of resources to achieve its goal. You also must plan for provisioning time and potential resource failures.

 Instances, containers, and functions provide mechanisms for elasticity either as a feature of the service, in the form of [Application Auto Scaling](https://aws.amazon.com/autoscaling/), or in combination with [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html). Use elasticity in your architecture to verify that you have sufficient capacity to meet performance requirements at a wide variety of scales of use.

 Validate your metrics for scaling up or down elastic resources against the type of workload being deployed. As an example, if you are deploying a video transcoding application, 100% CPU utilization is expected and should not be your primary metric. Alternatively, you can measure against the queue depth of transcoding jobs waiting to scale your instance types.

 Workload deployments need to handle both scale up and scale down events. Scaling down workload components safely is as critical as scaling up resources when demand dictates.

 Create test scenarios for scaling events to verify that the workload behaves as expected.

 **Implementation steps**
+  Leverage historical data to analyze your workload’s resource demands over time. Ask specific questions like:
  +  Is your workload steady and increasing over time at a known rate?
  +  Does your workload increase and decrease in seasonal, repeatable patterns?
  +  Is your workload spiky? Can the spikes be anticipated or predicted?
+  Leverage monitoring services and historical data as much as possible.
+  Tagging resources can help with monitoring. When using tags, refer to [tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html). Additionally, [tags can help you manage, identify, and organize resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
+  With AWS, you can use a number of different approaches to match supply with demand. The cost optimization pillar best practices ([COST09-BP01 through COST09-03](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/manage-demand-and-supply-resources.html)) describe how to use the following approaches to cost:
  + [ COST09-BP01 Perform an analysis on the workload demand ](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_cost_analysis.html)
  + [ COST09-BP02 Implement a buffer or throttle to manage demand ](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_buffer_throttle.html)
  + [ COST09-BP03 Supply resources dynamically ](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_dynamic.html)
+  Create test scenarios for scale down events to verify that the workload behaves as expected.
+  Most non-production instances should be stopped when they are not being used.
+  For storage needs when using Amazon Elastic Block Store (Amazon EBS), take advantage of [volume-based elasticity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html).
+  For [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), consider using [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html), which allow you to optimize performance and cost by automatically increasing the number of compute instances during demand spikes and decreasing capacity when demand decreases.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [PERF02-BP03 Collect compute-related metrics](perf_select_compute_collect_metrics.md)
+  [PERF02-BP04 Determine the required configuration by right-sizing](perf_select_compute_right_sizing.md)
+  [PERF02-BP06 Continually evaluate compute needs based on metrics](perf_select_compute_use_metrics.md)

 **Related documents:**
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

 **Related examples:**
+  [Amazon EC2 Auto Scaling Group Examples](https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples)
+  [Amazon EFS Tutorials](https://github.com/aws-samples/amazon-efs-tutorial)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
