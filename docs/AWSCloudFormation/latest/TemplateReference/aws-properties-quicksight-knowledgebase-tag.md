---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-knowledgebase-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase Tag
<a name="aws-properties-quicksight-knowledgebase-tag"></a>

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

## Syntax
<a name="aws-properties-quicksight-knowledgebase-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-knowledgebase-tag-syntax.json"></a>

```
{
  "[Key](#cfn-quicksight-knowledgebase-tag-key)" : {{String}},
  "[Value](#cfn-quicksight-knowledgebase-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-knowledgebase-tag-syntax.yaml"></a>

```
  [Key](#cfn-quicksight-knowledgebase-tag-key): {{String}}
  [Value](#cfn-quicksight-knowledgebase-tag-value): {{String}}
```

## Properties
<a name="aws-properties-quicksight-knowledgebase-tag-properties"></a>

`Key`  <a name="cfn-quicksight-knowledgebase-tag-key"></a>
Tag key.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-knowledgebase-tag-value"></a>
Tag value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
