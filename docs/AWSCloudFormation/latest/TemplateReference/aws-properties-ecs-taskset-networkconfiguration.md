---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskset-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::TaskSet NetworkConfiguration
<a name="aws-properties-ecs-taskset-networkconfiguration"></a>

The network configuration for a task or service.

## Syntax
<a name="aws-properties-ecs-taskset-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-taskset-networkconfiguration-syntax.json"></a>

```
{
  "[AwsVpcConfiguration](#cfn-ecs-taskset-networkconfiguration-awsvpcconfiguration)" : {{AwsVpcConfiguration}}
}
```

### YAML
<a name="aws-properties-ecs-taskset-networkconfiguration-syntax.yaml"></a>

```
  [AwsVpcConfiguration](#cfn-ecs-taskset-networkconfiguration-awsvpcconfiguration): {{
    AwsVpcConfiguration}}
```

## Properties
<a name="aws-properties-ecs-taskset-networkconfiguration-properties"></a>

`AwsVpcConfiguration`  <a name="cfn-ecs-taskset-networkconfiguration-awsvpcconfiguration"></a>
The VPC subnets and security groups that are associated with a task.
All specified subnets and security groups must be from the same VPC.
*Required*: No
*Type*: [AwsVpcConfiguration](aws-properties-ecs-taskset-awsvpcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
