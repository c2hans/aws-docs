---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/scale-your-group.html
---

# Increase or decrease compute capacity of your application with scaling
<a name="scale-your-group"></a>

*Scaling* is the ability to increase or decrease the compute capacity of your application. Scaling starts with an event, or scaling action, which instructs an Auto Scaling group to either launch or terminate Amazon EC2 instances.

Amazon EC2 Auto Scaling provides a number of ways to adjust scaling to best meet the needs of your applications. As a result, it's important that you have a good understanding of your application. Keep the following considerations in mind:
+ What role should Amazon EC2 Auto Scaling play in your application's architecture? It's common to think about automatic scaling primarily as a way to increase and decrease capacity, but it's also useful for maintaining a steady number of servers.
+ What cost constraints are important to you? Because Amazon EC2 Auto Scaling uses EC2 instances, you pay only for the resources that you use. Knowing your cost constraints helps you decide when to scale your applications, and by how much.
+ What metrics are important to your application? Amazon CloudWatch supports a number of different metrics that you can use with your Auto Scaling group.

**Topics**
+ [Choose your scaling method](scaling-overview.md)
+ [Set scaling limits](asg-capacity-limits.md)
+ [Set the default instance warmup](ec2-auto-scaling-default-instance-warmup.md)
+ [Manual scaling](ec2-auto-scaling-scaling-manually.md)
+ [Scheduled scaling](ec2-auto-scaling-scheduled-scaling.md)
+ [Dynamic scaling](as-scale-based-on-demand.md)
+ [Predictive scaling](ec2-auto-scaling-predictive-scaling.md)
+ [Control instance termination](as-instance-termination.md)
+ [Suspend-resume processes](as-suspend-resume-processes.md)
