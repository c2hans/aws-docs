---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-defaultrelativedatetimecontroloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DefaultRelativeDateTimeControlOptions
<a name="aws-properties-quicksight-analysis-defaultrelativedatetimecontroloptions"></a>

The default options that correspond to the `RelativeDateTime` filter control type.

## Syntax
<a name="aws-properties-quicksight-analysis-defaultrelativedatetimecontroloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-defaultrelativedatetimecontroloptions-syntax.json"></a>

```
{
  "[CommitMode](#cfn-quicksight-analysis-defaultrelativedatetimecontroloptions-commitmode)" : {{String}},
  "[DisplayOptions](#cfn-quicksight-analysis-defaultrelativedatetimecontroloptions-displayoptions)" : {{RelativeDateTimeControlDisplayOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-defaultrelativedatetimecontroloptions-syntax.yaml"></a>

```
  [CommitMode](#cfn-quicksight-analysis-defaultrelativedatetimecontroloptions-commitmode): {{String}}
  [DisplayOptions](#cfn-quicksight-analysis-defaultrelativedatetimecontroloptions-displayoptions): {{
    RelativeDateTimeControlDisplayOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-defaultrelativedatetimecontroloptions-properties"></a>

`CommitMode`  <a name="cfn-quicksight-analysis-defaultrelativedatetimecontroloptions-commitmode"></a>
The visibility configuration of the Apply button on a `RelativeDateTimeControl`.
*Required*: No
*Type*: String
*Allowed values*: `AUTO | MANUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayOptions`  <a name="cfn-quicksight-analysis-defaultrelativedatetimecontroloptions-displayoptions"></a>
The display options of a control.
*Required*: No
*Type*: [RelativeDateTimeControlDisplayOptions](aws-properties-quicksight-analysis-relativedatetimecontroldisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
