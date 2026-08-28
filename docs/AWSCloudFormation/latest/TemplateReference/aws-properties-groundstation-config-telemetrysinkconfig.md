---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-telemetrysinkconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config TelemetrySinkConfig
<a name="aws-properties-groundstation-config-telemetrysinkconfig"></a>

 Provides information about how AWS Ground Station should deliver telemetry during contacts.

## Syntax
<a name="aws-properties-groundstation-config-telemetrysinkconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-telemetrysinkconfig-syntax.json"></a>

```
{
  "[TelemetrySinkData](#cfn-groundstation-config-telemetrysinkconfig-telemetrysinkdata)" : {{TelemetrySinkData}},
  "[TelemetrySinkType](#cfn-groundstation-config-telemetrysinkconfig-telemetrysinktype)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-config-telemetrysinkconfig-syntax.yaml"></a>

```
  [TelemetrySinkData](#cfn-groundstation-config-telemetrysinkconfig-telemetrysinkdata): {{
    TelemetrySinkData}}
  [TelemetrySinkType](#cfn-groundstation-config-telemetrysinkconfig-telemetrysinktype): {{String}}
```

## Properties
<a name="aws-properties-groundstation-config-telemetrysinkconfig-properties"></a>

`TelemetrySinkData`  <a name="cfn-groundstation-config-telemetrysinkconfig-telemetrysinkdata"></a>
 Configuration data for the telemetry sink. The structure of this data depends on the telemetry sink type specified.
*Required*: Yes
*Type*: [TelemetrySinkData](aws-properties-groundstation-config-telemetrysinkdata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TelemetrySinkType`  <a name="cfn-groundstation-config-telemetrysinkconfig-telemetrysinktype"></a>
 Type of telemetry sink where telemetry is to be delivered. Currently, only `KINESIS_DATA_STREAM` is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `KINESIS_DATA_STREAM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-telemetrysinkconfig--examples"></a>

### Create a TelemetrySinkConfig
<a name="aws-properties-groundstation-config-telemetrysinkconfig--examples--Create_a_TelemetrySinkConfig"></a>

The following example creates a Ground Station `TelemetrySinkConfig` that delivers telemetry to an Amazon Kinesis Data Stream.

#### JSON
<a name="aws-properties-groundstation-config-telemetrysinkconfig--examples--Create_a_TelemetrySinkConfig--json"></a>

```
{
  "TelemetrySinkConfig": {
    "TelemetrySinkType": "KINESIS_DATA_STREAM",
    "TelemetrySinkData": {
      "KinesisDataStreamData": {
        "KinesisDataStreamArn": "arn:aws:kinesis:us-west-2:123456789012:stream/my-telemetry-stream",
        "KinesisRoleArn": "arn:aws:iam::123456789012:role/GroundStationKinesisRole"
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-groundstation-config-telemetrysinkconfig--examples--Create_a_TelemetrySinkConfig--yaml"></a>

```
TelemetrySinkConfig:
  TelemetrySinkType: KINESIS_DATA_STREAM
  TelemetrySinkData:
    KinesisDataStreamData:
      KinesisDataStreamArn: arn:aws:kinesis:us-west-2:123456789012:stream/my-telemetry-stream
      KinesisRoleArn: arn:aws:iam::123456789012:role/GroundStationKinesisRole
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
