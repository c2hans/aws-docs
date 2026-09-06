---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-multimeasureattributemapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe MultiMeasureAttributeMapping
<a name="aws-properties-pipes-pipe-multimeasureattributemapping"></a>

A mapping of a source event data field to a measure in a Timestream for LiveAnalytics record.

## Syntax
<a name="aws-properties-pipes-pipe-multimeasureattributemapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-multimeasureattributemapping-syntax.json"></a>

```
{
  "[MeasureValue](#cfn-pipes-pipe-multimeasureattributemapping-measurevalue)" : {{String}},
  "[MeasureValueType](#cfn-pipes-pipe-multimeasureattributemapping-measurevaluetype)" : {{String}},
  "[MultiMeasureAttributeName](#cfn-pipes-pipe-multimeasureattributemapping-multimeasureattributename)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-multimeasureattributemapping-syntax.yaml"></a>

```
  [MeasureValue](#cfn-pipes-pipe-multimeasureattributemapping-measurevalue): {{String}}
  [MeasureValueType](#cfn-pipes-pipe-multimeasureattributemapping-measurevaluetype): {{String}}
  [MultiMeasureAttributeName](#cfn-pipes-pipe-multimeasureattributemapping-multimeasureattributename): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-multimeasureattributemapping-properties"></a>

`MeasureValue`  <a name="cfn-pipes-pipe-multimeasureattributemapping-measurevalue"></a>
Dynamic path to the measurement attribute in the source event.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MeasureValueType`  <a name="cfn-pipes-pipe-multimeasureattributemapping-measurevaluetype"></a>
Data type of the measurement attribute in the source event.
*Required*: Yes
*Type*: String
*Allowed values*: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiMeasureAttributeName`  <a name="cfn-pipes-pipe-multimeasureattributemapping-multimeasureattributename"></a>
Target measure name to be used.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
