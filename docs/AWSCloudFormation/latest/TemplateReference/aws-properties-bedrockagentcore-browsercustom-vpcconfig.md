---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-browsercustom-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom VpcConfig
<a name="aws-properties-bedrockagentcore-browsercustom-vpcconfig"></a>

VpcConfig for the Agent.

## Syntax
<a name="aws-properties-bedrockagentcore-browsercustom-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-browsercustom-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-bedrockagentcore-browsercustom-vpcconfig-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-bedrockagentcore-browsercustom-vpcconfig-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-browsercustom-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-bedrockagentcore-browsercustom-vpcconfig-securitygroups): {{
    - String}}
  [Subnets](#cfn-bedrockagentcore-browsercustom-vpcconfig-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-browsercustom-vpcconfig-properties"></a>

`SecurityGroups`  <a name="cfn-bedrockagentcore-browsercustom-vpcconfig-securitygroups"></a>
The security groups associated with the VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-bedrockagentcore-browsercustom-vpcconfig-subnets"></a>
The subnets associated with the VPC configuration.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
