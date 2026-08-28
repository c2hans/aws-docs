---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::RealtimeLogConfig KinesisStreamConfig
<a name="aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig"></a>

Contains information about the Amazon Kinesis data stream where you are sending real-time log data.

## Syntax
<a name="aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig-syntax.json"></a>

```
{
  "[RoleArn](#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-rolearn)" : {{String}},
  "[StreamArn](#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-streamarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig-syntax.yaml"></a>

```
  [RoleArn](#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-rolearn): {{String}}
  [StreamArn](#cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-streamarn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-realtimelogconfig-kinesisstreamconfig-properties"></a>

`RoleArn`  <a name="cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-rolearn"></a>
The Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role that CloudFront can use to send real-time log data to your Kinesis data stream.
For more information the IAM role, see [Real-time log configuration IAM role](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-iam-role) in the *Amazon CloudFront Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamArn`  <a name="cfn-cloudfront-realtimelogconfig-kinesisstreamconfig-streamarn"></a>
The Amazon Resource Name (ARN) of the Kinesis data stream where you are sending real-time log data.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
