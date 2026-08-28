---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/security-iam-awsmanpol.html
---

# AWS managed policies for Amazon EC2 Auto Scaling
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## Amazon EC2 Auto Scaling managed policies
<a name="predefined-policies-auto-scaling"></a>

You can attach the following managed policies to your AWS Identity and Access Management (IAM) identities (users or roles). Each policy provides access to all or some of the API actions for Amazon EC2 Auto Scaling.
+ [AutoScalingConsoleFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AutoScalingConsoleFullAccess.html) – Grants full access to Amazon EC2 Auto Scaling using the AWS Management Console. This policy works when you are using launch configurations, but not when you are using launch templates.
+ [AutoScalingConsoleReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AutoScalingConsoleReadOnlyAccess.html) – Grants read-only access to Amazon EC2 Auto Scaling using the AWS Management Console. This policy works when you are using launch configurations, but not when you are using launch templates.
+ [AutoScalingFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AutoScalingFullAccess.html) – Grants full access to Amazon EC2 Auto Scaling for IAM identities that need full Amazon EC2 Auto Scaling access from the AWS CLI or SDKs, but not AWS Management Console access.
+ [AutoScalingReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AutoScalingReadOnlyAccess.html) – Grants read-only access to Amazon EC2 Auto Scaling for IAM identities that are making calls only to the AWS CLI or SDKs.

When you are using launch templates from the console, you need to grant additional permissions specific to launch templates, which are discussed in [Control Amazon EC2 launch template usage in Auto Scaling groups](ec2-auto-scaling-launch-template-permissions.md). The Amazon EC2 Auto Scaling console needs permissions for `ec2` actions so it can display information about launch templates and launch instances using launch templates.

## AutoScalingServiceRolePolicy AWS managed policy
<a name="service-linked-role-policy"></a>

This policy is attached to a service-linked role that allows Amazon EC2 Auto Scaling to perform actions on your behalf. For more information, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md).

To view the permissions for this policy, see [AutoScalingServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AutoScalingServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Amazon EC2 Auto Scaling updates to AWS managed policies
<a name="policy-updates"></a>

View details about updates to AWS managed policies for Amazon EC2 Auto Scaling since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon EC2 Auto Scaling Document history page.

| Change | Description | Date |
| --- | --- | --- |
| Amazon EC2 Auto Scaling updates permissions to its service-linked role | The `AutoScalingServiceRolePolicy` policy now includes the `ec2:CreateReplaceRootVolumeTask` permission that allows you to replace root volumes on instances as part of an instance refresh. Additionally, the `events:DescribeRule` permission has been removed from the policy. For more information, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md). | November 18, 2025 |
| Amazon EC2 Auto Scaling adds permissions to its service-linked role | The `AutoScalingServiceRolePolicy` policy now includes permission to call the AWS Resource Groups [ListGroupResources](https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListGroupResources.html) API action to get all resource names (ARNs) of the resources that are members of a specified resource group. For more information, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md). | November 20, 2024 |
| Amazon EC2 Auto Scaling adds permissions to its service-linked role | The `AutoScalingServiceRolePolicy` policy now grants permissions to call the Amazon EC2 [GetSecurityGroupsForVpc](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSecurityGroupsForVpc.html) API action to get all security groups for a VPC to improve validation, and the Amazon EC2 [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) API action to get information about which instance types meet a certain set of instance requirements. For more information, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md). | February 29, 2024 |
| Amazon EC2 Auto Scaling adds permissions to its service-linked role | The `AutoScalingServiceRolePolicy` policy now grants permissions to the service to access the API actions it needs for an integration with VPC Lattice.+  `GetTargetGroup` and `ListTargetGroup` actions. Required to retrieve information about VPC Lattice target groups. <br />+  `RegisterTargets` and `DeregisterTargets` actions. Required to register and deregister instances from VPC Lattice target groups. <br />+  `ListTargets`. Allows Amazon EC2 Auto Scaling to retrieve health information for instances registered to VPC Lattice target groups. <br />For more information, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md). | December 6, 2022 |
| Amazon EC2 Auto Scaling adds permissions to its service-linked role | To support using an AWS Systems Manager Parameter as an alias for an AMI ID when creating a launch template, the `AutoScalingServiceRolePolicy` policy now grants permission to call the AWS Systems Manager [GetParameters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetParameters.html) API action. For more information, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md). | March 28, 2022 |
| Amazon EC2 Auto Scaling adds permissions to its service-linked role | To support predictive scaling, the `AutoScalingServiceRolePolicy` policy now includes permission to call the CloudWatch [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) API action. For more information, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md). | May 19, 2021 |
| Amazon EC2 Auto Scaling started tracking changes | Amazon EC2 Auto Scaling started tracking changes for its AWS managed policies. | May 19, 2021 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
