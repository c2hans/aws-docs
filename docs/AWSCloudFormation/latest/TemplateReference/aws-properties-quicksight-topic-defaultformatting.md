---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-defaultformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic DefaultFormatting
<a name="aws-properties-quicksight-topic-defaultformatting"></a>

A structure that represents a default formatting definition.

## Syntax
<a name="aws-properties-quicksight-topic-defaultformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-defaultformatting-syntax.json"></a>

```
{
  "[DisplayFormat](#cfn-quicksight-topic-defaultformatting-displayformat)" : {{String}},
  "[DisplayFormatOptions](#cfn-quicksight-topic-defaultformatting-displayformatoptions)" : {{DisplayFormatOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-defaultformatting-syntax.yaml"></a>

```
  [DisplayFormat](#cfn-quicksight-topic-defaultformatting-displayformat): {{String}}
  [DisplayFormatOptions](#cfn-quicksight-topic-defaultformatting-displayformatoptions): {{
    DisplayFormatOptions}}
```

## Properties
<a name="aws-properties-quicksight-topic-defaultformatting-properties"></a>

`DisplayFormat`  <a name="cfn-quicksight-topic-defaultformatting-displayformat"></a>
The display format. Valid values for this structure are `AUTO`, `PERCENT`, `CURRENCY`, `NUMBER`, `DATE`, and `STRING`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | PERCENT | CURRENCY | NUMBER | DATE | STRING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayFormatOptions`  <a name="cfn-quicksight-topic-defaultformatting-displayformatoptions"></a>
The additional options for display formatting.
*Required*: No
*Type*: [DisplayFormatOptions](aws-properties-quicksight-topic-displayformatoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
