---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application KinesisFirehoseInput
<a name="aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput"></a>

For a SQL-based Kinesis Data Analytics application, identifies a Kinesis Data Firehose delivery stream as the streaming source. You provide the delivery stream's Amazon Resource Name (ARN).

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput-syntax.json"></a>

```
{
  "[ResourceARN](#cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput-syntax.yaml"></a>

```
  [ResourceARN](#cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput-properties"></a>

`ResourceARN`  <a name="cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn"></a>
The Amazon Resource Name (ARN) of the delivery stream.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput--seealso"></a>
+ [KinesisFirehoseInput](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_KinesisFirehoseInput.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
