---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html
---

# Get started with Amazon EC2 Auto Scaling
<a name="get-started-with-ec2-auto-scaling"></a>

To get started with Amazon EC2 Auto Scaling, you can follow tutorials that introduce you to the service.

**Topics**
+ [Tutorial: Create your first Auto Scaling group](create-your-first-auto-scaling-group.md)
+ [Tutorial: Set up a scaled and load-balanced application](tutorial-ec2-auto-scaling-load-balancer.md)

For additional tutorials that focus on specific tools for managing the lifecycle of instances in an Auto Scaling group, see the following topics:
+ [Tutorial: Configure a lifecycle hook that invokes a Lambda function](tutorial-lifecycle-hook-lambda.md). This tutorial shows you how to use Amazon EventBridge to create rules that invoke Lambda functions based on events that happen to the instances in your Auto Scaling group.
+ [Tutorial: Use data script and instance metadata to retrieve lifecycle state](tutorial-lifecycle-hook-instance-metadata.md). This tutorial shows you how to use the Instance Metadata Service (IMDS) to invoke an action from within the instance itself.

Before you create an Auto Scaling group for use with your application, review your application thoroughly as it runs in the AWS Cloud. Consider the following:
+ How many Availability Zones the Auto Scaling group should span.
+ What existing resources can be used, such as security groups or Amazon Machine Images (AMIs).
+ Whether you want to scale to increase or decrease capacity, or if you just want to ensure that a specific number of servers are always running. Keep in mind that Amazon EC2 Auto Scaling can do both simultaneously.
+ What metrics have the most relevance to your application's performance.
+ How long it takes to launch and provision a server.

The better you understand your application, the more effective you can make your Auto Scaling architecture.
