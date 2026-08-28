---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/control-access-using-iam.html
---

# How Amazon EC2 Auto Scaling works with IAM
<a name="control-access-using-iam"></a>

Before you use IAM to manage access to Amazon EC2 Auto Scaling, learn what IAM features are available to use with Amazon EC2 Auto Scaling.

**IAM features you can use with Amazon EC2 Auto Scaling**

| IAM feature | Amazon EC2 Auto Scaling support |
| --- | --- |
| [Identity-based policies](#security_iam_service-with-iam-id-based-policies) |  Yes |
| [Resource-based policies](#policy-auto-scaling-resources) |  No  |
| [Policy actions](#security_iam_service-with-iam-id-based-policies-actions) |  Yes |
| [Policy resources](#security_iam_service-with-iam-id-based-policies-resources) |  Yes |
| [Policy condition keys (service-specific)](#policy-auto-scaling-condition-keys) |  Yes |
| [ACLs](#security_iam_service-with-iam-acls) |  No  |
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags) |  Partial |
| [Temporary credentials](#security_iam_service-with-iam-roles-tempcreds) |  Yes |
| [Service roles](#security_iam_service-with-iam-roles-service) |  Yes |
| [Service-linked roles](#security_iam_service-with-iam-roles-service-linked) |  Yes |

To get a high-level view of how Amazon EC2 Auto Scaling and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Identity-based policies for Amazon EC2 Auto Scaling
<a name="security_iam_service-with-iam-id-based-policies"></a>

**Supports identity-based policies:** Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

## Resource-based policies within Amazon EC2 Auto Scaling
<a name="policy-auto-scaling-resources"></a>

**Supports resource-based policies:** No

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions a specified principal can perform on that resource and under what conditions. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy. Principals can include accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM entities in another account as the principal in a resource-based policy. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Policy actions for Amazon EC2 Auto Scaling
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

**Supports policy actions:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

To see a list of Amazon EC2 Auto Scaling actions, see [Actions defined by Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html#amazonec2autoscaling-actions-as-permissions) in the *Service Authorization Reference*.

Policy actions in Amazon EC2 Auto Scaling use the following prefix before the action:

```
autoscaling
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
  "autoscaling:{{action1}}",
  "autoscaling:{{action2}}"
]
```

You can specify multiple actions by using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "autoscaling:{{Describe*}}"
```

## Policy resources for Amazon EC2 Auto Scaling
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

You can use ARNs to identify the Auto Scaling groups and launch configurations that the IAM policy applies to.

An Auto Scaling group has the following ARN.

```
"Resource": "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:{{uuid}}:autoScalingGroupName/{{asg-name}}"
```

A launch configuration has the following ARN.

```
"Resource": "arn:aws:autoscaling:{{region}}:{{account-id}}:launchConfiguration:{{uuid}}:launchConfigurationName/{{lc-name}}"
```

To specify an Auto Scaling group with the `CreateAutoScalingGroup` action, you must replace the UUID with a wildcard (`*`) as shown in the following example.

```
"Resource": "arn:aws:autoscaling:{{region}}:{{account-id}}:autoScalingGroup:*:autoScalingGroupName/{{asg-name}}"
```

To specify a launch configuration with the `CreateLaunchConfiguration` action, you must replace the UUID with a wildcard (`*`) as shown in the following example.

```
"Resource": "arn:aws:autoscaling:{{region}}:{{account-id}}:launchConfiguration:*:launchConfigurationName/{{lc-name}}"
```

For more information about Amazon EC2 Auto Scaling resource types and their ARNs, see [Resources defined by Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html#amazonec2autoscaling-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions defined by Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html#amazonec2autoscaling-actions-as-permissions).

**Note**
For an example of an IAM policy that uses ARNs to control access to Auto Scaling groups, see [Control which Auto Scaling groups can be deleted](security_iam_id-based-policy-examples.md#policy-example-delete-auto-scaling-group).

Not all Amazon EC2 Auto Scaling actions support resource-level permissions. For actions that don't support resource-level permissions, you must use a wildcard (`*`) as the resource.

The following Amazon EC2 Auto Scaling actions do not support resource-level permissions.
+ `DescribeAccountLimits`
+ `DescribeAdjustmentTypes`
+ `DescribeAutoScalingGroups`
+ `DescribeAutoScalingInstances`
+ `DescribeAutoScalingNotificationTypes`
+ `DescribeInstanceRefreshes`
+ `DescribeLaunchConfigurations`
+ `DescribeLifecycleHooks`
+ `DescribeLifecycleHookTypes`
+ `DescribeLoadBalancers`
+ `DescribeLoadBalancerTargetGroups`
+ `DescribeMetricCollectionTypes`
+ `DescribeNotificationConfigurations`
+ `DescribePolicies`
+ `DescribeScalingActivities`
+ `DescribeScalingProcessTypes`
+ `DescribeScheduledActions`
+ `DescribeTags`
+ `DescribeTerminationPolicyTypes`
+ `DescribeWarmPool`

## Policy condition keys for Amazon EC2 Auto Scaling
<a name="policy-auto-scaling-condition-keys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Amazon EC2 Auto Scaling supports the following condition keys that can be used to control access to supported actions and enforce the configuration of Auto Scaling groups:
+ `autoscaling:InstanceTypes`
+ `autoscaling:LaunchConfigurationName`
+ `autoscaling:LaunchTemplateVersionSpecified`
+ `autoscaling:LoadBalancerNames`
+ `autoscaling:MaxSize`
+ `autoscaling:MinSize`
+ `autoscaling:ResourceTag/{{key-name}}: {{tag-value}}`
+ `autoscaling:TargetGroupARNs`
+ `autoscaling:VPCZoneIdentifiers`
+ `autoscaling:ForceDelete`

The following condition keys are specific to create launch configuration requests:
+ `autoscaling:ImageId`
+ `autoscaling:InstanceType`
+ `autoscaling:MetadataHttpEndpoint`
+ `autoscaling:MetadataHttpPutResponseHopLimit`
+ `autoscaling:MetadataHttpTokens`
+ `autoscaling:SpotPrice`

Amazon EC2 Auto Scaling also supports the following global condition keys that you can use to define permissions based on the tags in the request or present on the Auto Scaling group. For more information, see [Tag Auto Scaling groups and instances](ec2-auto-scaling-tagging.md).
+ `aws:RequestTag/{{key-name}}: {{tag-value}}`
+ `aws:ResourceTag/{{key-name}}: {{tag-value}}`
+ `aws:TagKeys: {{[{{tag-key}}, ...]}}`

To learn which Amazon EC2 Auto Scaling API actions you can use a condition key with, see [Actions defined by Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html#amazonec2autoscaling-actions-as-permissions) in the *Service Authorization Reference*. For more information about Amazon EC2 Auto Scaling condition keys, see [Condition keys for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2autoscaling.html#amazonec2autoscaling-policy-keys).

**Note**
For examples of IAM policies that use condition keys to control access to supported actions and enforce the configuration of Auto Scaling groups, see the following resources:
[Require a launch template and a version number](ec2-auto-scaling-launch-template-permissions.md#policy-example-launch-template-ex2) – This example enforces that a launch template and the version number of the launch template must be specified when creating or updating Auto Scaling groups.
[Control the size of the Auto Scaling groups that can be created](security_iam_id-based-policy-examples.md#policy-example-min-max-size) – This example enforces constraints on the possible values for the `MinSize` and `MaxSize` properties when creating or updating Auto Scaling groups with a specific tag.
[Control which scaling policies can be deleted](security_iam_id-based-policy-examples.md#policy-example-delete-policy) – This example enforces that deleting scaling policies is allowed only for Auto Scaling groups without a specific tag.

## ACLs in Amazon EC2 Auto Scaling
<a name="security_iam_service-with-iam-acls"></a>

**Supports ACLs:** No

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

## ABAC with Amazon EC2 Auto Scaling
<a name="security_iam_service-with-iam-tags"></a>

**Supports ABAC (tags in policies):** Partial

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `aws:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the *IAM User Guide*. To view a tutorial with steps for setting up ABAC, see [Use attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the *IAM User Guide*.

ABAC is possible for resources that support tags, but not everything supports tags. Launch configurations and scaling policies don't support tags, but Auto Scaling groups support tags.

For more information, see [Tag Auto Scaling groups and instances](ec2-auto-scaling-tagging.md).

## Using temporary credentials with Amazon EC2 Auto Scaling
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

**Supports temporary credentials:** Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you dynamically generate temporary credentials instead of using long-term access keys. For more information, see [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) and [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## Service roles for Amazon EC2 Auto Scaling
<a name="security_iam_service-with-iam-roles-service"></a>

**Supports service roles:** Yes

 A service role is an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see [Create a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

When you create a lifecycle hook that notifies an Amazon SNS topic or Amazon SQS queue, you must specify a role to allow Amazon EC2 Auto Scaling to access Amazon SNS or Amazon SQS on your behalf. Use the IAM console to set up the service role for your lifecycle hook. The console helps you create a role with a sufficient set of permissions using a managed policy. For more information, see [Receive notifications using Amazon SNS](prepare-for-lifecycle-notifications.md#sns-notifications) and [Receive notifications using Amazon SQS](prepare-for-lifecycle-notifications.md#sqs-notifications).

When you create an Auto Scaling group, you can optionally pass in a service role to allow Amazon EC2 instances to access other AWS services on your behalf. The service role for Amazon EC2 instances (also called the Amazon EC2 instance profile for a launch template or launch configuration) is a special type of service role that is assigned to every EC2 instance in an Auto Scaling group when the instance launches. You can use the IAM console and AWS CLI to create or edit this service role. For more information, see [IAM role for applications that run on Amazon EC2 instances](us-iam-role.md).

**Warning**
Changing the permissions for a service role might break Amazon EC2 Auto Scaling functionality. Edit service roles only when Amazon EC2 Auto Scaling provides guidance to do so.

## Service-linked roles for Amazon EC2 Auto Scaling
<a name="security_iam_service-with-iam-roles-service-linked"></a>

**Supports service-linked roles:** Yes

 A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf. Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view, but not edit the permissions for service-linked roles.

For details about creating or managing Amazon EC2 Auto Scaling service-linked roles, see [Service-linked roles for Amazon EC2 Auto Scaling](autoscaling-service-linked-role.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
