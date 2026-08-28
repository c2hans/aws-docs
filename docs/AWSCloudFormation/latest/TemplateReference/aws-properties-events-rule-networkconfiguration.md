---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-networkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule NetworkConfiguration
<a name="aws-properties-events-rule-networkconfiguration"></a>

This structure specifies the network configuration for an ECS task.

## Syntax
<a name="aws-properties-events-rule-networkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-networkconfiguration-syntax.json"></a>

```
{
  "[AwsVpcConfiguration](#cfn-events-rule-networkconfiguration-awsvpcconfiguration)" : {{AwsVpcConfiguration}}
}
```

### YAML
<a name="aws-properties-events-rule-networkconfiguration-syntax.yaml"></a>

```
  [AwsVpcConfiguration](#cfn-events-rule-networkconfiguration-awsvpcconfiguration): {{
    AwsVpcConfiguration}}
```

## Properties
<a name="aws-properties-events-rule-networkconfiguration-properties"></a>

`AwsVpcConfiguration`  <a name="cfn-events-rule-networkconfiguration-awsvpcconfiguration"></a>
Use this structure to specify the VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the `awsvpc` network mode.
*Required*: No
*Type*: [AwsVpcConfiguration](aws-properties-events-rule-awsvpcconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-events-rule-networkconfiguration--seealso"></a>
+  [NetworkConfiguration](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_NetworkConfiguration.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
