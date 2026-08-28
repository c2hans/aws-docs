---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sheetcontrollayout.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SheetControlLayout
<a name="aws-properties-quicksight-template-sheetcontrollayout"></a>

A grid layout to define the placement of sheet control.

## Syntax
<a name="aws-properties-quicksight-template-sheetcontrollayout-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sheetcontrollayout-syntax.json"></a>

```
{
  "[Configuration](#cfn-quicksight-template-sheetcontrollayout-configuration)" : {{SheetControlLayoutConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sheetcontrollayout-syntax.yaml"></a>

```
  [Configuration](#cfn-quicksight-template-sheetcontrollayout-configuration): {{
    SheetControlLayoutConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-sheetcontrollayout-properties"></a>

`Configuration`  <a name="cfn-quicksight-template-sheetcontrollayout-configuration"></a>
The configuration that determines the elements and canvas size options of sheet control.
*Required*: Yes
*Type*: [SheetControlLayoutConfiguration](aws-properties-quicksight-template-sheetcontrollayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
