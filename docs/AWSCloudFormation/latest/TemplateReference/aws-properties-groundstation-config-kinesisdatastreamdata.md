---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-config-kinesisdatastreamdata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::Config KinesisDataStreamData
<a name="aws-properties-groundstation-config-kinesisdatastreamdata"></a>

 Defines the configuration for delivering telemetry to an Amazon Kinesis Data Stream.

## Syntax
<a name="aws-properties-groundstation-config-kinesisdatastreamdata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-config-kinesisdatastreamdata-syntax.json"></a>

```
{
  "[KinesisDataStreamArn](#cfn-groundstation-config-kinesisdatastreamdata-kinesisdatastreamarn)" : {{String}},
  "[KinesisRoleArn](#cfn-groundstation-config-kinesisdatastreamdata-kinesisrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-config-kinesisdatastreamdata-syntax.yaml"></a>

```
  [KinesisDataStreamArn](#cfn-groundstation-config-kinesisdatastreamdata-kinesisdatastreamarn): {{String}}
  [KinesisRoleArn](#cfn-groundstation-config-kinesisdatastreamdata-kinesisrolearn): {{String}}
```

## Properties
<a name="aws-properties-groundstation-config-kinesisdatastreamdata-properties"></a>

`KinesisDataStreamArn`  <a name="cfn-groundstation-config-kinesisdatastreamdata-kinesisdatastreamarn"></a>
 The ARN of the Amazon Kinesis Data Stream where telemetry data will be delivered, such as `arn:aws:kinesis:us-east-2:123456789012:stream/my-telemetry-stream`.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-.]{1,63}:kinesis:[-a-z0-9]{1,50}:[0-9]{12}:stream/[a-zA-Z0-9_.-]{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KinesisRoleArn`  <a name="cfn-groundstation-config-kinesisdatastreamdata-kinesisrolearn"></a>
 The ARN of an IAM role that AWS Ground Station assumes to write telemetry data to the Kinesis Data Stream. This role must have permissions to perform `kinesis:PutRecord`, `kinesis:PutRecords`, and `kinesis:DescribeStream` actions on the specified stream.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[^:\n]+:iam::[^:\n]+:role\/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-groundstation-config-kinesisdatastreamdata--examples"></a>

### Create KinesisDataStreamData
<a name="aws-properties-groundstation-config-kinesisdatastreamdata--examples--Create_KinesisDataStreamData"></a>

The following example creates `KinesisDataStreamData` with the required IAM role and Kinesis stream configuration.

#### JSON
<a name="aws-properties-groundstation-config-kinesisdatastreamdata--examples--Create_KinesisDataStreamData--json"></a>

```
{
  "KinesisDataStreamData": {
    "KinesisDataStreamArn": "arn:aws:kinesis:us-east-2:123456789012:stream/my-telemetry-stream",
    "KinesisRoleArn": "arn:aws:iam::123456789012:role/GroundStationKinesisRole"
  }
}
```

#### YAML
<a name="aws-properties-groundstation-config-kinesisdatastreamdata--examples--Create_KinesisDataStreamData--yaml"></a>

```
KinesisDataStreamData:
  KinesisDataStreamArn: arn:aws:kinesis:us-east-2:123456789012:stream/my-telemetry-stream
  KinesisRoleArn: arn:aws:iam::123456789012:role/GroundStationKinesisRole
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
