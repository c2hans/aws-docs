---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint RistStandardSourceEndpointConfiguration

The configuration settings for a source endpoint that uses the RIST protocol.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-syntax.json"></a>

```json
{
  "[DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-destinationingestport)" : {{Integer}},
  "[RecoveryLatencyMilliseconds](#cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-recoverylatencymilliseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-syntax.yaml"></a>

```yaml
  [DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-destinationingestport): {{Integer}}
  [RecoveryLatencyMilliseconds](#cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-recoverylatencymilliseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-properties"></a>

`DestinationIngestPort`  <a name="cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-destinationingestport"></a>
The port on the destination that receives the content. The valid range is 3000 to 30000.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryLatencyMilliseconds`  <a name="cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-recoverylatencymilliseconds"></a>
The amount of time, in milliseconds, that the source endpoint allows for recovering lost packets. The valid range is 10 to 10000.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
