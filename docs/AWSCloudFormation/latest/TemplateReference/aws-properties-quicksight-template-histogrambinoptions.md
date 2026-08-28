---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-histogrambinoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template HistogramBinOptions
<a name="aws-properties-quicksight-template-histogrambinoptions"></a>

The options that determine the presentation of histogram bins.

## Syntax
<a name="aws-properties-quicksight-template-histogrambinoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-histogrambinoptions-syntax.json"></a>

```
{
  "[BinCount](#cfn-quicksight-template-histogrambinoptions-bincount)" : {{BinCountOptions}},
  "[BinWidth](#cfn-quicksight-template-histogrambinoptions-binwidth)" : {{BinWidthOptions}},
  "[SelectedBinType](#cfn-quicksight-template-histogrambinoptions-selectedbintype)" : {{String}},
  "[StartValue](#cfn-quicksight-template-histogrambinoptions-startvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-histogrambinoptions-syntax.yaml"></a>

```
  [BinCount](#cfn-quicksight-template-histogrambinoptions-bincount): {{
    BinCountOptions}}
  [BinWidth](#cfn-quicksight-template-histogrambinoptions-binwidth): {{
    BinWidthOptions}}
  [SelectedBinType](#cfn-quicksight-template-histogrambinoptions-selectedbintype): {{String}}
  [StartValue](#cfn-quicksight-template-histogrambinoptions-startvalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-template-histogrambinoptions-properties"></a>

`BinCount`  <a name="cfn-quicksight-template-histogrambinoptions-bincount"></a>
The options that determine the bin count of a histogram.
*Required*: No
*Type*: [BinCountOptions](aws-properties-quicksight-template-bincountoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BinWidth`  <a name="cfn-quicksight-template-histogrambinoptions-binwidth"></a>
The options that determine the bin width of a histogram.
*Required*: No
*Type*: [BinWidthOptions](aws-properties-quicksight-template-binwidthoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedBinType`  <a name="cfn-quicksight-template-histogrambinoptions-selectedbintype"></a>
The options that determine the selected bin type.
*Required*: No
*Type*: String
*Allowed values*: `BIN_COUNT | BIN_WIDTH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartValue`  <a name="cfn-quicksight-template-histogrambinoptions-startvalue"></a>
The options that determine the bin start value.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
