---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-dynamicdefaultvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DynamicDefaultValue
<a name="aws-properties-quicksight-dashboard-dynamicdefaultvalue"></a>

Defines different defaults to the users or groups based on mapping.

## Syntax
<a name="aws-properties-quicksight-dashboard-dynamicdefaultvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-dynamicdefaultvalue-syntax.json"></a>

```
{
  "[DefaultValueColumn](#cfn-quicksight-dashboard-dynamicdefaultvalue-defaultvaluecolumn)" : {{ColumnIdentifier}},
  "[GroupNameColumn](#cfn-quicksight-dashboard-dynamicdefaultvalue-groupnamecolumn)" : {{ColumnIdentifier}},
  "[UserNameColumn](#cfn-quicksight-dashboard-dynamicdefaultvalue-usernamecolumn)" : {{ColumnIdentifier}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-dynamicdefaultvalue-syntax.yaml"></a>

```
  [DefaultValueColumn](#cfn-quicksight-dashboard-dynamicdefaultvalue-defaultvaluecolumn): {{
    ColumnIdentifier}}
  [GroupNameColumn](#cfn-quicksight-dashboard-dynamicdefaultvalue-groupnamecolumn): {{
    ColumnIdentifier}}
  [UserNameColumn](#cfn-quicksight-dashboard-dynamicdefaultvalue-usernamecolumn): {{
    ColumnIdentifier}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-dynamicdefaultvalue-properties"></a>

`DefaultValueColumn`  <a name="cfn-quicksight-dashboard-dynamicdefaultvalue-defaultvaluecolumn"></a>
The column that contains the default value of each user or group.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-dashboard-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupNameColumn`  <a name="cfn-quicksight-dashboard-dynamicdefaultvalue-groupnamecolumn"></a>
The column that contains the group name.
*Required*: No
*Type*: [ColumnIdentifier](aws-properties-quicksight-dashboard-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserNameColumn`  <a name="cfn-quicksight-dashboard-dynamicdefaultvalue-usernamecolumn"></a>
The column that contains the username.
*Required*: No
*Type*: [ColumnIdentifier](aws-properties-quicksight-dashboard-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
