---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-memory-indexedkey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Memory IndexedKey
<a name="aws-properties-bedrockagentcore-memory-indexedkey"></a>

A metadata key indexed for filtering.

## Syntax
<a name="aws-properties-bedrockagentcore-memory-indexedkey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-memory-indexedkey-syntax.json"></a>

```
{
  "[Key](#cfn-bedrockagentcore-memory-indexedkey-key)" : {{String}},
  "[Type](#cfn-bedrockagentcore-memory-indexedkey-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-memory-indexedkey-syntax.yaml"></a>

```
  [Key](#cfn-bedrockagentcore-memory-indexedkey-key): {{String}}
  [Type](#cfn-bedrockagentcore-memory-indexedkey-type): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-memory-indexedkey-properties"></a>

`Key`  <a name="cfn-bedrockagentcore-memory-indexedkey-key"></a>
The metadata key name to index.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrockagentcore-memory-indexedkey-type"></a>
The data type of the indexed key.
*Required*: Yes
*Type*: String
*Allowed values*: `STRING | STRINGLIST | NUMBER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
