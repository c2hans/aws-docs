---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign WhatsAppChannelSubtypeConfig
<a name="aws-properties-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig"></a>

The configuration for the WhatsApp channel subtype.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-syntax.json"></a>

```
{
  "[Capacity](#cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-capacity)" : {{Number}},
  "[DefaultOutboundConfig](#cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-defaultoutboundconfig)" : {{WhatsAppOutboundConfig}},
  "[OutboundMode](#cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-outboundmode)" : {{WhatsAppOutboundMode}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-syntax.yaml"></a>

```
  [Capacity](#cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-capacity): {{Number}}
  [DefaultOutboundConfig](#cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-defaultoutboundconfig): {{
    WhatsAppOutboundConfig}}
  [OutboundMode](#cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-outboundmode): {{
    WhatsAppOutboundMode}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-properties"></a>

`Capacity`  <a name="cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-capacity"></a>
The allocation of WhatsApp capacity between multiple running outbound campaigns.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOutboundConfig`  <a name="cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-defaultoutboundconfig"></a>
The default WhatsApp outbound configuration of an outbound campaign.
*Required*: Yes
*Type*: [WhatsAppOutboundConfig](aws-properties-connectcampaignsv2-campaign-whatsappoutboundconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutboundMode`  <a name="cfn-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig-outboundmode"></a>
The outbound mode for WhatsApp of an outbound campaign.
*Required*: Yes
*Type*: [WhatsAppOutboundMode](aws-properties-connectcampaignsv2-campaign-whatsappoutboundmode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
