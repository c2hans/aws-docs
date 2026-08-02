---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipetargettimestreamparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeTargetTimestreamParameters
<a name="aws-properties-pipes-pipe-pipetargettimestreamparameters"></a>

The parameters for using a Timestream for LiveAnalytics table as a target.

## Syntax
<a name="aws-properties-pipes-pipe-pipetargettimestreamparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipetargettimestreamparameters-syntax.json"></a>

```
{
  "[DimensionMappings](#cfn-pipes-pipe-pipetargettimestreamparameters-dimensionmappings)" : {{[ DimensionMapping, ... ]}},
  "[EpochTimeUnit](#cfn-pipes-pipe-pipetargettimestreamparameters-epochtimeunit)" : {{String}},
  "[MultiMeasureMappings](#cfn-pipes-pipe-pipetargettimestreamparameters-multimeasuremappings)" : {{[ MultiMeasureMapping, ... ]}},
  "[SingleMeasureMappings](#cfn-pipes-pipe-pipetargettimestreamparameters-singlemeasuremappings)" : {{[ SingleMeasureMapping, ... ]}},
  "[TimeFieldType](#cfn-pipes-pipe-pipetargettimestreamparameters-timefieldtype)" : {{String}},
  "[TimestampFormat](#cfn-pipes-pipe-pipetargettimestreamparameters-timestampformat)" : {{String}},
  "[TimeValue](#cfn-pipes-pipe-pipetargettimestreamparameters-timevalue)" : {{String}},
  "[VersionValue](#cfn-pipes-pipe-pipetargettimestreamparameters-versionvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipetargettimestreamparameters-syntax.yaml"></a>

```
  [DimensionMappings](#cfn-pipes-pipe-pipetargettimestreamparameters-dimensionmappings): {{
    - DimensionMapping}}
  [EpochTimeUnit](#cfn-pipes-pipe-pipetargettimestreamparameters-epochtimeunit): {{String}}
  [MultiMeasureMappings](#cfn-pipes-pipe-pipetargettimestreamparameters-multimeasuremappings): {{
    - MultiMeasureMapping}}
  [SingleMeasureMappings](#cfn-pipes-pipe-pipetargettimestreamparameters-singlemeasuremappings): {{
    - SingleMeasureMapping}}
  [TimeFieldType](#cfn-pipes-pipe-pipetargettimestreamparameters-timefieldtype): {{String}}
  [TimestampFormat](#cfn-pipes-pipe-pipetargettimestreamparameters-timestampformat): {{String}}
  [TimeValue](#cfn-pipes-pipe-pipetargettimestreamparameters-timevalue): {{String}}
  [VersionValue](#cfn-pipes-pipe-pipetargettimestreamparameters-versionvalue): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipetargettimestreamparameters-properties"></a>

`DimensionMappings`  <a name="cfn-pipes-pipe-pipetargettimestreamparameters-dimensionmappings"></a>
Map source data to dimensions in the target Timestream for LiveAnalytics table.
For more information, see [Amazon Timestream for LiveAnalytics concepts](https://docs.aws.amazon.com/timestream/latest/developerguide/concepts.html)
*Required*: Yes
*Type*: Array of [DimensionMapping](aws-properties-pipes-pipe-dimensionmapping.md)
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EpochTimeUnit`  <a name="cfn-pipes-pipe-pipetargettimestreamparameters-epochtimeunit"></a>
The granularity of the time units used. Default is `MILLISECONDS`.
Required if `TimeFieldType` is specified as `EPOCH`.
*Required*: No
*Type*: String
*Allowed values*: `MILLISECONDS | SECONDS | MICROSECONDS | NANOSECONDS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiMeasureMappings`  <a name="cfn-pipes-pipe-pipetargettimestreamparameters-multimeasuremappings"></a>
Maps multiple measures from the source event to the same record in the specified Timestream for LiveAnalytics table.
*Required*: No
*Type*: Array of [MultiMeasureMapping](aws-properties-pipes-pipe-multimeasuremapping.md)
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SingleMeasureMappings`  <a name="cfn-pipes-pipe-pipetargettimestreamparameters-singlemeasuremappings"></a>
Mappings of single source data fields to individual records in the specified Timestream for LiveAnalytics table.
*Required*: No
*Type*: Array of [SingleMeasureMapping](aws-properties-pipes-pipe-singlemeasuremapping.md)
*Minimum*: `0`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeFieldType`  <a name="cfn-pipes-pipe-pipetargettimestreamparameters-timefieldtype"></a>
The type of time value used.
The default is `EPOCH`.
*Required*: No
*Type*: String
*Allowed values*: `EPOCH | TIMESTAMP_FORMAT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimestampFormat`  <a name="cfn-pipes-pipe-pipetargettimestreamparameters-timestampformat"></a>
How to format the timestamps. For example, `yyyy-MM-dd'T'HH:mm:ss'Z'`.
Required if `TimeFieldType` is specified as `TIMESTAMP_FORMAT`.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeValue`  <a name="cfn-pipes-pipe-pipetargettimestreamparameters-timevalue"></a>
Dynamic path to the source data field that represents the time value for your data.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionValue`  <a name="cfn-pipes-pipe-pipetargettimestreamparameters-versionvalue"></a>
64 bit version value or source data field that represents the version value for your data.
Write requests with a higher version number will update the existing measure values of the record and version. In cases where the measure value is the same, the version will still be updated.
Default value is 1.
Timestream for LiveAnalytics does not support updating partial measure values in a record.
Write requests for duplicate data with a higher version number will update the existing measure value and version. In cases where the measure value is the same, `Version` will still be updated. Default value is `1`.
`Version` must be `1` or greater, or you will receive a `ValidationException` error.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
