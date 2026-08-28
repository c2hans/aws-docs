---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-dateaxisoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DateAxisOptions
<a name="aws-properties-quicksight-template-dateaxisoptions"></a>

The options that determine how a date axis is displayed.

## Syntax
<a name="aws-properties-quicksight-template-dateaxisoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-dateaxisoptions-syntax.json"></a>

```
{
  "[MissingDateVisibility](#cfn-quicksight-template-dateaxisoptions-missingdatevisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-dateaxisoptions-syntax.yaml"></a>

```
  [MissingDateVisibility](#cfn-quicksight-template-dateaxisoptions-missingdatevisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-dateaxisoptions-properties"></a>

`MissingDateVisibility`  <a name="cfn-quicksight-template-dateaxisoptions-missingdatevisibility"></a>
Determines whether or not missing dates are displayed.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
