---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sheetcontrolinfoiconlabeloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SheetControlInfoIconLabelOptions
<a name="aws-properties-quicksight-analysis-sheetcontrolinfoiconlabeloptions"></a>

A control to display info icons for filters and parameters.

## Syntax
<a name="aws-properties-quicksight-analysis-sheetcontrolinfoiconlabeloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sheetcontrolinfoiconlabeloptions-syntax.json"></a>

```
{
  "[InfoIconText](#cfn-quicksight-analysis-sheetcontrolinfoiconlabeloptions-infoicontext)" : {{String}},
  "[Visibility](#cfn-quicksight-analysis-sheetcontrolinfoiconlabeloptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sheetcontrolinfoiconlabeloptions-syntax.yaml"></a>

```
  [InfoIconText](#cfn-quicksight-analysis-sheetcontrolinfoiconlabeloptions-infoicontext): {{String}}
  [Visibility](#cfn-quicksight-analysis-sheetcontrolinfoiconlabeloptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sheetcontrolinfoiconlabeloptions-properties"></a>

`InfoIconText`  <a name="cfn-quicksight-analysis-sheetcontrolinfoiconlabeloptions-infoicontext"></a>
 The text content of info icon.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-analysis-sheetcontrolinfoiconlabeloptions-visibility"></a>
The visibility configuration of info icon label options.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
