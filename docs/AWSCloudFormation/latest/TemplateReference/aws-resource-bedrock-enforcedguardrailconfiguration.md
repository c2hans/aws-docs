---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-enforcedguardrailconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::EnforcedGuardrailConfiguration
<a name="aws-resource-bedrock-enforcedguardrailconfiguration"></a>

Sets the account-level enforced guardrail configuration.

## Syntax
<a name="aws-resource-bedrock-enforcedguardrailconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-enforcedguardrailconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::EnforcedGuardrailConfiguration",
  "Properties" : {
      "[GuardrailIdentifier](#cfn-bedrock-enforcedguardrailconfiguration-guardrailidentifier)" : {{String}},
      "[GuardrailVersion](#cfn-bedrock-enforcedguardrailconfiguration-guardrailversion)" : {{String}},
      "[ModelEnforcement](#cfn-bedrock-enforcedguardrailconfiguration-modelenforcement)" : {{ModelEnforcement}},
      "[SelectiveContentGuarding](#cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding)" : {{SelectiveContentGuarding}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-enforcedguardrailconfiguration-syntax.yaml"></a>

```
Type: AWS::Bedrock::EnforcedGuardrailConfiguration
Properties:
  [GuardrailIdentifier](#cfn-bedrock-enforcedguardrailconfiguration-guardrailidentifier): {{String}}
  [GuardrailVersion](#cfn-bedrock-enforcedguardrailconfiguration-guardrailversion): {{String}}
  [ModelEnforcement](#cfn-bedrock-enforcedguardrailconfiguration-modelenforcement): {{
    ModelEnforcement}}
  [SelectiveContentGuarding](#cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding): {{
    SelectiveContentGuarding}}
```

## Properties
<a name="aws-resource-bedrock-enforcedguardrailconfiguration-properties"></a>

`GuardrailIdentifier`  <a name="cfn-bedrock-enforcedguardrailconfiguration-guardrailidentifier"></a>
Identifier for the guardrail, could be the ID or the ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))$`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GuardrailVersion`  <a name="cfn-bedrock-enforcedguardrailconfiguration-guardrailversion"></a>
Numerical guardrail version.
*Required*: Yes
*Type*: String
*Pattern*: `^[1-9][0-9]{0,7}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelEnforcement`  <a name="cfn-bedrock-enforcedguardrailconfiguration-modelenforcement"></a>
Model-specific information for the enforced guardrail configuration.
*Required*: No
*Type*: [ModelEnforcement](aws-properties-bedrock-enforcedguardrailconfiguration-modelenforcement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectiveContentGuarding`  <a name="cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding"></a>
Selective content guarding controls for enforced guardrails.
*Required*: No
*Type*: [SelectiveContentGuarding](aws-properties-bedrock-enforcedguardrailconfiguration-selectivecontentguarding.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrock-enforcedguardrailconfiguration-return-values"></a>

### Ref
<a name="aws-resource-bedrock-enforcedguardrailconfiguration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-enforcedguardrailconfiguration-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-enforcedguardrailconfiguration-return-values-fn--getatt-fn--getatt"></a>

`ConfigId`  <a name="ConfigId-fn::getatt"></a>
Unique ID for the account enforced configuration.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Timestamp.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The ARN of the role used to update the configuration.

`GuardrailArn`  <a name="GuardrailArn-fn::getatt"></a>
ARN representation for the guardrail.

`GuardrailId`  <a name="GuardrailId-fn::getatt"></a>
Unique ID for the guardrail.

`Owner`  <a name="Owner-fn::getatt"></a>
Configuration owner type.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Timestamp.

`UpdatedBy`  <a name="UpdatedBy-fn::getatt"></a>
The ARN of the role used to update the configuration.
