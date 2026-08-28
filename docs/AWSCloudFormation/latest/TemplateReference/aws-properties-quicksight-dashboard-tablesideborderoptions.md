---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-tablesideborderoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard TableSideBorderOptions
<a name="aws-properties-quicksight-dashboard-tablesideborderoptions"></a>

The side border options for a table.

## Syntax
<a name="aws-properties-quicksight-dashboard-tablesideborderoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-tablesideborderoptions-syntax.json"></a>

```
{
  "[Bottom](#cfn-quicksight-dashboard-tablesideborderoptions-bottom)" : {{TableBorderOptions}},
  "[InnerHorizontal](#cfn-quicksight-dashboard-tablesideborderoptions-innerhorizontal)" : {{TableBorderOptions}},
  "[InnerVertical](#cfn-quicksight-dashboard-tablesideborderoptions-innervertical)" : {{TableBorderOptions}},
  "[Left](#cfn-quicksight-dashboard-tablesideborderoptions-left)" : {{TableBorderOptions}},
  "[Right](#cfn-quicksight-dashboard-tablesideborderoptions-right)" : {{TableBorderOptions}},
  "[Top](#cfn-quicksight-dashboard-tablesideborderoptions-top)" : {{TableBorderOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-tablesideborderoptions-syntax.yaml"></a>

```
  [Bottom](#cfn-quicksight-dashboard-tablesideborderoptions-bottom): {{
    TableBorderOptions}}
  [InnerHorizontal](#cfn-quicksight-dashboard-tablesideborderoptions-innerhorizontal): {{
    TableBorderOptions}}
  [InnerVertical](#cfn-quicksight-dashboard-tablesideborderoptions-innervertical): {{
    TableBorderOptions}}
  [Left](#cfn-quicksight-dashboard-tablesideborderoptions-left): {{
    TableBorderOptions}}
  [Right](#cfn-quicksight-dashboard-tablesideborderoptions-right): {{
    TableBorderOptions}}
  [Top](#cfn-quicksight-dashboard-tablesideborderoptions-top): {{
    TableBorderOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-tablesideborderoptions-properties"></a>

`Bottom`  <a name="cfn-quicksight-dashboard-tablesideborderoptions-bottom"></a>
The table border options of the bottom border.
*Required*: No
*Type*: [TableBorderOptions](aws-properties-quicksight-dashboard-tableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InnerHorizontal`  <a name="cfn-quicksight-dashboard-tablesideborderoptions-innerhorizontal"></a>
The table border options of the inner horizontal border.
*Required*: No
*Type*: [TableBorderOptions](aws-properties-quicksight-dashboard-tableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InnerVertical`  <a name="cfn-quicksight-dashboard-tablesideborderoptions-innervertical"></a>
The table border options of the inner vertical border.
*Required*: No
*Type*: [TableBorderOptions](aws-properties-quicksight-dashboard-tableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Left`  <a name="cfn-quicksight-dashboard-tablesideborderoptions-left"></a>
The table border options of the left border.
*Required*: No
*Type*: [TableBorderOptions](aws-properties-quicksight-dashboard-tableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Right`  <a name="cfn-quicksight-dashboard-tablesideborderoptions-right"></a>
The table border options of the right border.
*Required*: No
*Type*: [TableBorderOptions](aws-properties-quicksight-dashboard-tableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Top`  <a name="cfn-quicksight-dashboard-tablesideborderoptions-top"></a>
The table border options of the top border.
*Required*: No
*Type*: [TableBorderOptions](aws-properties-quicksight-dashboard-tableborderoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
