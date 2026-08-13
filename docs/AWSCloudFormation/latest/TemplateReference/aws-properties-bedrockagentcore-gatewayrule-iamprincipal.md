---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-iamprincipal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule IamPrincipal
<a name="aws-properties-bedrockagentcore-gatewayrule-iamprincipal"></a>

An IAM principal specification for rule matching.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-iamprincipal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-iamprincipal-syntax.json"></a>

```
{
  "[Arn](#cfn-bedrockagentcore-gatewayrule-iamprincipal-arn)" : {{String}},
  "[Operator](#cfn-bedrockagentcore-gatewayrule-iamprincipal-operator)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-iamprincipal-syntax.yaml"></a>

```
  [Arn](#cfn-bedrockagentcore-gatewayrule-iamprincipal-arn): {{String}}
  [Operator](#cfn-bedrockagentcore-gatewayrule-iamprincipal-operator): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-iamprincipal-properties"></a>

`Arn`  <a name="cfn-bedrockagentcore-gatewayrule-iamprincipal-arn"></a>
The Amazon Resource Name (ARN) of the IAM principal. Supports user, role, and assumed-role ARNs. Wildcards can be used with the `StringLike` operator.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws[a-zA-Z-]*:iam::(\d{12}|\*):(user|role)/[\w+=,.@*?/-]+|arn:aws[a-zA-Z-]*:sts::(\d{12}|\*):assumed-role/[\w+=,.@*?/-]+)$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-bedrockagentcore-gatewayrule-iamprincipal-operator"></a>
The match operator. `StringEquals` requires an exact match. `StringLike` supports wildcard patterns using `*` and `?`.
*Required*: No
*Type*: String
*Allowed values*: `StringEquals | StringLike`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
