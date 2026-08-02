---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html
---

# Auto Scaling groups with multiple instance types and purchase options
<a name="ec2-auto-scaling-mixed-instances-groups"></a>

You can launch and automatically scale a fleet of On-Demand Instances and Spot Instances within a single Auto Scaling group. In addition to receiving discounts for using Spot Instances, you can use Reserved Instances or a Savings Plans to receive discounts on the regular On-Demand Instance pricing. These factors help you optimize your cost savings for EC2 instances and get the desired scale and performance for your application.

Spot Instances are spare capacity available at steep discounts compared to the EC2 On-Demand price. Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted. They can be used for various fault-tolerant and flexible applications. Examples include stateless web servers, API endpoints, big data and analytics applications, containerized workloads, CI/CD pipelines, high performance and high throughput computing (HPC/HTC), rendering workloads, and other flexible workloads.

For more information, see [Instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) in the *Amazon EC2 User Guide*.

**Topics**
+ [Setup overview for creating a mixed instances group](mixed-instances-groups-set-up-overview.md)
+ [Allocation strategies for multiple instance types](allocation-strategies.md)
+ [Create mixed instances group using attribute-based instance type selection](create-mixed-instances-group-attribute-based-instance-type-selection.md)
+ [Create a mixed instances group by manually choosing instance types](create-mixed-instances-group-manual-instance-type-selection.md)
+ [Configure an Auto Scaling group to use instance weights](ec2-auto-scaling-mixed-instances-groups-instance-weighting.md)
+ [Use multiple launch templates](ec2-auto-scaling-mixed-instances-groups-launch-template-overrides.md)
