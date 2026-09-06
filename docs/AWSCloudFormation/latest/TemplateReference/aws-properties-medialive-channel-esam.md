---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-esam.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel Esam
<a name="aws-properties-medialive-channel-esam"></a>

Settings for the ESAM (Event Signaling and Management) integration.

The parent of this entity is AvailSettings.

## Syntax
<a name="aws-properties-medialive-channel-esam-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-esam-syntax.json"></a>

```
{
  "[AcquisitionPointId](#cfn-medialive-channel-esam-acquisitionpointid)" : {{String}},
  "[AdAvailOffset](#cfn-medialive-channel-esam-adavailoffset)" : {{Integer}},
  "[PasswordParam](#cfn-medialive-channel-esam-passwordparam)" : {{String}},
  "[PoisEndpoint](#cfn-medialive-channel-esam-poisendpoint)" : {{String}},
  "[Username](#cfn-medialive-channel-esam-username)" : {{String}},
  "[ZoneIdentity](#cfn-medialive-channel-esam-zoneidentity)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-esam-syntax.yaml"></a>

```
  [AcquisitionPointId](#cfn-medialive-channel-esam-acquisitionpointid): {{String}}
  [AdAvailOffset](#cfn-medialive-channel-esam-adavailoffset): {{Integer}}
  [PasswordParam](#cfn-medialive-channel-esam-passwordparam): {{String}}
  [PoisEndpoint](#cfn-medialive-channel-esam-poisendpoint): {{String}}
  [Username](#cfn-medialive-channel-esam-username): {{String}}
  [ZoneIdentity](#cfn-medialive-channel-esam-zoneidentity): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-esam-properties"></a>

`AcquisitionPointId`  <a name="cfn-medialive-channel-esam-acquisitionpointid"></a>
Sent as acquisitionPointIdentity to identify the MediaLive channel to the POIS.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdAvailOffset`  <a name="cfn-medialive-channel-esam-adavailoffset"></a>
When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PasswordParam`  <a name="cfn-medialive-channel-esam-passwordparam"></a>
The password parameter for authenticating with the POIS endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PoisEndpoint`  <a name="cfn-medialive-channel-esam-poisendpoint"></a>
The URL of the signal conditioner endpoint on the Placement Opportunity Information System (POIS). MediaLive sends SignalProcessingEvents here when SCTE-35 messages are read.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Username`  <a name="cfn-medialive-channel-esam-username"></a>
The username for authenticating with the POIS endpoint.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ZoneIdentity`  <a name="cfn-medialive-channel-esam-zoneidentity"></a>
Optional data sent as zoneIdentity to identify the MediaLive channel to the POIS.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
