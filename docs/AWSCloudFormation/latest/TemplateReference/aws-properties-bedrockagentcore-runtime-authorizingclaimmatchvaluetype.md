---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Runtime AuthorizingClaimMatchValueType
<a name="aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype"></a>

Defines the value or values to match for and the relationship of the match.

## Syntax
<a name="aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-syntax.json"></a>

```
{
  "[ClaimMatchOperator](#cfn-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-claimmatchoperator)" : {{String}},
  "[ClaimMatchValue](#cfn-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-claimmatchvalue)" : {{ClaimMatchValueType}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-syntax.yaml"></a>

```
  [ClaimMatchOperator](#cfn-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-claimmatchoperator): {{String}}
  [ClaimMatchValue](#cfn-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-claimmatchvalue): {{
    ClaimMatchValueType}}
```

## Properties
<a name="aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-properties"></a>

`ClaimMatchOperator`  <a name="cfn-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-claimmatchoperator"></a>
Defines the relationship between the claim field value and the value or values you're matching for.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | CONTAINS | CONTAINS_ANY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClaimMatchValue`  <a name="cfn-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-claimmatchvalue"></a>
The value or values to match for.
*Required*: Yes
*Type*: [ClaimMatchValueType](aws-properties-bedrockagentcore-runtime-claimmatchvaluetype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
