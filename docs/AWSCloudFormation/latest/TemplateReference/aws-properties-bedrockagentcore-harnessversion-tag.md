---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harnessversion-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::HarnessVersion Tag
<a name="aws-properties-bedrockagentcore-harnessversion-tag"></a>

<a name="aws-properties-bedrockagentcore-harnessversion-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::BedrockAgentCore::HarnessVersion](aws-resource-bedrockagentcore-harnessversion.md).

## Syntax
<a name="aws-properties-bedrockagentcore-harnessversion-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harnessversion-tag-syntax.json"></a>

```
{
  "[Key](#cfn-bedrockagentcore-harnessversion-tag-key)" : {{String}},
  "[Value](#cfn-bedrockagentcore-harnessversion-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harnessversion-tag-syntax.yaml"></a>

```
  [Key](#cfn-bedrockagentcore-harnessversion-tag-key): {{String}}
  [Value](#cfn-bedrockagentcore-harnessversion-tag-value): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harnessversion-tag-properties"></a>

`Key`  <a name="cfn-bedrockagentcore-harnessversion-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.:/=+\-@]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrockagentcore-harnessversion-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s_.:/=+\-@]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
