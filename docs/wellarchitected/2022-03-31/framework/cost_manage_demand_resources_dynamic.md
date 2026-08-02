---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_manage_demand_resources_dynamic.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST09-BP03 Supply resources dynamically
<a name="cost_manage_demand_resources_dynamic"></a>

 Resources are provisioned in a planned manner. This can be demand-based, such as through automatic scaling, or time-based, where demand is predictable and resources are provided based on time. These methods result in the least amount of over or under-provisioning.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

You can use [AWS Auto Scaling](https://aws.amazon.com/autoscaling/), or incorporate scaling in your code with the [AWS API or SDKs](https://aws.amazon.com/developer/tools/). This reduces your overall workload costs by removing the operational cost from manually making changes to your environment, and can be performed much faster. This will ensure that the workload resourcing best matches the demand at any time.

**Demand-based supply:** Leverage the elasticity of the cloud to supply resources to meet changing demand. Take advantage of APIs or service features to programmatically vary the amount of cloud resources in your architecture dynamically. This allows you to scale components in your architecture, and automatically increase the number of resources during demand spikes to maintain performance, and decrease capacity when demand subsides to reduce costs.

[AWS Auto Scaling](https://aws.amazon.com/autoscaling/) helps you adjust your capacity to maintain steady, predictable performance at the lowest possible cost. It is a fully managed and free service that integrates with Amazon Elastic Compute Cloud (Amazon EC2) instances and Spot Fleets, Amazon Elastic Container Service (Amazon ECS), Amazon DynamoDB, and Amazon Aurora.

Auto Scaling provides automatic resource discovery to help find resources in your workload that can be configured, it has built-in scaling strategies to optimize performance, costs or a balance between the two, and provides predictive scaling to assist with regularly occurring spikes.

Auto Scaling can implement manual, scheduled or demand-based scaling. You can also use metrics and alarms from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to trigger scaling events for your workload. Typical metrics can be standard Amazon EC2 metrics, such as CPU utilization, network throughput, and [Elastic Load Balancing(ELB) ](https://aws.amazon.com/elasticloadbalancing/)observed request or response latency. When possible, you should use a metric that is indicative of customer experience, which is typically a custom metric that might originate from application code within your workload.

When architecting with a demand-based approach keep in mind two key considerations. First, understand how quickly you must provision new resources. Second, understand that the size of margin between supply and demand will shift. You must be ready to cope with the rate of change in demand and also be ready for resource failures.

[ELB](https://aws.amazon.com/elasticloadbalancing/) helps you to scale by distributing demand across multiple resources. As you implement more resources, you add them to the load balancer to take on the demand. Elastic Load Balancing has support for Amazon EC2 Instances, containers, IP addresses, and AWS Lambda functions.

**Time-based supply:** A time-based approach aligns resource capacity to demand that is predictable or well-defined by time. This approach is typically not dependent upon utilization levels of the resources. A time-based approach ensures that resources are available at the specific time they are required, and can be provided without any delays due to start-up procedures and system or consistency checks. Using a time-based approach, you can provide additional resources or increase capacity during busy periods.

You can use scheduled Auto Scaling to implement a time-based approach. Workloads can be scheduled to scale out or in at defined times (for example, the start of business hours) thus ensuring that resources are available when users or demand arrives.

You can also leverage the [AWS APIs and SDKs](https://aws.amazon.com/developer/tools/) and [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to automatically provision and decommission entire environments as you need them. This approach is well suited for development or test environments that run only in defined business hours or periods of time.

You can use APIs to scale the size of resources within an environment (vertical scaling). For example, you could scale up a production workload by changing the instance size or class. This can be achieved by stopping and starting the instance and selecting the different instance size or class. This technique can also be applied to other resources, such as Amazon Elastic Block Store (Amazon EBS) Elastic Volumes, which can be modified to increase size, adjust performance (IOPS) or change the volume type while in use.

When architecting with a time-based approach keep in mind two key considerations. First, how consistent is the usage pattern? Second, what is the impact if the pattern changes? You can increase the accuracy of predictions by monitoring your workloads and by using business intelligence. If you see significant changes in the usage pattern, you can adjust the times to ensure that coverage is provided.

**Implementation steps**
+ ** Configure time-based scheduling: **For predictable changes in demand, time-based scaling can provide the correct number of resources in a timely manner. It is also useful if resource creation and configuration is not fast enough to respond to changes on demand. Using the workload analysis configure scheduled scaling using AWS Auto Scaling.
+ ** Configure Auto Scaling: **To configure scaling based on active workload metrics, use Amazon Auto Scaling. Use the analysis and configure auto scaling to trigger on the correct resource levels, and ensure that the workload scales in the required time.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
+  [AWS Instance Scheduler](https://aws.amazon.com/answers/infrastructure-management/instance-scheduler/)
+  [Getting Started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html)
+  [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)
+  [Scheduled Scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html)
