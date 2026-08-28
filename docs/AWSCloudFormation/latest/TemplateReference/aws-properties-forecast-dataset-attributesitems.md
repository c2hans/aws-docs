---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-forecast-dataset-attributesitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Forecast::Dataset AttributesItems
<a name="aws-properties-forecast-dataset-attributesitems"></a>

<a name="aws-properties-forecast-dataset-attributesitems-description"></a>The `AttributesItems` property type specifies Property description not available. for an [AWS::Forecast::Dataset](aws-resource-forecast-dataset.md).

## Syntax
<a name="aws-properties-forecast-dataset-attributesitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-forecast-dataset-attributesitems-syntax.json"></a>

```
{
  "[AttributeName](#cfn-forecast-dataset-attributesitems-attributename)" : {{String}},
  "[AttributeType](#cfn-forecast-dataset-attributesitems-attributetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-forecast-dataset-attributesitems-syntax.yaml"></a>

```
  [AttributeName](#cfn-forecast-dataset-attributesitems-attributename): {{String}}
  [AttributeType](#cfn-forecast-dataset-attributesitems-attributetype): {{String}}
```

## Properties
<a name="aws-properties-forecast-dataset-attributesitems-properties"></a>

`AttributeName`  <a name="cfn-forecast-dataset-attributesitems-attributename"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AttributeType`  <a name="cfn-forecast-dataset-attributesitems-attributetype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `string | integer | float | timestamp | geolocation`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
