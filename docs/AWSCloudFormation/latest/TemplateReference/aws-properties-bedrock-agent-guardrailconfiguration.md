---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-guardrailconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent GuardrailConfiguration
<a name="aws-properties-bedrock-agent-guardrailconfiguration"></a>

Configuration information for a guardrail that you use with the [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) operation.

## Syntax
<a name="aws-properties-bedrock-agent-guardrailconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-guardrailconfiguration-syntax.json"></a>

```
{
  "[GuardrailIdentifier](#cfn-bedrock-agent-guardrailconfiguration-guardrailidentifier)" : {{String}},
  "[GuardrailVersion](#cfn-bedrock-agent-guardrailconfiguration-guardrailversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-guardrailconfiguration-syntax.yaml"></a>

```
  [GuardrailIdentifier](#cfn-bedrock-agent-guardrailconfiguration-guardrailidentifier): {{String}}
  [GuardrailVersion](#cfn-bedrock-agent-guardrailconfiguration-guardrailversion): {{String}}
```

## Properties
<a name="aws-properties-bedrock-agent-guardrailconfiguration-properties"></a>

`GuardrailIdentifier`  <a name="cfn-bedrock-agent-guardrailconfiguration-guardrailidentifier"></a>
The identifier for the guardrail.
*Required*: No
*Type*: String
*Pattern*: `^(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GuardrailVersion`  <a name="cfn-bedrock-agent-guardrailconfiguration-guardrailversion"></a>
The version of the guardrail.
*Required*: No
*Type*: String
*Pattern*: `^(([0-9]{1,8})|(DRAFT))$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
