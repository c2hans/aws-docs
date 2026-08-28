---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-integerdatasetparameterdefaultvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet IntegerDatasetParameterDefaultValues
<a name="aws-properties-quicksight-dataset-integerdatasetparameterdefaultvalues"></a>

A list of default values for a given integer parameter. This structure only accepts static values.

## Syntax
<a name="aws-properties-quicksight-dataset-integerdatasetparameterdefaultvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-integerdatasetparameterdefaultvalues-syntax.json"></a>

```
{
  "[StaticValues](#cfn-quicksight-dataset-integerdatasetparameterdefaultvalues-staticvalues)" : {{[ Integer, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-integerdatasetparameterdefaultvalues-syntax.yaml"></a>

```
  [StaticValues](#cfn-quicksight-dataset-integerdatasetparameterdefaultvalues-staticvalues): {{
    - Integer}}
```

## Properties
<a name="aws-properties-quicksight-dataset-integerdatasetparameterdefaultvalues-properties"></a>

`StaticValues`  <a name="cfn-quicksight-dataset-integerdatasetparameterdefaultvalues-staticvalues"></a>
A list of static default values for a given integer parameter.
*Required*: No
*Type*: Array of Integer
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
