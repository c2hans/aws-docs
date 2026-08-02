---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/capacity-management.html
---

# Capacity management
<a name="capacity-management"></a>

 You can monitor Outpost EC2 instance pool utilization in the AWS Management Console and via Amazon CloudWatch metrics. Contact Enterprise Support to retrieve or change the slotting layouts for your Outposts.

 You use the same [instance auto recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) and [EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) mechanisms to recover or replace instances impacted by server failures and maintenance events. You must monitor and manage your Outpost capacity to ensure sufficient spare capacity is always available to accommodate server failures. The [https://aws.amazon.com/blogs/compute/managing-your-aws-outposts-capacity-using-amazon-cloudwatch-and-aws-lambda/](https://aws.amazon.com/blogs/compute/managing-your-aws-outposts-capacity-using-amazon-cloudwatch-and-aws-lambda/) blog post provides a hands-on tutorial showing you how to combine AWS CloudWatch and AWS Lambda to manage your Outpost capacity to maintain instance availability.

![Diagram showing Managing AWS Outposts capacity with Amazon CloudWatch and AWS Lambda](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/managing-outposts-capacity.png)

Capacity Reservations can be used in a multi-account environment to control how much of your Outpost compute capacity is used by a single account, or an AWS Organization unit (OU) containing multiple accounts. You can create a capacity reservation for Amazon EC2 on Outposts, as well as supported Outposts AWS services such as Amazon Elastic Kubernetes Service (EKS, Amazon Elastic Container Service (ECS), and Amazon Elastic Map Reduce (EMR). Capacity reservations are created and shared to accounts through AWS Resource Access Manager (AWS RAM) in the Outpost owner account. The [Creating computing quotas on AWS Outposts rack with EC2 Capacity Reservations sharing](https://aws.amazon.com/blogs/compute/creating-computing-quotas-on-aws-outposts-rack-with-ec2-capacity-reservation-sharing/) provides a hands-on tutorial and additional guidance for implementing capacity reservations with your Outpost for the purpose of capacity management.

![Diagram showing Capacity Reservation sharing process steps 1-4](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-36-capacity-reservation-sharing-process-steps-1-4.png)

![Diagram showing Capacity Reservation sharing process steps 5-6](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-37-capacity-reservation-sharing-process-steps-5-6.png)

## Recommended practices for compute capacity management
<a name="recommended-practices-for-compute-capacity-management"></a>
+  Configure your EC2 instances in Auto Scaling groups or use instance auto recovery to restart failed instances.
+  Automate capacity monitoring for your Outpost deployments and configure notifications and (optionally) automated responses for capacity alarms.
+ Use Capacity Reservations to have granular control over how much compute capacity is shared to other accounts within your AWS Organization.
