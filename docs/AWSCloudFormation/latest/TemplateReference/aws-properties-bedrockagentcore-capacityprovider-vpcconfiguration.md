---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-vpcconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider VpcConfiguration
<a name="aws-properties-bedrockagentcore-capacityprovider-vpcconfiguration"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-vpcconfiguration-description"></a>The `VpcConfiguration` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-vpcconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-vpcconfiguration-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-bedrockagentcore-capacityprovider-vpcconfiguration-securitygroups)" : {{[ String, ... ]}},
  "[Subnets](#cfn-bedrockagentcore-capacityprovider-vpcconfiguration-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-vpcconfiguration-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-bedrockagentcore-capacityprovider-vpcconfiguration-securitygroups): {{
    - String}}
  [Subnets](#cfn-bedrockagentcore-capacityprovider-vpcconfiguration-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-vpcconfiguration-properties"></a>

`SecurityGroups`  <a name="cfn-bedrockagentcore-capacityprovider-vpcconfiguration-securitygroups"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Subnets`  <a name="cfn-bedrockagentcore-capacityprovider-vpcconfiguration-subnets"></a>
Property description not available.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `16`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
