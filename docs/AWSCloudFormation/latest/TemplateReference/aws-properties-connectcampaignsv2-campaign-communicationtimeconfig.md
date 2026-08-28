---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-communicationtimeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign CommunicationTimeConfig
<a name="aws-properties-connectcampaignsv2-campaign-communicationtimeconfig"></a>

Communication time configuration for an outbound campaign.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-communicationtimeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-communicationtimeconfig-syntax.json"></a>

```
{
  "[Email](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-email)" : {{TimeWindow}},
  "[LocalTimeZoneConfig](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-localtimezoneconfig)" : {{LocalTimeZoneConfig}},
  "[Sms](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-sms)" : {{TimeWindow}},
  "[Telephony](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-telephony)" : {{TimeWindow}},
  "[WhatsApp](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-whatsapp)" : {{TimeWindow}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-communicationtimeconfig-syntax.yaml"></a>

```
  [Email](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-email): {{
    TimeWindow}}
  [LocalTimeZoneConfig](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-localtimezoneconfig): {{
    LocalTimeZoneConfig}}
  [Sms](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-sms): {{
    TimeWindow}}
  [Telephony](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-telephony): {{
    TimeWindow}}
  [WhatsApp](#cfn-connectcampaignsv2-campaign-communicationtimeconfig-whatsapp): {{
    TimeWindow}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-communicationtimeconfig-properties"></a>

`Email`  <a name="cfn-connectcampaignsv2-campaign-communicationtimeconfig-email"></a>
The communication time configuration for the email channel subtype.
*Required*: No
*Type*: [TimeWindow](aws-properties-connectcampaignsv2-campaign-timewindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalTimeZoneConfig`  <a name="cfn-connectcampaignsv2-campaign-communicationtimeconfig-localtimezoneconfig"></a>
The local timezone configuration.
*Required*: Yes
*Type*: [LocalTimeZoneConfig](aws-properties-connectcampaignsv2-campaign-localtimezoneconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sms`  <a name="cfn-connectcampaignsv2-campaign-communicationtimeconfig-sms"></a>
The communication time configuration for the SMS channel subtype.
*Required*: No
*Type*: [TimeWindow](aws-properties-connectcampaignsv2-campaign-timewindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Telephony`  <a name="cfn-connectcampaignsv2-campaign-communicationtimeconfig-telephony"></a>
The communication time configuration for the telephony channel subtype.
*Required*: No
*Type*: [TimeWindow](aws-properties-connectcampaignsv2-campaign-timewindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WhatsApp`  <a name="cfn-connectcampaignsv2-campaign-communicationtimeconfig-whatsapp"></a>
The communication time configuration for the WhatsApp channel subtype.
*Required*: No
*Type*: [TimeWindow](aws-properties-connectcampaignsv2-campaign-timewindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
