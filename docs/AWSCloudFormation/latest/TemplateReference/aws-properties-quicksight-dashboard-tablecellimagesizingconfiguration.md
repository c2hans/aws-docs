---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-tablecellimagesizingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TableCellImageSizingConfiguration
<a name="aws-properties-quicksight-dashboard-tablecellimagesizingconfiguration"></a>

The sizing options for the table image configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-tablecellimagesizingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-tablecellimagesizingconfiguration-syntax.json"></a>

```
{
  "[TableCellImageScalingConfiguration](#cfn-quicksight-dashboard-tablecellimagesizingconfiguration-tablecellimagescalingconfiguration)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-tablecellimagesizingconfiguration-syntax.yaml"></a>

```
  [TableCellImageScalingConfiguration](#cfn-quicksight-dashboard-tablecellimagesizingconfiguration-tablecellimagescalingconfiguration): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-tablecellimagesizingconfiguration-properties"></a>

`TableCellImageScalingConfiguration`  <a name="cfn-quicksight-dashboard-tablecellimagesizingconfiguration-tablecellimagescalingconfiguration"></a>
The cell scaling configuration of the sizing options for the table image configuration.
*Required*: No
*Type*: String
*Allowed values*: `FIT_TO_CELL_HEIGHT | FIT_TO_CELL_WIDTH | DO_NOT_SCALE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
