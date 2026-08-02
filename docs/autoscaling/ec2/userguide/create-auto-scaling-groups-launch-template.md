---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-auto-scaling-groups-launch-template.html
---

# Create Auto Scaling groups using launch templates
<a name="create-auto-scaling-groups-launch-template"></a>

If you have created a launch template, you can create an Auto Scaling group that uses a launch template as a configuration template for its EC2 instances. The launch template specifies information such as the AMI ID, instance type, key pair, security groups, and block device mapping for your instances. For information about creating launch templates, see [Create a launch template for an Auto Scaling group](create-launch-template.md).

You must have sufficient permissions to create an Auto Scaling group. You must also have sufficient permissions to create the service-linked role that Amazon EC2 Auto Scaling uses to perform actions on your behalf if it does not yet exist. For examples of IAM policies that an administrator can use as a reference for granting you permissions, see [Identity-based policy examples](security_iam_id-based-policy-examples.md) and [Control Amazon EC2 launch template usage in Auto Scaling groups](ec2-auto-scaling-launch-template-permissions.md).

**Topics**
+ [Create an Auto Scaling group using a launch template](create-asg-launch-template.md)
+ [Create an Auto Scaling group using the Amazon EC2 launch wizard](create-asg-ec2-wizard.md)
+ [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md)
