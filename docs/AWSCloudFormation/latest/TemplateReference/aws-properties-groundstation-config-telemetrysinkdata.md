---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-telemetrysinkdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config TelemetrySinkData
<a name="aws-properties-groundstation-config-telemetrysinkdata"></a>

 Contains configuration data for a telemetry sink. The specific data structure depends on the sink type being configured.

## Syntax
<a name="aws-properties-groundstation-config-telemetrysinkdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-telemetrysinkdata-syntax.json"></a>

```
{
  "[KinesisDataStreamData](#cfn-groundstation-config-telemetrysinkdata-kinesisdatastreamdata)" : {{KinesisDataStreamData}}
}
```

### YAML
<a name="aws-properties-groundstation-config-telemetrysinkdata-syntax.yaml"></a>

```
  [KinesisDataStreamData](#cfn-groundstation-config-telemetrysinkdata-kinesisdatastreamdata): {{
    KinesisDataStreamData}}
```

## Properties
<a name="aws-properties-groundstation-config-telemetrysinkdata-properties"></a>

`KinesisDataStreamData`  <a name="cfn-groundstation-config-telemetrysinkdata-kinesisdatastreamdata"></a>
 Configuration data for delivering telemetry to a Kinesis Data Stream stream.
*Required*: No
*Type*: [KinesisDataStreamData](aws-properties-groundstation-config-kinesisdatastreamdata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-telemetrysinkdata--examples"></a>

### Create TelemetrySinkData for Kinesis
<a name="aws-properties-groundstation-config-telemetrysinkdata--examples--Create_TelemetrySinkData_for_Kinesis"></a>

The following example creates `TelemetrySinkData` configured for Amazon Kinesis Data Stream delivery.

#### JSON
<a name="aws-properties-groundstation-config-telemetrysinkdata--examples--Create_TelemetrySinkData_for_Kinesis--json"></a>

```
{
  "TelemetrySinkData": {
    "KinesisDataStreamData": {
      "KinesisDataStreamArn": "arn:aws:kinesis:us-east-2:123456789012:stream/my-telemetry-stream",
      "KinesisRoleArn": "arn:aws:iam::123456789012:role/GroundStationKinesisRole"
    }
  }
}
```

#### YAML
<a name="aws-properties-groundstation-config-telemetrysinkdata--examples--Create_TelemetrySinkData_for_Kinesis--yaml"></a>

```
TelemetrySinkData:
  KinesisDataStreamData:
    KinesisDataStreamArn: arn:aws:kinesis:us-east-2:123456789012:stream/my-telemetry-stream
    KinesisRoleArn: arn:aws:iam::123456789012:role/GroundStationKinesisRole
```
