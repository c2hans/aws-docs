---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream HttpEndpointConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration"></a>

Describes the configuration of the HTTP endpoint to which Kinesis Firehose delivers data. Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration-syntax.json"></a>

```
{
  "[AccessKey](#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey)" : {{String}},
  "[Name](#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name)" : {{String}},
  "[Url](#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration-syntax.yaml"></a>

```
  [AccessKey](#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey): {{String}}
  [Name](#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name): {{String}}
  [Url](#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration-properties"></a>

`AccessKey`  <a name="cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey"></a>
The access key required for Kinesis Firehose to authenticate with the HTTP endpoint selected as the destination.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name"></a>
The name of the HTTP endpoint selected as the destination.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url"></a>
The URL of the HTTP endpoint selected as the destination.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
