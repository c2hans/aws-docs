---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CodeInterpreterCustom VpcConfig
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig"></a>

VpcConfig for the Agent.

## Syntax
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-securitygroups): {{
    - String}}
  [Subnets](#cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig-properties"></a>

`SecurityGroups`  <a name="cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-securitygroups"></a>
The security groups associated with the VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-subnets"></a>
The subnets associated with the VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
