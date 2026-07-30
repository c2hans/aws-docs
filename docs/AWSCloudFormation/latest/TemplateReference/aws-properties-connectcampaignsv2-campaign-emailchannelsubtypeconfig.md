---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign EmailChannelSubtypeConfig
<a name="aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig"></a>

The configuration for the email channel subtype.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig-syntax.json"></a>

```
{
  "[Capacity](#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-capacity)" : {{Number}},
  "[DefaultOutboundConfig](#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-defaultoutboundconfig)" : {{EmailOutboundConfig}},
  "[OutboundMode](#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-outboundmode)" : {{EmailOutboundMode}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig-syntax.yaml"></a>

```
  [Capacity](#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-capacity): {{Number}}
  [DefaultOutboundConfig](#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-defaultoutboundconfig): {{
    EmailOutboundConfig}}
  [OutboundMode](#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-outboundmode): {{
    EmailOutboundMode}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig-properties"></a>

`Capacity`  <a name="cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-capacity"></a>
The allocation of email capacity between multiple running outbound campaigns.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOutboundConfig`  <a name="cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-defaultoutboundconfig"></a>
The default email outbound configuration of an outbound campaign.
*Required*: Yes
*Type*: [EmailOutboundConfig](aws-properties-connectcampaignsv2-campaign-emailoutboundconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutboundMode`  <a name="cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-outboundmode"></a>
The outbound mode for email of an outbound campaign.
*Required*: Yes
*Type*: [EmailOutboundMode](aws-properties-connectcampaignsv2-campaign-emailoutboundmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
