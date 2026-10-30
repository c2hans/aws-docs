---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-matchmodels.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule MatchModels
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodels"></a>

A condition that matches inference requests based on the requested model.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodels-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodels-syntax.json"></a>

```
{
  "[AnyOf](#cfn-bedrockagentcore-gatewayrule-matchmodels-anyof)" : {{[ MatchModelEntry, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodels-syntax.yaml"></a>

```
  [AnyOf](#cfn-bedrockagentcore-gatewayrule-matchmodels-anyof): {{
    - MatchModelEntry}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodels-properties"></a>

`AnyOf`  <a name="cfn-bedrockagentcore-gatewayrule-matchmodels-anyof"></a>
A list of model entries. The condition is met if the requested model matches any of the entries.
*Required*: Yes
*Type*: Array of [MatchModelEntry](aws-properties-bedrockagentcore-gatewayrule-matchmodelentry.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
