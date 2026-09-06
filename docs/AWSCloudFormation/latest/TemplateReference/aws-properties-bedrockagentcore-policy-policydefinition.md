---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-policy-policydefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Policy PolicyDefinition
<a name="aws-properties-bedrockagentcore-policy-policydefinition"></a>

The definition structure for policies. Encapsulates different policy formats.

## Syntax
<a name="aws-properties-bedrockagentcore-policy-policydefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-policy-policydefinition-syntax.json"></a>

```
{
  "[Cedar](#cfn-bedrockagentcore-policy-policydefinition-cedar)" : {{CedarPolicy}},
  "[Policy](#cfn-bedrockagentcore-policy-policydefinition-policy)" : {{PolicyStatement}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-policy-policydefinition-syntax.yaml"></a>

```
  [Cedar](#cfn-bedrockagentcore-policy-policydefinition-cedar): {{
    CedarPolicy}}
  [Policy](#cfn-bedrockagentcore-policy-policydefinition-policy): {{
    PolicyStatement}}
```

## Properties
<a name="aws-properties-bedrockagentcore-policy-policydefinition-properties"></a>

`Cedar`  <a name="cfn-bedrockagentcore-policy-policydefinition-cedar"></a>
The Cedar policy definition.
*Required*: No
*Type*: [CedarPolicy](aws-properties-bedrockagentcore-policy-cedarpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Policy`  <a name="cfn-bedrockagentcore-policy-policydefinition-policy"></a>
The policy statement definition.
*Required*: No
*Type*: [PolicyStatement](aws-properties-bedrockagentcore-policy-policystatement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
