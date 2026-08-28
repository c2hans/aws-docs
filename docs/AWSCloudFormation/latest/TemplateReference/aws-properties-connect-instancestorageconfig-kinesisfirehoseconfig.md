---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::InstanceStorageConfig KinesisFirehoseConfig
<a name="aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig"></a>

Configuration information of a Kinesis Data Firehose delivery stream.

## Syntax
<a name="aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig-syntax.json"></a>

```
{
  "[FirehoseArn](#cfn-connect-instancestorageconfig-kinesisfirehoseconfig-firehosearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig-syntax.yaml"></a>

```
  [FirehoseArn](#cfn-connect-instancestorageconfig-kinesisfirehoseconfig-firehosearn): {{String}}
```

## Properties
<a name="aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig-properties"></a>

`FirehoseArn`  <a name="cfn-connect-instancestorageconfig-kinesisfirehoseconfig-firehosearn"></a>
The Amazon Resource Name (ARN) of the delivery stream.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:firehose:[-a-z0-9]*:[0-9]{12}:deliverystream/[-a-zA-Z0-9_.]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
