---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::ApplicationOutput KinesisStreamsOutput
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput"></a>

When configuring application output, identifies an Amazon Kinesis stream as the destination. You provide the stream Amazon Resource Name (ARN) and also an IAM role ARN that Amazon Kinesis Analytics can use to write to the stream on your behalf.

## Syntax
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput-syntax.json"></a>

```
{
  "[ResourceARN](#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-resourcearn)" : {{String}},
  "[RoleARN](#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput-syntax.yaml"></a>

```
  [ResourceARN](#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-resourcearn): {{String}}
  [RoleARN](#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-rolearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput-properties"></a>

`ResourceARN`  <a name="cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-resourcearn"></a>
ARN of the destination Amazon Kinesis stream to write to.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-rolearn"></a>
ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
