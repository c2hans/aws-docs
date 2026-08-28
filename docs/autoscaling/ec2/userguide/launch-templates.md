---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html
---

# Auto Scaling launch templates
<a name="launch-templates"></a>

A launch template is similar to a [launch configuration](launch-configurations.md), in that it specifies instance configuration information. It includes the ID of the Amazon Machine Image (AMI), the instance type, a key pair, security groups, and other parameters used to launch EC2 instances. However, defining a launch template instead of a launch configuration allows you to have multiple versions of a launch template.

With versioning of launch templates, you can create a subset of the full set of parameters. Then, you can reuse it to create other versions of the same launch template. For example, you can create a launch template that defines a base configuration without an AMI or user data script. After you create your launch template, you can create a new version and add the AMI and user data that has the latest version of your application for testing. This results in two versions of the launch template. Storing a base configuration helps you to maintain the required general configuration parameters. You can create a new version of your launch template from the base configuration whenever you want. You can also delete the versions used for testing your application when you no longer need them.

We recommend that you use launch templates to ensure that you're accessing the latest features and improvements. Not all Amazon EC2 Auto Scaling features are available when you use launch configurations. For example, you cannot create an Auto Scaling group that launches both Spot and On-Demand Instances or that specifies multiple instance types. You must use a launch template to configure these features. For more information, see [Auto Scaling groups with multiple instance types and purchase options](ec2-auto-scaling-mixed-instances-groups.md).

With launch templates, you can also use newer features of Amazon EC2. This includes Systems Manager parameters (AMI ID), the current generation of EBS Provisioned IOPS volumes (io2), EBS volume tagging, T2 Unlimited instances, Capacity Reservations, Capacity Blocks, and Dedicated Hosts, to name a few.

When you create a launch template, all parameters are optional. However, if a launch template does not specify an AMI, you cannot add the AMI when you create your Auto Scaling group. If you specify an AMI but no instance type, you can add one or more instance types when you create your Auto Scaling group.

**Topics**
+ [Permissions to work with launch templates](#launch-templates-permissions)
+ [API operations supported by launch templates](#launch-templates-api-operations)
+ [Create a launch template for an Auto Scaling group](create-launch-template.md)
+ [Create a launch template using advanced settings](advanced-settings-for-your-launch-template.md)
+ [Migrate your Auto Scaling groups to launch templates](migrate-to-launch-templates.md)
+ [Migrate AWS CloudFormation stacks to launch templates](migrate-launch-configurations-with-cloudformation.md)
+ [Examples for creating and managing launch templates with the AWS CLI](examples-launch-templates-aws-cli.md)
+ [Use AWS Systems Manager parameters instead of AMI IDs in launch templates](using-systems-manager-parameters.md)

## Permissions to work with launch templates
<a name="launch-templates-permissions"></a>

The procedures in this section assume that you already have the required permissions to create launch templates. For information about how an administrator grants you permissions, see [Control access to launch templates with IAM permissions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permissions-for-launch-templates.html) in the *Amazon EC2 User Guide*.

Note that if you do not have sufficient permissions to use and create resources specified in a launch template, you receive an error that you're not authorized to use the launch template when you try to specify it for an Auto Scaling group. For more information, see [Troubleshoot Amazon EC2 Auto Scaling: Launch templates](ts-as-launch-template.md).

For examples of IAM policies that let you call the `CreateAutoScalingGroup`, `UpdateAutoScalingGroup`, and `RunInstances` API operations with a launch template, see [Control Amazon EC2 launch template usage in Auto Scaling groups](ec2-auto-scaling-launch-template-permissions.md).

## API operations supported by launch templates
<a name="launch-templates-api-operations"></a>

For a list of API operations supported by launch templates, see [Amazon EC2 actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-ec2.html) in the *[Amazon EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
