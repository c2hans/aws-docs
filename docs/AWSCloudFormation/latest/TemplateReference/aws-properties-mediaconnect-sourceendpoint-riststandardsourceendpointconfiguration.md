---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint RistStandardSourceEndpointConfiguration
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-description"></a>The `RistStandardSourceEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::SourceEndpoint](aws-resource-mediaconnect-sourceendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-syntax.json"></a>

```
{
  "[DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-destinationingestport)" : {{Integer}},
  "[RecoveryLatencyMilliseconds](#cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-recoverylatencymilliseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-syntax.yaml"></a>

```
  [DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-destinationingestport): {{Integer}}
  [RecoveryLatencyMilliseconds](#cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-recoverylatencymilliseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-properties"></a>

`DestinationIngestPort`  <a name="cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-destinationingestport"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryLatencyMilliseconds`  <a name="cfn-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration-recoverylatencymilliseconds"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
