---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign ChannelSubtypeConfig
<a name="aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig"></a>

Contains channel subtype configuration for an outbound campaign.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig-syntax.json"></a>

```
{
  "[Email](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-email)" : {{EmailChannelSubtypeConfig}},
  "[Sms](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-sms)" : {{SmsChannelSubtypeConfig}},
  "[Telephony](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-telephony)" : {{TelephonyChannelSubtypeConfig}},
  "[WhatsApp](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-whatsapp)" : {{WhatsAppChannelSubtypeConfig}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig-syntax.yaml"></a>

```
  [Email](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-email): {{
    EmailChannelSubtypeConfig}}
  [Sms](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-sms): {{
    SmsChannelSubtypeConfig}}
  [Telephony](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-telephony): {{
    TelephonyChannelSubtypeConfig}}
  [WhatsApp](#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-whatsapp): {{
    WhatsAppChannelSubtypeConfig}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig-properties"></a>

`Email`  <a name="cfn-connectcampaignsv2-campaign-channelsubtypeconfig-email"></a>
The configuration of the email channel subtype.
*Required*: No
*Type*: [EmailChannelSubtypeConfig](aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sms`  <a name="cfn-connectcampaignsv2-campaign-channelsubtypeconfig-sms"></a>
The configuration of the SMS channel subtype.
*Required*: No
*Type*: [SmsChannelSubtypeConfig](aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Telephony`  <a name="cfn-connectcampaignsv2-campaign-channelsubtypeconfig-telephony"></a>
The configuration of the telephony channel subtype.
*Required*: No
*Type*: [TelephonyChannelSubtypeConfig](aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WhatsApp`  <a name="cfn-connectcampaignsv2-campaign-channelsubtypeconfig-whatsapp"></a>
The configuration of the WhatsApp channel subtype.
*Required*: No
*Type*: [WhatsAppChannelSubtypeConfig](aws-properties-connectcampaignsv2-campaign-whatsappchannelsubtypeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
