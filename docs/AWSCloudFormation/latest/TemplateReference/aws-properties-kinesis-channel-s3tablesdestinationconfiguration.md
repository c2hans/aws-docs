---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesis-channel-s3tablesdestinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel S3TablesDestinationConfiguration
<a name="aws-properties-kinesis-channel-s3tablesdestinationconfiguration"></a>

The configuration for delivery to streaming tables on Apache Iceberg. Used in CreateChannel.

## Syntax
<a name="aws-properties-kinesis-channel-s3tablesdestinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesis-channel-s3tablesdestinationconfiguration-syntax.json"></a>

```
{
  "[DataFreshnessInSeconds](#cfn-kinesis-channel-s3tablesdestinationconfiguration-datafreshnessinseconds)" : {{Integer}},
  "[DeadLetterQueueS3Configuration](#cfn-kinesis-channel-s3tablesdestinationconfiguration-deadletterqueues3configuration)" : {{DeadLetterQueueS3Configuration}},
  "[S3TablesConfigurationList](#cfn-kinesis-channel-s3tablesdestinationconfiguration-s3tablesconfigurationlist)" : {{[ S3TableConfiguration, ... ]}}
}
```

### YAML
<a name="aws-properties-kinesis-channel-s3tablesdestinationconfiguration-syntax.yaml"></a>

```
  [DataFreshnessInSeconds](#cfn-kinesis-channel-s3tablesdestinationconfiguration-datafreshnessinseconds): {{Integer}}
  [DeadLetterQueueS3Configuration](#cfn-kinesis-channel-s3tablesdestinationconfiguration-deadletterqueues3configuration): {{
    DeadLetterQueueS3Configuration}}
  [S3TablesConfigurationList](#cfn-kinesis-channel-s3tablesdestinationconfiguration-s3tablesconfigurationlist): {{
    - S3TableConfiguration}}
```

## Properties
<a name="aws-properties-kinesis-channel-s3tablesdestinationconfiguration-properties"></a>

`DataFreshnessInSeconds`  <a name="cfn-kinesis-channel-s3tablesdestinationconfiguration-datafreshnessinseconds"></a>
The maximum age, in seconds, of undelivered data before the channel delivers it to the destination. The default value is 300 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeadLetterQueueS3Configuration`  <a name="cfn-kinesis-channel-s3tablesdestinationconfiguration-deadletterqueues3configuration"></a>
The dead-letter queue configuration for records that cannot be delivered. Required for streaming table destinations.
*Required*: Yes
*Type*: [DeadLetterQueueS3Configuration](aws-properties-kinesis-channel-deadletterqueues3configuration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3TablesConfigurationList`  <a name="cfn-kinesis-channel-s3tablesdestinationconfiguration-s3tablesconfigurationlist"></a>
The list of streaming table configurations. Currently, one table is supported per channel.
*Required*: Yes
*Type*: Array of [S3TableConfiguration](aws-properties-kinesis-channel-s3tableconfiguration.md)
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
