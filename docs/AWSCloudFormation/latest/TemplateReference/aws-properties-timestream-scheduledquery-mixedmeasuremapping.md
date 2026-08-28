---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery MixedMeasureMapping
<a name="aws-properties-timestream-scheduledquery-mixedmeasuremapping"></a>

MixedMeasureMappings are mappings that can be used to ingest data into a mixture of narrow and multi measures in the derived table.

## Syntax
<a name="aws-properties-timestream-scheduledquery-mixedmeasuremapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-mixedmeasuremapping-syntax.json"></a>

```
{
  "[MeasureName](#cfn-timestream-scheduledquery-mixedmeasuremapping-measurename)" : {{String}},
  "[MeasureValueType](#cfn-timestream-scheduledquery-mixedmeasuremapping-measurevaluetype)" : {{String}},
  "[MultiMeasureAttributeMappings](#cfn-timestream-scheduledquery-mixedmeasuremapping-multimeasureattributemappings)" : {{[ MultiMeasureAttributeMapping, ... ]}},
  "[SourceColumn](#cfn-timestream-scheduledquery-mixedmeasuremapping-sourcecolumn)" : {{String}},
  "[TargetMeasureName](#cfn-timestream-scheduledquery-mixedmeasuremapping-targetmeasurename)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-mixedmeasuremapping-syntax.yaml"></a>

```
  [MeasureName](#cfn-timestream-scheduledquery-mixedmeasuremapping-measurename): {{String}}
  [MeasureValueType](#cfn-timestream-scheduledquery-mixedmeasuremapping-measurevaluetype): {{String}}
  [MultiMeasureAttributeMappings](#cfn-timestream-scheduledquery-mixedmeasuremapping-multimeasureattributemappings): {{
    - MultiMeasureAttributeMapping}}
  [SourceColumn](#cfn-timestream-scheduledquery-mixedmeasuremapping-sourcecolumn): {{String}}
  [TargetMeasureName](#cfn-timestream-scheduledquery-mixedmeasuremapping-targetmeasurename): {{String}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-mixedmeasuremapping-properties"></a>

`MeasureName`  <a name="cfn-timestream-scheduledquery-mixedmeasuremapping-measurename"></a>
Refers to the value of measure\_name in a result row. This field is required if MeasureNameColumn is provided.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MeasureValueType`  <a name="cfn-timestream-scheduledquery-mixedmeasuremapping-measurevaluetype"></a>
Type of the value that is to be read from sourceColumn. If the mapping is for MULTI, use MeasureValueType.MULTI.
*Required*: Yes
*Type*: String
*Allowed values*: `BIGINT | BOOLEAN | DOUBLE | VARCHAR | MULTI`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MultiMeasureAttributeMappings`  <a name="cfn-timestream-scheduledquery-mixedmeasuremapping-multimeasureattributemappings"></a>
Required when measureValueType is MULTI. Attribute mappings for MULTI value measures.
*Required*: No
*Type*: Array of [MultiMeasureAttributeMapping](aws-properties-timestream-scheduledquery-multimeasureattributemapping.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceColumn`  <a name="cfn-timestream-scheduledquery-mixedmeasuremapping-sourcecolumn"></a>
This field refers to the source column from which measure-value is to be read for result materialization.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetMeasureName`  <a name="cfn-timestream-scheduledquery-mixedmeasuremapping-targetmeasurename"></a>
Target measure name to be used. If not provided, the target measure name by default would be measure-name if provided, or sourceColumn otherwise.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
