---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::ApplicationOutput KinesisStreamsOutput
<a name="aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput"></a>

When you configure a SQL-based Kinesis Data Analytics application's output, identifies a Kinesis data stream as the destination. You provide the stream Amazon Resource Name (ARN).

## Syntax
<a name="aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-syntax.json"></a>

```
{
  "[ResourceARN](#cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-syntax.yaml"></a>

```
  [ResourceARN](#cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-properties"></a>

`ResourceARN`  <a name="cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn"></a>
The ARN of the destination Kinesis data stream to write to.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput--seealso"></a>
+ [KinesisStreamsOutput](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisStreamsOutput.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
