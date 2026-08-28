---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-singlemeasuremapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe SingleMeasureMapping
<a name="aws-properties-pipes-pipe-singlemeasuremapping"></a>

Maps a single source data field to a single record in the specified Timestream for LiveAnalytics table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html)

## Syntax
<a name="aws-properties-pipes-pipe-singlemeasuremapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-singlemeasuremapping-syntax.json"></a>

```
{
  "[MeasureName](#cfn-pipes-pipe-singlemeasuremapping-measurename)" : {{String}},
  "[MeasureValue](#cfn-pipes-pipe-singlemeasuremapping-measurevalue)" : {{String}},
  "[MeasureValueType](#cfn-pipes-pipe-singlemeasuremapping-measurevaluetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-singlemeasuremapping-syntax.yaml"></a>

```
  [MeasureName](#cfn-pipes-pipe-singlemeasuremapping-measurename): {{String}}
  [MeasureValue](#cfn-pipes-pipe-singlemeasuremapping-measurevalue): {{String}}
  [MeasureValueType](#cfn-pipes-pipe-singlemeasuremapping-measurevaluetype): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-singlemeasuremapping-properties"></a>

`MeasureName`  <a name="cfn-pipes-pipe-singlemeasuremapping-measurename"></a>
Target measure name for the measurement attribute in the Timestream table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MeasureValue`  <a name="cfn-pipes-pipe-singlemeasuremapping-measurevalue"></a>
Dynamic path of the source field to map to the measure in the record.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MeasureValueType`  <a name="cfn-pipes-pipe-singlemeasuremapping-measurevaluetype"></a>
Data type of the source field.
*Required*: Yes
*Type*: String
*Allowed values*: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
