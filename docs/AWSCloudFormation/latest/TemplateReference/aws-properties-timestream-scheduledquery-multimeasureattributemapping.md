---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery MultiMeasureAttributeMapping
<a name="aws-properties-timestream-scheduledquery-multimeasureattributemapping"></a>

Attribute mapping for MULTI value measures.

## Syntax
<a name="aws-properties-timestream-scheduledquery-multimeasureattributemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-multimeasureattributemapping-syntax.json"></a>

```
{
  "[MeasureValueType](#cfn-timestream-scheduledquery-multimeasureattributemapping-measurevaluetype)" : {{String}},
  "[SourceColumn](#cfn-timestream-scheduledquery-multimeasureattributemapping-sourcecolumn)" : {{String}},
  "[TargetMultiMeasureAttributeName](#cfn-timestream-scheduledquery-multimeasureattributemapping-targetmultimeasureattributename)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-multimeasureattributemapping-syntax.yaml"></a>

```
  [MeasureValueType](#cfn-timestream-scheduledquery-multimeasureattributemapping-measurevaluetype): {{String}}
  [SourceColumn](#cfn-timestream-scheduledquery-multimeasureattributemapping-sourcecolumn): {{String}}
  [TargetMultiMeasureAttributeName](#cfn-timestream-scheduledquery-multimeasureattributemapping-targetmultimeasureattributename): {{String}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-multimeasureattributemapping-properties"></a>

`MeasureValueType`  <a name="cfn-timestream-scheduledquery-multimeasureattributemapping-measurevaluetype"></a>
Type of the attribute to be read from the source column.
*Required*: Yes
*Type*: String
*Allowed values*: `BIGINT | BOOLEAN | DOUBLE | VARCHAR | TIMESTAMP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceColumn`  <a name="cfn-timestream-scheduledquery-multimeasureattributemapping-sourcecolumn"></a>
Source column from where the attribute value is to be read.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetMultiMeasureAttributeName`  <a name="cfn-timestream-scheduledquery-multimeasureattributemapping-targetmultimeasureattributename"></a>
Custom name to be used for attribute name in derived table. If not provided, source column name would be used.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
