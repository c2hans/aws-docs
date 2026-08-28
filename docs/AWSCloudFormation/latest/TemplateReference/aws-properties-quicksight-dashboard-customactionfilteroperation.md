---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-customactionfilteroperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard CustomActionFilterOperation
<a name="aws-properties-quicksight-dashboard-customactionfilteroperation"></a>

The filter operation that filters data included in a visual or in an entire sheet.

## Syntax
<a name="aws-properties-quicksight-dashboard-customactionfilteroperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-customactionfilteroperation-syntax.json"></a>

```
{
  "[SelectedFieldsConfiguration](#cfn-quicksight-dashboard-customactionfilteroperation-selectedfieldsconfiguration)" : {{FilterOperationSelectedFieldsConfiguration}},
  "[TargetVisualsConfiguration](#cfn-quicksight-dashboard-customactionfilteroperation-targetvisualsconfiguration)" : {{FilterOperationTargetVisualsConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-customactionfilteroperation-syntax.yaml"></a>

```
  [SelectedFieldsConfiguration](#cfn-quicksight-dashboard-customactionfilteroperation-selectedfieldsconfiguration): {{
    FilterOperationSelectedFieldsConfiguration}}
  [TargetVisualsConfiguration](#cfn-quicksight-dashboard-customactionfilteroperation-targetvisualsconfiguration): {{
    FilterOperationTargetVisualsConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-customactionfilteroperation-properties"></a>

`SelectedFieldsConfiguration`  <a name="cfn-quicksight-dashboard-customactionfilteroperation-selectedfieldsconfiguration"></a>
The configuration that chooses the fields to be filtered.
*Required*: Yes
*Type*: [FilterOperationSelectedFieldsConfiguration](aws-properties-quicksight-dashboard-filteroperationselectedfieldsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetVisualsConfiguration`  <a name="cfn-quicksight-dashboard-customactionfilteroperation-targetvisualsconfiguration"></a>
The configuration that chooses the target visuals to be filtered.
*Required*: Yes
*Type*: [FilterOperationTargetVisualsConfiguration](aws-properties-quicksight-dashboard-filteroperationtargetvisualsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
