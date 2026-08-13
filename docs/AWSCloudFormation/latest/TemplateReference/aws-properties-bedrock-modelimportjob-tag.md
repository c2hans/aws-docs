---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-modelimportjob-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::ModelImportJob Tag
<a name="aws-properties-bedrock-modelimportjob-tag"></a>

A tag associated with a resource. A tag consists of a key and value.

## Syntax
<a name="aws-properties-bedrock-modelimportjob-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-modelimportjob-tag-syntax.json"></a>

```
{
  "[Key](#cfn-bedrock-modelimportjob-tag-key)" : {{String}},
  "[Value](#cfn-bedrock-modelimportjob-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-modelimportjob-tag-syntax.yaml"></a>

```
  [Key](#cfn-bedrock-modelimportjob-tag-key): {{String}}
  [Value](#cfn-bedrock-modelimportjob-tag-value): {{String}}
```

## Properties
<a name="aws-properties-bedrock-modelimportjob-tag-properties"></a>

`Key`  <a name="cfn-bedrock-modelimportjob-tag-key"></a>
The key associated with a tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-bedrock-modelimportjob-tag-value"></a>
The value associated with a tag.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
