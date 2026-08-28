---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-simpleclustermarker.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SimpleClusterMarker
<a name="aws-properties-quicksight-dashboard-simpleclustermarker"></a>

The simple cluster marker of the cluster marker.

## Syntax
<a name="aws-properties-quicksight-dashboard-simpleclustermarker-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-simpleclustermarker-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-dashboard-simpleclustermarker-color)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-simpleclustermarker-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-dashboard-simpleclustermarker-color): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-simpleclustermarker-properties"></a>

`Color`  <a name="cfn-quicksight-dashboard-simpleclustermarker-color"></a>
The color of the simple cluster marker.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
