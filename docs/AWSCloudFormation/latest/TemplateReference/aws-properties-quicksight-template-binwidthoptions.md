---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-binwidthoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BinWidthOptions
<a name="aws-properties-quicksight-template-binwidthoptions"></a>

The options that determine the bin width of a histogram.

## Syntax
<a name="aws-properties-quicksight-template-binwidthoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-binwidthoptions-syntax.json"></a>

```
{
  "[BinCountLimit](#cfn-quicksight-template-binwidthoptions-bincountlimit)" : {{Number}},
  "[Value](#cfn-quicksight-template-binwidthoptions-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-binwidthoptions-syntax.yaml"></a>

```
  [BinCountLimit](#cfn-quicksight-template-binwidthoptions-bincountlimit): {{Number}}
  [Value](#cfn-quicksight-template-binwidthoptions-value): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-template-binwidthoptions-properties"></a>

`BinCountLimit`  <a name="cfn-quicksight-template-binwidthoptions-bincountlimit"></a>
The options that determine the bin count limit.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-template-binwidthoptions-value"></a>
The options that determine the bin width value.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
