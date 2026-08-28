---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe NetworkConfiguration
<a name="aws-properties-pipes-pipe-networkconfiguration"></a>

This structure specifies the network configuration for an Amazon ECS task.

## Syntax
<a name="aws-properties-pipes-pipe-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-networkconfiguration-syntax.json"></a>

```
{
  "[AwsvpcConfiguration](#cfn-pipes-pipe-networkconfiguration-awsvpcconfiguration)" : {{AwsVpcConfiguration}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-networkconfiguration-syntax.yaml"></a>

```
  [AwsvpcConfiguration](#cfn-pipes-pipe-networkconfiguration-awsvpcconfiguration): {{
    AwsVpcConfiguration}}
```

## Properties
<a name="aws-properties-pipes-pipe-networkconfiguration-properties"></a>

`AwsvpcConfiguration`  <a name="cfn-pipes-pipe-networkconfiguration-awsvpcconfiguration"></a>
Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the `awsvpc` network mode.
*Required*: No
*Type*: [AwsVpcConfiguration](aws-properties-pipes-pipe-awsvpcconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
