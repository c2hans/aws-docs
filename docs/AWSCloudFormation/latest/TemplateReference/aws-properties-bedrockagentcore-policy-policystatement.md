---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-policy-policystatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Policy PolicyStatement
<a name="aws-properties-bedrockagentcore-policy-policystatement"></a>

A policy statement within the AgentCore Policy system.

## Syntax
<a name="aws-properties-bedrockagentcore-policy-policystatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-policy-policystatement-syntax.json"></a>

```
{
  "[Statement](#cfn-bedrockagentcore-policy-policystatement-statement)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-policy-policystatement-syntax.yaml"></a>

```
  [Statement](#cfn-bedrockagentcore-policy-policystatement-statement): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-policy-policystatement-properties"></a>

`Statement`  <a name="cfn-bedrockagentcore-policy-policystatement-statement"></a>
The policy statement that defines the authorization logic.
*Required*: Yes
*Type*: String
*Minimum*: `35`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
