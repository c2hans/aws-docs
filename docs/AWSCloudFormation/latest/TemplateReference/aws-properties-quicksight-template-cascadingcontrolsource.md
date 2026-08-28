---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-cascadingcontrolsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template CascadingControlSource
<a name="aws-properties-quicksight-template-cascadingcontrolsource"></a>

The source controls that are used in a `CascadingControlConfiguration`.

## Syntax
<a name="aws-properties-quicksight-template-cascadingcontrolsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-cascadingcontrolsource-syntax.json"></a>

```
{
  "[ColumnToMatch](#cfn-quicksight-template-cascadingcontrolsource-columntomatch)" : {{ColumnIdentifier}},
  "[SourceSheetControlId](#cfn-quicksight-template-cascadingcontrolsource-sourcesheetcontrolid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-cascadingcontrolsource-syntax.yaml"></a>

```
  [ColumnToMatch](#cfn-quicksight-template-cascadingcontrolsource-columntomatch): {{
    ColumnIdentifier}}
  [SourceSheetControlId](#cfn-quicksight-template-cascadingcontrolsource-sourcesheetcontrolid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-cascadingcontrolsource-properties"></a>

`ColumnToMatch`  <a name="cfn-quicksight-template-cascadingcontrolsource-columntomatch"></a>
The column identifier that determines which column to look up for the source sheet control.
*Required*: No
*Type*: [ColumnIdentifier](aws-properties-quicksight-template-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceSheetControlId`  <a name="cfn-quicksight-template-cascadingcontrolsource-sourcesheetcontrolid"></a>
The source sheet control ID of a `CascadingControlSource`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
