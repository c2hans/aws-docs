---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign TelephonyChannelSubtypeConfig
<a name="aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig"></a>

The configuration for the telephony channel subtype.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-syntax.json"></a>

```
{
  "[Capacity](#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-capacity)" : {{Number}},
  "[ConnectQueueId](#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-connectqueueid)" : {{String}},
  "[DefaultOutboundConfig](#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-defaultoutboundconfig)" : {{TelephonyOutboundConfig}},
  "[OutboundMode](#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-outboundmode)" : {{TelephonyOutboundMode}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-syntax.yaml"></a>

```
  [Capacity](#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-capacity): {{Number}}
  [ConnectQueueId](#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-connectqueueid): {{String}}
  [DefaultOutboundConfig](#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-defaultoutboundconfig): {{
    TelephonyOutboundConfig}}
  [OutboundMode](#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-outboundmode): {{
    TelephonyOutboundMode}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-properties"></a>

`Capacity`  <a name="cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-capacity"></a>
The allocation of telephony capacity between multiple running outbound campaigns.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectQueueId`  <a name="cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-connectqueueid"></a>
The identifier of the Amazon Connect queue associated with telephony outbound requests of an outbound campaign.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOutboundConfig`  <a name="cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-defaultoutboundconfig"></a>
The default telephony outbound configuration of an outbound campaign.
*Required*: Yes
*Type*: [TelephonyOutboundConfig](aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutboundMode`  <a name="cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-outboundmode"></a>
The outbound mode of telephony for an outbound campaign.
*Required*: Yes
*Type*: [TelephonyOutboundMode](aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
