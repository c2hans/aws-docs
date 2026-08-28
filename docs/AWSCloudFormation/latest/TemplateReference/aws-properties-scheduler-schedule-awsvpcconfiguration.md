---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-awsvpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule AwsVpcConfiguration
<a name="aws-properties-scheduler-schedule-awsvpcconfiguration"></a>

This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.

## Syntax
<a name="aws-properties-scheduler-schedule-awsvpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-awsvpcconfiguration-syntax.json"></a>

```
{
  "[AssignPublicIp](#cfn-scheduler-schedule-awsvpcconfiguration-assignpublicip)" : {{String}},
  "[SecurityGroups](#cfn-scheduler-schedule-awsvpcconfiguration-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-scheduler-schedule-awsvpcconfiguration-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-awsvpcconfiguration-syntax.yaml"></a>

```
  [AssignPublicIp](#cfn-scheduler-schedule-awsvpcconfiguration-assignpublicip): {{String}}
  [SecurityGroups](#cfn-scheduler-schedule-awsvpcconfiguration-securitygroups): {{
    - String}}
  [Subnets](#cfn-scheduler-schedule-awsvpcconfiguration-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-scheduler-schedule-awsvpcconfiguration-properties"></a>

`AssignPublicIp`  <a name="cfn-scheduler-schedule-awsvpcconfiguration-assignpublicip"></a>
Specifies whether the task's elastic network interface receives a public IP address. You can specify `ENABLED` only when `LaunchType` in `EcsParameters` is set to `FARGATE`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroups`  <a name="cfn-scheduler-schedule-awsvpcconfiguration-securitygroups"></a>
Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `1000 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-scheduler-schedule-awsvpcconfiguration-subnets"></a>
Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `1000 | 16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
