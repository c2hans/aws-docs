---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-emailoutboundconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign EmailOutboundConfig
<a name="aws-properties-connectcampaignsv2-campaign-emailoutboundconfig"></a>

The outbound configuration for email.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-emailoutboundconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-emailoutboundconfig-syntax.json"></a>

```
{
  "[ConnectSourceEmailAddress](#cfn-connectcampaignsv2-campaign-emailoutboundconfig-connectsourceemailaddress)" : {{String}},
  "[SourceEmailAddressDisplayName](#cfn-connectcampaignsv2-campaign-emailoutboundconfig-sourceemailaddressdisplayname)" : {{String}},
  "[WisdomTemplateArn](#cfn-connectcampaignsv2-campaign-emailoutboundconfig-wisdomtemplatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-emailoutboundconfig-syntax.yaml"></a>

```
  [ConnectSourceEmailAddress](#cfn-connectcampaignsv2-campaign-emailoutboundconfig-connectsourceemailaddress): {{String}}
  [SourceEmailAddressDisplayName](#cfn-connectcampaignsv2-campaign-emailoutboundconfig-sourceemailaddressdisplayname): {{String}}
  [WisdomTemplateArn](#cfn-connectcampaignsv2-campaign-emailoutboundconfig-wisdomtemplatearn): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-emailoutboundconfig-properties"></a>

`ConnectSourceEmailAddress`  <a name="cfn-connectcampaignsv2-campaign-emailoutboundconfig-connectsourceemailaddress"></a>
The Amazon Connect source email address.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w-\.\+]+@([\w-]+\.)+[\w-]{2,4}$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceEmailAddressDisplayName`  <a name="cfn-connectcampaignsv2-campaign-emailoutboundconfig-sourceemailaddressdisplayname"></a>
The display name for the Amazon Connect source email address.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WisdomTemplateArn`  <a name="cfn-connectcampaignsv2-campaign-emailoutboundconfig-wisdomtemplatearn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect template.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `20`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
