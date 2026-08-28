---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-binwidthoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis BinWidthOptions
<a name="aws-properties-quicksight-analysis-binwidthoptions"></a>

The options that determine the bin width of a histogram.

## Syntax
<a name="aws-properties-quicksight-analysis-binwidthoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-binwidthoptions-syntax.json"></a>

```
{
  "[BinCountLimit](#cfn-quicksight-analysis-binwidthoptions-bincountlimit)" : {{Number}},
  "[Value](#cfn-quicksight-analysis-binwidthoptions-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-binwidthoptions-syntax.yaml"></a>

```
  [BinCountLimit](#cfn-quicksight-analysis-binwidthoptions-bincountlimit): {{Number}}
  [Value](#cfn-quicksight-analysis-binwidthoptions-value): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-binwidthoptions-properties"></a>

`BinCountLimit`  <a name="cfn-quicksight-analysis-binwidthoptions-bincountlimit"></a>
The options that determine the bin count limit.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-analysis-binwidthoptions-value"></a>
The options that determine the bin width value.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
