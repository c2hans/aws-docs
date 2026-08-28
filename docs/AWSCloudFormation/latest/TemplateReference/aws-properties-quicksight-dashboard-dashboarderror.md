---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dashboarderror.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DashboardError
<a name="aws-properties-quicksight-dashboard-dashboarderror"></a>

Dashboard error.

## Syntax
<a name="aws-properties-quicksight-dashboard-dashboarderror-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dashboarderror-syntax.json"></a>

```
{
  "[Message](#cfn-quicksight-dashboard-dashboarderror-message)" : {{String}},
  "[Type](#cfn-quicksight-dashboard-dashboarderror-type)" : {{String}},
  "[ViolatedEntities](#cfn-quicksight-dashboard-dashboarderror-violatedentities)" : {{[ Entity, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dashboarderror-syntax.yaml"></a>

```
  [Message](#cfn-quicksight-dashboard-dashboarderror-message): {{String}}
  [Type](#cfn-quicksight-dashboard-dashboarderror-type): {{String}}
  [ViolatedEntities](#cfn-quicksight-dashboard-dashboarderror-violatedentities): {{
    - Entity}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dashboarderror-properties"></a>

`Message`  <a name="cfn-quicksight-dashboard-dashboarderror-message"></a>
Message.
*Required*: No
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-dashboard-dashboarderror-type"></a>
Type.
*Required*: No
*Type*: String
*Allowed values*: `ACCESS_DENIED | SOURCE_NOT_FOUND | DATA_SET_NOT_FOUND | INTERNAL_FAILURE | PARAMETER_VALUE_INCOMPATIBLE | PARAMETER_TYPE_INVALID | PARAMETER_NOT_FOUND | COLUMN_TYPE_MISMATCH | COLUMN_GEOGRAPHIC_ROLE_MISMATCH | COLUMN_REPLACEMENT_MISSING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ViolatedEntities`  <a name="cfn-quicksight-dashboard-dashboarderror-violatedentities"></a>
Lists the violated entities that caused the dashboard error.
*Required*: No
*Type*: Array of [Entity](aws-properties-quicksight-dashboard-entity.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
