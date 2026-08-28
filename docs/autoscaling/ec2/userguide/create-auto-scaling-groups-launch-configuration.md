---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-auto-scaling-groups-launch-configuration.html
---

# Create Auto Scaling groups using launch configurations
<a name="create-auto-scaling-groups-launch-configuration"></a>

**Important**
Limitations:
As of **January 1, 2023**, new Amazon EC2 instance types are no longer supported in launch configurations. This includes support for any instance types added to an AWS Region after the initial Region launch.
Accounts created on or after **June 1, 2023** cannot create new launch configurations using the console.
Accounts created on or after **October 1, 2024** cannot create new launch configurations using any method (console, API, AWS CLI, or CloudFormation).
 Migrate to launch templates to make sure that you don’t need to create new launch configurations now or in the future. For information about migrating your Auto Scaling groups to launch templates, see [Migrate your Auto Scaling groups to launch templates](migrate-to-launch-templates.md).

If you have created a launch configuration or an EC2 instance, you can create an Auto Scaling group that uses a launch configuration as a configuration template for its EC2 instances. The launch configuration specifies information such as the AMI ID, instance type, key pair, security groups, and block device mapping for your instances. For information about creating launch configurations, see [Create a launch configuration](create-launch-config.md).

You must have sufficient permissions to create an Auto Scaling group. You must also have sufficient permissions to create the service-linked role that Amazon EC2 Auto Scaling uses to perform actions on your behalf if it does not yet exist. For examples of IAM policies that an administrator can use as a reference for granting you permissions, see [Identity-based policy examples](security_iam_id-based-policy-examples.md).

**Topics**
+ [Create an Auto Scaling group using a launch configuration](create-asg-launch-configuration.md)
+ [Create an Auto Scaling group from existing instance using the AWS CLI](create-asg-from-instance.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
