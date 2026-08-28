---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-columnlevelpermissionrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet ColumnLevelPermissionRule
<a name="aws-properties-quicksight-dataset-columnlevelpermissionrule"></a>

A rule defined to grant access on one or more restricted columns. Each dataset can have multiple rules. To create a restricted column, you add it to one or more rules. Each rule must contain at least one column and at least one user or group. To be able to see a restricted column, a user or group needs to be added to a rule for that column.

## Syntax
<a name="aws-properties-quicksight-dataset-columnlevelpermissionrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-columnlevelpermissionrule-syntax.json"></a>

```
{
  "[ColumnNames](#cfn-quicksight-dataset-columnlevelpermissionrule-columnnames)" : {{[ String, ... ]}},
  "[Principals](#cfn-quicksight-dataset-columnlevelpermissionrule-principals)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-columnlevelpermissionrule-syntax.yaml"></a>

```
  [ColumnNames](#cfn-quicksight-dataset-columnlevelpermissionrule-columnnames): {{
    - String}}
  [Principals](#cfn-quicksight-dataset-columnlevelpermissionrule-principals): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-columnlevelpermissionrule-properties"></a>

`ColumnNames`  <a name="cfn-quicksight-dataset-columnlevelpermissionrule-columnnames"></a>
An array of column names.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Principals`  <a name="cfn-quicksight-dataset-columnlevelpermissionrule-principals"></a>
An array of Amazon Resource Names (ARNs) for Quick users or groups.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
