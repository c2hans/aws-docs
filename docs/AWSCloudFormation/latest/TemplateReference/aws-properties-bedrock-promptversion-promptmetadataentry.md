---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-promptmetadataentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion PromptMetadataEntry
<a name="aws-properties-bedrock-promptversion-promptmetadataentry"></a>

Contains a key-value pair that defines a metadata tag and value to attach to a prompt variant. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html).

## Syntax
<a name="aws-properties-bedrock-promptversion-promptmetadataentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-promptmetadataentry-syntax.json"></a>

```
{
  "[Key](#cfn-bedrock-promptversion-promptmetadataentry-key)" : {{String}},
  "[Value](#cfn-bedrock-promptversion-promptmetadataentry-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-promptmetadataentry-syntax.yaml"></a>

```
  [Key](#cfn-bedrock-promptversion-promptmetadataentry-key): {{String}}
  [Value](#cfn-bedrock-promptversion-promptmetadataentry-value): {{String}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-promptmetadataentry-properties"></a>

`Key`  <a name="cfn-bedrock-promptversion-promptmetadataentry-key"></a>
The key of a metadata tag for a prompt variant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrock-promptversion-promptmetadataentry-value"></a>
The value of a metadata tag for a prompt variant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
