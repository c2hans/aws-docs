---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-cascadingcontrolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template CascadingControlConfiguration
<a name="aws-properties-quicksight-template-cascadingcontrolconfiguration"></a>

The values that are displayed in a control can be configured to only show values that are valid based on what's selected in other controls.

## Syntax
<a name="aws-properties-quicksight-template-cascadingcontrolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-cascadingcontrolconfiguration-syntax.json"></a>

```
{
  "[SourceControls](#cfn-quicksight-template-cascadingcontrolconfiguration-sourcecontrols)" : {{[ CascadingControlSource, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-cascadingcontrolconfiguration-syntax.yaml"></a>

```
  [SourceControls](#cfn-quicksight-template-cascadingcontrolconfiguration-sourcecontrols): {{
    - CascadingControlSource}}
```

## Properties
<a name="aws-properties-quicksight-template-cascadingcontrolconfiguration-properties"></a>

`SourceControls`  <a name="cfn-quicksight-template-cascadingcontrolconfiguration-sourcecontrols"></a>
A list of source controls that determine the values that are used in the current control.
*Required*: No
*Type*: Array of [CascadingControlSource](aws-properties-quicksight-template-cascadingcontrolsource.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
