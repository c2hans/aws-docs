---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-timestream-scheduledquery-multimeasuremappings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Timestream::ScheduledQuery MultiMeasureMappings
<a name="aws-properties-timestream-scheduledquery-multimeasuremappings"></a>

Only one of MixedMeasureMappings or MultiMeasureMappings is to be provided. MultiMeasureMappings can be used to ingest data as multi measures in the derived table.

## Syntax
<a name="aws-properties-timestream-scheduledquery-multimeasuremappings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-timestream-scheduledquery-multimeasuremappings-syntax.json"></a>

```
{
  "[MultiMeasureAttributeMappings](#cfn-timestream-scheduledquery-multimeasuremappings-multimeasureattributemappings)" : {{[ MultiMeasureAttributeMapping, ... ]}},
  "[TargetMultiMeasureName](#cfn-timestream-scheduledquery-multimeasuremappings-targetmultimeasurename)" : {{String}}
}
```

### YAML
<a name="aws-properties-timestream-scheduledquery-multimeasuremappings-syntax.yaml"></a>

```
  [MultiMeasureAttributeMappings](#cfn-timestream-scheduledquery-multimeasuremappings-multimeasureattributemappings): {{
    - MultiMeasureAttributeMapping}}
  [TargetMultiMeasureName](#cfn-timestream-scheduledquery-multimeasuremappings-targetmultimeasurename): {{String}}
```

## Properties
<a name="aws-properties-timestream-scheduledquery-multimeasuremappings-properties"></a>

`MultiMeasureAttributeMappings`  <a name="cfn-timestream-scheduledquery-multimeasuremappings-multimeasureattributemappings"></a>
Required. Attribute mappings to be used for mapping query results to ingest data for multi-measure attributes.
*Required*: Yes
*Type*: Array of [MultiMeasureAttributeMapping](aws-properties-timestream-scheduledquery-multimeasureattributemapping.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetMultiMeasureName`  <a name="cfn-timestream-scheduledquery-multimeasuremappings-targetmultimeasurename"></a>
The name of the target multi-measure name in the derived table. This input is required when measureNameColumn is not provided. If MeasureNameColumn is provided, then value from that column will be used as multi-measure name.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
