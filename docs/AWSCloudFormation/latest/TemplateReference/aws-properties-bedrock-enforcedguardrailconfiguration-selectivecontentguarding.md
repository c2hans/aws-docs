---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-enforcedguardrailconfiguration-selectivecontentguarding.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::EnforcedGuardrailConfiguration SelectiveContentGuarding
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-selectivecontentguarding"></a>

Selective content guarding controls for enforced guardrails.

## Syntax
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-syntax.json"></a>

```
{
  "[Messages](#cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-messages)" : {{String}},
  "[System](#cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-system)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-syntax.yaml"></a>

```
  [Messages](#cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-messages): {{String}}
  [System](#cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-system): {{String}}
```

## Properties
<a name="aws-properties-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-properties"></a>

`Messages`  <a name="cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-messages"></a>
Selective guarding mode for user messages.
*Required*: No
*Type*: String
*Allowed values*: `SELECTIVE | COMPREHENSIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`System`  <a name="cfn-bedrock-enforcedguardrailconfiguration-selectivecontentguarding-system"></a>
Selective guarding mode for system prompts.
*Required*: No
*Type*: String
*Allowed values*: `SELECTIVE | COMPREHENSIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
