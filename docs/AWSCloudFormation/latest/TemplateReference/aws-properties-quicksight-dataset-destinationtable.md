---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-destinationtable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DestinationTable
<a name="aws-properties-quicksight-dataset-destinationtable"></a>

Defines a destination table in data preparation that receives the final transformed data.

## Syntax
<a name="aws-properties-quicksight-dataset-destinationtable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-destinationtable-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-destinationtable-alias)" : {{String}},
  "[Source](#cfn-quicksight-dataset-destinationtable-source)" : {{DestinationTableSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-destinationtable-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-destinationtable-alias): {{String}}
  [Source](#cfn-quicksight-dataset-destinationtable-source): {{
    DestinationTableSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-destinationtable-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-destinationtable-alias"></a>
Alias for the destination table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-destinationtable-source"></a>
The source configuration that specifies which transform operation provides data to this destination table.
*Required*: Yes
*Type*: [DestinationTableSource](aws-properties-quicksight-dataset-destinationtablesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
