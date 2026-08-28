---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-calculatedfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard CalculatedField
<a name="aws-properties-quicksight-dashboard-calculatedfield"></a>

The calculated field of an analysis.

## Syntax
<a name="aws-properties-quicksight-dashboard-calculatedfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-calculatedfield-syntax.json"></a>

```
{
  "[DataSetIdentifier](#cfn-quicksight-dashboard-calculatedfield-datasetidentifier)" : {{String}},
  "[Expression](#cfn-quicksight-dashboard-calculatedfield-expression)" : {{String}},
  "[Name](#cfn-quicksight-dashboard-calculatedfield-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-calculatedfield-syntax.yaml"></a>

```
  [DataSetIdentifier](#cfn-quicksight-dashboard-calculatedfield-datasetidentifier): {{String}}
  [Expression](#cfn-quicksight-dashboard-calculatedfield-expression): {{String}}
  [Name](#cfn-quicksight-dashboard-calculatedfield-name): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-calculatedfield-properties"></a>

`DataSetIdentifier`  <a name="cfn-quicksight-dashboard-calculatedfield-datasetidentifier"></a>
The data set that is used in this calculated field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-quicksight-dashboard-calculatedfield-expression"></a>
The expression of the calculated field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `32000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-dashboard-calculatedfield-name"></a>
The name of the calculated field.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
