---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSetEventDestination KinesisFirehoseDestination
<a name="aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination"></a>

An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.

## Syntax
<a name="aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination-syntax.json"></a>

```
{
  "[DeliveryStreamARN](#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn)" : {{String}},
  "[IAMRoleARN](#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination-syntax.yaml"></a>

```
  [DeliveryStreamARN](#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn): {{String}}
  [IAMRoleARN](#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn): {{String}}
```

## Properties
<a name="aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination-properties"></a>

`DeliveryStreamARN`  <a name="cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn"></a>
The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IAMRoleARN`  <a name="cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that the Amazon SES API v2 uses to send email events to the Amazon Kinesis Data Firehose stream.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
