---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-cloudwatchlogsaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::TopicRule CloudwatchLogsAction
<a name="aws-properties-iot-topicrule-cloudwatchlogsaction"></a>

Describes an action that updates a CloudWatch log.

## Syntax
<a name="aws-properties-iot-topicrule-cloudwatchlogsaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-topicrule-cloudwatchlogsaction-syntax.json"></a>

```
{
  "[BatchMode](#cfn-iot-topicrule-cloudwatchlogsaction-batchmode)" : {{Boolean}},
  "[LogGroupName](#cfn-iot-topicrule-cloudwatchlogsaction-loggroupname)" : {{String}},
  "[RoleArn](#cfn-iot-topicrule-cloudwatchlogsaction-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-topicrule-cloudwatchlogsaction-syntax.yaml"></a>

```
  [BatchMode](#cfn-iot-topicrule-cloudwatchlogsaction-batchmode): {{Boolean}}
  [LogGroupName](#cfn-iot-topicrule-cloudwatchlogsaction-loggroupname): {{String}}
  [RoleArn](#cfn-iot-topicrule-cloudwatchlogsaction-rolearn): {{String}}
```

## Properties
<a name="aws-properties-iot-topicrule-cloudwatchlogsaction-properties"></a>

`BatchMode`  <a name="cfn-iot-topicrule-cloudwatchlogsaction-batchmode"></a>
Indicates whether batches of log records will be extracted and uploaded into CloudWatch.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupName`  <a name="cfn-iot-topicrule-cloudwatchlogsaction-loggroupname"></a>
The CloudWatch log name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-iot-topicrule-cloudwatchlogsaction-rolearn"></a>
The IAM role that allows access to the CloudWatch log.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
