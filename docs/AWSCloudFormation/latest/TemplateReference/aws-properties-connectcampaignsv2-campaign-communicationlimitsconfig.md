---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign CommunicationLimitsConfig
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig"></a>

Contains the communication limits configuration for an outbound campaign.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig-syntax.json"></a>

```
{
  "[AllChannelsSubtypes](#cfn-connectcampaignsv2-campaign-communicationlimitsconfig-allchannelssubtypes)" : {{CommunicationLimits}},
  "[InstanceLimitsHandling](#cfn-connectcampaignsv2-campaign-communicationlimitsconfig-instancelimitshandling)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig-syntax.yaml"></a>

```
  [AllChannelsSubtypes](#cfn-connectcampaignsv2-campaign-communicationlimitsconfig-allchannelssubtypes): {{
    CommunicationLimits}}
  [InstanceLimitsHandling](#cfn-connectcampaignsv2-campaign-communicationlimitsconfig-instancelimitshandling): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig-properties"></a>

`AllChannelsSubtypes`  <a name="cfn-connectcampaignsv2-campaign-communicationlimitsconfig-allchannelssubtypes"></a>
The CommunicationLimits that apply to all channel subtypes defined in an outbound campaign.
*Required*: No
*Type*: [CommunicationLimits](aws-properties-connectcampaignsv2-campaign-communicationlimits.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceLimitsHandling`  <a name="cfn-connectcampaignsv2-campaign-communicationlimitsconfig-instancelimitshandling"></a>
Opt-in or Opt-out from instance-level limits.
*Required*: No
*Type*: String
*Allowed values*: `OPT_IN | OPT_OUT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
