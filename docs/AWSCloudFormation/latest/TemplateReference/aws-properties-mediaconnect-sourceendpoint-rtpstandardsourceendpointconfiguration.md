---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint RtpStandardSourceEndpointConfiguration

The configuration settings for a source endpoint that uses the RTP protocol.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-syntax.json"></a>

```json
{
  "[DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-destinationingestport)" : {{Integer}},
  "[ForwardErrorCorrectionState](#cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-forwarderrorcorrectionstate)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-syntax.yaml"></a>

```yaml
  [DestinationIngestPort](#cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-destinationingestport): {{Integer}}
  [ForwardErrorCorrectionState](#cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-forwarderrorcorrectionstate): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-properties"></a>

`DestinationIngestPort`  <a name="cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-destinationingestport"></a>
The port on the destination that receives the content. The valid range is 3000 to 30000.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForwardErrorCorrectionState`  <a name="cfn-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration-forwarderrorcorrectionstate"></a>
Indicates whether forward error correction (FEC) is enabled for the source endpoint.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
