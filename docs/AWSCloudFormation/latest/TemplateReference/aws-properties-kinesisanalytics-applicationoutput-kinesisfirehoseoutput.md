---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalytics::ApplicationOutput KinesisFirehoseOutput
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput"></a>

When configuring application output, identifies an Amazon Kinesis Firehose delivery stream as the destination. You provide the stream Amazon Resource Name (ARN) and an IAM role that enables Amazon Kinesis Analytics to write to the stream on your behalf.

## Syntax
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-syntax.json"></a>

```
{
  "[ResourceARN](#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-resourcearn)" : {{String}},
  "[RoleARN](#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-syntax.yaml"></a>

```
  [ResourceARN](#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-resourcearn): {{String}}
  [RoleARN](#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-rolearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-properties"></a>

`ResourceARN`  <a name="cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-resourcearn"></a>
ARN of the destination Amazon Kinesis Firehose delivery stream to write to.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleARN`  <a name="cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-rolearn"></a>
ARN of the IAM role that Amazon Kinesis Analytics can assume to write to the destination stream on your behalf. You need to grant the necessary permissions to this role.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
