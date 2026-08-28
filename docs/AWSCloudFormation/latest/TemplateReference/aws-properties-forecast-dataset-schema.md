---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-forecast-dataset-schema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Forecast::Dataset Schema
<a name="aws-properties-forecast-dataset-schema"></a>

Defines the fields of a dataset.

## Syntax
<a name="aws-properties-forecast-dataset-schema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-forecast-dataset-schema-syntax.json"></a>

```
{
  "[Attributes](#cfn-forecast-dataset-schema-attributes)" : {{[ AttributesItems, ... ]}}
}
```

### YAML
<a name="aws-properties-forecast-dataset-schema-syntax.yaml"></a>

```
  [Attributes](#cfn-forecast-dataset-schema-attributes): {{
    - AttributesItems}}
```

## Properties
<a name="aws-properties-forecast-dataset-schema-properties"></a>

`Attributes`  <a name="cfn-forecast-dataset-schema-attributes"></a>
An array of attributes specifying the name and type of each field in a dataset.
*Required*: No
*Type*: Array of [AttributesItems](aws-properties-forecast-dataset-attributesitems.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
