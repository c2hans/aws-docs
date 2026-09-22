---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-namespacekeyentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory NamespaceKeyEntry
<a name="aws-properties-bedrockagentcore-memory-namespacekeyentry"></a>

A namespace variable key definition with optional `NamespaceKeyValidation` rules.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-namespacekeyentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-namespacekeyentry-syntax.json"></a>

```
{
  "[Key](#cfn-bedrockagentcore-memory-namespacekeyentry-key)" : {{String}},
  "[Validation](#cfn-bedrockagentcore-memory-namespacekeyentry-validation)" : {{NamespaceKeyValidation}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-namespacekeyentry-syntax.yaml"></a>

```
  [Key](#cfn-bedrockagentcore-memory-namespacekeyentry-key): {{String}}
  [Validation](#cfn-bedrockagentcore-memory-namespacekeyentry-validation): {{
    NamespaceKeyValidation}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-namespacekeyentry-properties"></a>

`Key`  <a name="cfn-bedrockagentcore-memory-namespacekeyentry-key"></a>
The namespace variable key name.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!memoryStrategyId$|actorId$|sessionId$)[a-z][a-z0-9]*$`
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Validation`  <a name="cfn-bedrockagentcore-memory-namespacekeyentry-validation"></a>
The validation rules that constrain values for this namespace variable at runtime (`CreateEvent` API).
*Required*: No
*Type*: [NamespaceKeyValidation](aws-properties-bedrockagentcore-memory-namespacekeyvalidation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
