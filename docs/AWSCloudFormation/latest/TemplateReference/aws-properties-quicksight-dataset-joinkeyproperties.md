---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-joinkeyproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet JoinKeyProperties
<a name="aws-properties-quicksight-dataset-joinkeyproperties"></a>

Properties associated with the columns participating in a join.

## Syntax
<a name="aws-properties-quicksight-dataset-joinkeyproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-joinkeyproperties-syntax.json"></a>

```
{
  "[UniqueKey](#cfn-quicksight-dataset-joinkeyproperties-uniquekey)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-joinkeyproperties-syntax.yaml"></a>

```
  [UniqueKey](#cfn-quicksight-dataset-joinkeyproperties-uniquekey): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-dataset-joinkeyproperties-properties"></a>

`UniqueKey`  <a name="cfn-quicksight-dataset-joinkeyproperties-uniquekey"></a>
A value that indicates that a row in a table is uniquely identified by the columns in a join key. This is used by Quick to optimize query performance.
*Required*: No
*Type*: [Boolean](aws-properties-quicksight-dataset-uniquekey.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
