---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::PaymentManager AuthorizingClaimMatchValueType
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype"></a>

Defines the value or values to match for and the relationship of the match.

## Syntax
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-syntax.json"></a>

```
{
  "[ClaimMatchOperator](#cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-claimmatchoperator)" : {{String}},
  "[ClaimMatchValue](#cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-claimmatchvalue)" : {{ClaimMatchValueType}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-syntax.yaml"></a>

```
  [ClaimMatchOperator](#cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-claimmatchoperator): {{String}}
  [ClaimMatchValue](#cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-claimmatchvalue): {{
    ClaimMatchValueType}}
```

## Properties
<a name="aws-properties-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-properties"></a>

`ClaimMatchOperator`  <a name="cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-claimmatchoperator"></a>
Defines the relationship between the claim field value and the value or values you're matching for.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | CONTAINS | CONTAINS_ANY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClaimMatchValue`  <a name="cfn-bedrockagentcore-paymentmanager-authorizingclaimmatchvaluetype-claimmatchvalue"></a>
The value or values to match for.
*Required*: Yes
*Type*: [ClaimMatchValueType](aws-properties-bedrockagentcore-paymentmanager-claimmatchvaluetype.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
