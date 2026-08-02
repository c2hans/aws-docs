---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-detective-graph-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Detective::Graph Tag
<a name="aws-properties-detective-graph-tag"></a>

The metadata that you apply to a resource to help you categorize and organize it. Each tag consists of a key and an optional value, both of which you define. For more information about tags, see [What is Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) in the *Tagging AWS Resources and Tag Editor User Guide*.

## Syntax
<a name="aws-properties-detective-graph-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-detective-graph-tag-syntax.json"></a>

```
{
  "[Key](#cfn-detective-graph-tag-key)" : {{String}},
  "[Value](#cfn-detective-graph-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-detective-graph-tag-syntax.yaml"></a>

```
  [Key](#cfn-detective-graph-tag-key): {{String}}
  [Value](#cfn-detective-graph-tag-value): {{String}}
```

## Properties
<a name="aws-properties-detective-graph-tag-properties"></a>

`Key`  <a name="cfn-detective-graph-tag-key"></a>
One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-detective-graph-tag-value"></a>
The optional part of a key-value pair that makes up a tag. A value acts as a descriptor in a tag category (key).
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
