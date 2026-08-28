---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-fieldfolder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet FieldFolder
<a name="aws-properties-quicksight-dataset-fieldfolder"></a>

A FieldFolder element is a folder that contains fields and nested subfolders.

## Syntax
<a name="aws-properties-quicksight-dataset-fieldfolder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-fieldfolder-syntax.json"></a>

```
{
  "[Columns](#cfn-quicksight-dataset-fieldfolder-columns)" : {{[ String, ... ]}},
  "[Description](#cfn-quicksight-dataset-fieldfolder-description)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-fieldfolder-syntax.yaml"></a>

```
  [Columns](#cfn-quicksight-dataset-fieldfolder-columns): {{
    - String}}
  [Description](#cfn-quicksight-dataset-fieldfolder-description): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-fieldfolder-properties"></a>

`Columns`  <a name="cfn-quicksight-dataset-fieldfolder-columns"></a>
A folder has a list of columns. A column can only be in one folder.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-dataset-fieldfolder-description"></a>
The description for a field folder.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
