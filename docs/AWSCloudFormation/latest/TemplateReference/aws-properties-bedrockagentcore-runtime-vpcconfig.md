---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime VpcConfig
<a name="aws-properties-bedrockagentcore-runtime-vpcconfig"></a>

VpcConfig for the Agent.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-bedrockagentcore-runtime-vpcconfig-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-bedrockagentcore-runtime-vpcconfig-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-bedrockagentcore-runtime-vpcconfig-securitygroups): {{
    - String}}
  [Subnets](#cfn-bedrockagentcore-runtime-vpcconfig-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-vpcconfig-properties"></a>

`SecurityGroups`  <a name="cfn-bedrockagentcore-runtime-vpcconfig-securitygroups"></a>
The security groups associated with the VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-bedrockagentcore-runtime-vpcconfig-subnets"></a>
The subnets associated with the VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
