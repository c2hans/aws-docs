---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-s3logdelivery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector S3LogDelivery
<a name="aws-properties-kafkaconnect-connector-s3logdelivery"></a>

Details about delivering logs to Amazon S3.

## Syntax
<a name="aws-properties-kafkaconnect-connector-s3logdelivery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-s3logdelivery-syntax.json"></a>

```
{
  "[Bucket](#cfn-kafkaconnect-connector-s3logdelivery-bucket)" : {{String}},
  "[Enabled](#cfn-kafkaconnect-connector-s3logdelivery-enabled)" : {{Boolean}},
  "[Prefix](#cfn-kafkaconnect-connector-s3logdelivery-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-s3logdelivery-syntax.yaml"></a>

```
  [Bucket](#cfn-kafkaconnect-connector-s3logdelivery-bucket): {{String}}
  [Enabled](#cfn-kafkaconnect-connector-s3logdelivery-enabled): {{Boolean}}
  [Prefix](#cfn-kafkaconnect-connector-s3logdelivery-prefix): {{String}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-s3logdelivery-properties"></a>

`Bucket`  <a name="cfn-kafkaconnect-connector-s3logdelivery-bucket"></a>
The name of the S3 bucket that is the destination for log delivery.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Enabled`  <a name="cfn-kafkaconnect-connector-s3logdelivery-enabled"></a>
Specifies whether connector logs get sent to the specified Amazon S3 destination.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Prefix`  <a name="cfn-kafkaconnect-connector-s3logdelivery-prefix"></a>
The S3 prefix that is the destination for log delivery.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
