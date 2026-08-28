---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-attributeaggregationfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template AttributeAggregationFunction
<a name="aws-properties-quicksight-template-attributeaggregationfunction"></a>

Aggregation for attributes.

## Syntax
<a name="aws-properties-quicksight-template-attributeaggregationfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-attributeaggregationfunction-syntax.json"></a>

```
{
  "[SimpleAttributeAggregation](#cfn-quicksight-template-attributeaggregationfunction-simpleattributeaggregation)" : {{String}},
  "[ValueForMultipleValues](#cfn-quicksight-template-attributeaggregationfunction-valueformultiplevalues)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-attributeaggregationfunction-syntax.yaml"></a>

```
  [SimpleAttributeAggregation](#cfn-quicksight-template-attributeaggregationfunction-simpleattributeaggregation): {{String}}
  [ValueForMultipleValues](#cfn-quicksight-template-attributeaggregationfunction-valueformultiplevalues): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-attributeaggregationfunction-properties"></a>

`SimpleAttributeAggregation`  <a name="cfn-quicksight-template-attributeaggregationfunction-simpleattributeaggregation"></a>
The built-in aggregation functions for attributes.
+ `UNIQUE_VALUE`: Returns the unique value for a field, aggregated by the dimension fields.
*Required*: No
*Type*: String
*Allowed values*: `UNIQUE_VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueForMultipleValues`  <a name="cfn-quicksight-template-attributeaggregationfunction-valueformultiplevalues"></a>
Used by the `UNIQUE_VALUE` aggregation function. If there are multiple values for the field used by the aggregation, the value for this property will be returned instead. Defaults to '\*'.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
