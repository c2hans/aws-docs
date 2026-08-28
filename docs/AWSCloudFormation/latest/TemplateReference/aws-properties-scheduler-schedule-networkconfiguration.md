---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule NetworkConfiguration
<a name="aws-properties-scheduler-schedule-networkconfiguration"></a>

Specifies the network configuration for an ECS task.

## Syntax
<a name="aws-properties-scheduler-schedule-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-networkconfiguration-syntax.json"></a>

```
{
  "[AwsvpcConfiguration](#cfn-scheduler-schedule-networkconfiguration-awsvpcconfiguration)" : {{AwsVpcConfiguration}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-networkconfiguration-syntax.yaml"></a>

```
  [AwsvpcConfiguration](#cfn-scheduler-schedule-networkconfiguration-awsvpcconfiguration): {{
    AwsVpcConfiguration}}
```

## Properties
<a name="aws-properties-scheduler-schedule-networkconfiguration-properties"></a>

`AwsvpcConfiguration`  <a name="cfn-scheduler-schedule-networkconfiguration-awsvpcconfiguration"></a>
Specifies the Amazon VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.
*Required*: No
*Type*: [AwsVpcConfiguration](aws-properties-scheduler-schedule-awsvpcconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
