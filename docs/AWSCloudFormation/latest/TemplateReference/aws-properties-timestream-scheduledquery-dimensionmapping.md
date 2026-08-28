---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-dimensionmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery DimensionMapping
<a name="aws-properties-timestream-scheduledquery-dimensionmapping"></a>

This type is used to map column(s) from the query result to a dimension in the destination table.

## Syntax
<a name="aws-properties-timestream-scheduledquery-dimensionmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-dimensionmapping-syntax.json"></a>

```
{
  "[DimensionValueType](#cfn-timestream-scheduledquery-dimensionmapping-dimensionvaluetype)" : {{String}},
  "[Name](#cfn-timestream-scheduledquery-dimensionmapping-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-dimensionmapping-syntax.yaml"></a>

```
  [DimensionValueType](#cfn-timestream-scheduledquery-dimensionmapping-dimensionvaluetype): {{String}}
  [Name](#cfn-timestream-scheduledquery-dimensionmapping-name): {{String}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-dimensionmapping-properties"></a>

`DimensionValueType`  <a name="cfn-timestream-scheduledquery-dimensionmapping-dimensionvaluetype"></a>
Type for the dimension: VARCHAR
*Required*: Yes
*Type*: String
*Allowed values*: `VARCHAR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-timestream-scheduledquery-dimensionmapping-name"></a>
Column name from query result.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
