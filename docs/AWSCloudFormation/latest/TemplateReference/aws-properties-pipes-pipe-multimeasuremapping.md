---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-multimeasuremapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe MultiMeasureMapping
<a name="aws-properties-pipes-pipe-multimeasuremapping"></a>

Maps multiple measures from the source event to the same Timestream for LiveAnalytics record.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html)

## Syntax
<a name="aws-properties-pipes-pipe-multimeasuremapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-multimeasuremapping-syntax.json"></a>

```
{
  "[MultiMeasureAttributeMappings](#cfn-pipes-pipe-multimeasuremapping-multimeasureattributemappings)" : {{[ MultiMeasureAttributeMapping, ... ]}},
  "[MultiMeasureName](#cfn-pipes-pipe-multimeasuremapping-multimeasurename)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-multimeasuremapping-syntax.yaml"></a>

```
  [MultiMeasureAttributeMappings](#cfn-pipes-pipe-multimeasuremapping-multimeasureattributemappings): {{
    - MultiMeasureAttributeMapping}}
  [MultiMeasureName](#cfn-pipes-pipe-multimeasuremapping-multimeasurename): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-multimeasuremapping-properties"></a>

`MultiMeasureAttributeMappings`  <a name="cfn-pipes-pipe-multimeasuremapping-multimeasureattributemappings"></a>
Mappings that represent multiple source event fields mapped to measures in the same Timestream for LiveAnalytics record.
*Required*: Yes
*Type*: Array of [MultiMeasureAttributeMapping](aws-properties-pipes-pipe-multimeasureattributemapping.md)
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiMeasureName`  <a name="cfn-pipes-pipe-multimeasuremapping-multimeasurename"></a>
The name of the multiple measurements per record (multi-measure).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
