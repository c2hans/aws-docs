---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream RedshiftRetryOptions
<a name="aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions"></a>

Configures retry behavior in case Firehose is unable to deliver documents to Amazon Redshift.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions-syntax.json"></a>

```
{
  "[DurationInSeconds](#cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions-syntax.yaml"></a>

```
  [DurationInSeconds](#cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions-properties"></a>

`DurationInSeconds`  <a name="cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds"></a>
The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of `DurationInSeconds` is 0 (zero) or if the first delivery attempt takes longer than the current value.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `7200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
