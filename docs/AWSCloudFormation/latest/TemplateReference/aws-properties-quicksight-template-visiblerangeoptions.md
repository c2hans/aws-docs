---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-visiblerangeoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template VisibleRangeOptions
<a name="aws-properties-quicksight-template-visiblerangeoptions"></a>

The range options for the data zoom scroll bar.

## Syntax
<a name="aws-properties-quicksight-template-visiblerangeoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-visiblerangeoptions-syntax.json"></a>

```
{
  "[PercentRange](#cfn-quicksight-template-visiblerangeoptions-percentrange)" : {{PercentVisibleRange}}
}
```

### YAML
<a name="aws-properties-quicksight-template-visiblerangeoptions-syntax.yaml"></a>

```
  [PercentRange](#cfn-quicksight-template-visiblerangeoptions-percentrange): {{
    PercentVisibleRange}}
```

## Properties
<a name="aws-properties-quicksight-template-visiblerangeoptions-properties"></a>

`PercentRange`  <a name="cfn-quicksight-template-visiblerangeoptions-percentrange"></a>
The percent range in the visible range.
*Required*: No
*Type*: [PercentVisibleRange](aws-properties-quicksight-template-percentvisiblerange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
