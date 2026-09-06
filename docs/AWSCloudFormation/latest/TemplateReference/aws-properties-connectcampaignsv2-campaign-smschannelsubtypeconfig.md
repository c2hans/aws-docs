---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign SmsChannelSubtypeConfig
<a name="aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig"></a>

The configuration for the SMS channel subtype.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig-syntax.json"></a>

```
{
  "[Capacity](#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-capacity)" : {{Number}},
  "[DefaultOutboundConfig](#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-defaultoutboundconfig)" : {{SmsOutboundConfig}},
  "[OutboundMode](#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-outboundmode)" : {{SmsOutboundMode}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig-syntax.yaml"></a>

```
  [Capacity](#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-capacity): {{Number}}
  [DefaultOutboundConfig](#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-defaultoutboundconfig): {{
    SmsOutboundConfig}}
  [OutboundMode](#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-outboundmode): {{
    SmsOutboundMode}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig-properties"></a>

`Capacity`  <a name="cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-capacity"></a>
The allocation of SMS capacity between multiple running outbound campaigns.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOutboundConfig`  <a name="cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-defaultoutboundconfig"></a>
The default SMS outbound configuration of an outbound campaign.
*Required*: Yes
*Type*: [SmsOutboundConfig](aws-properties-connectcampaignsv2-campaign-smsoutboundconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutboundMode`  <a name="cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-outboundmode"></a>
The outbound mode of SMS for an outbound campaign.
*Required*: Yes
*Type*: [SmsOutboundMode](aws-properties-connectcampaignsv2-campaign-smsoutboundmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
