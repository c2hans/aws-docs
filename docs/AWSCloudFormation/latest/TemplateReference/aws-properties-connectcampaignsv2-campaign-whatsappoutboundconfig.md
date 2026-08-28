---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-whatsappoutboundconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign WhatsAppOutboundConfig
<a name="aws-properties-connectcampaignsv2-campaign-whatsappoutboundconfig"></a>

The outbound configuration for WhatsApp.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-whatsappoutboundconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-whatsappoutboundconfig-syntax.json"></a>

```
{
  "[ConnectSourcePhoneNumberArn](#cfn-connectcampaignsv2-campaign-whatsappoutboundconfig-connectsourcephonenumberarn)" : {{String}},
  "[WisdomTemplateArn](#cfn-connectcampaignsv2-campaign-whatsappoutboundconfig-wisdomtemplatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-whatsappoutboundconfig-syntax.yaml"></a>

```
  [ConnectSourcePhoneNumberArn](#cfn-connectcampaignsv2-campaign-whatsappoutboundconfig-connectsourcephonenumberarn): {{String}}
  [WisdomTemplateArn](#cfn-connectcampaignsv2-campaign-whatsappoutboundconfig-wisdomtemplatearn): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-whatsappoutboundconfig-properties"></a>

`ConnectSourcePhoneNumberArn`  <a name="cfn-connectcampaignsv2-campaign-whatsappoutboundconfig-connectsourcephonenumberarn"></a>
The Amazon Resource Name (ARN) of the Connect Customer source WhatsApp phone number.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `20`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WisdomTemplateArn`  <a name="cfn-connectcampaignsv2-campaign-whatsappoutboundconfig-wisdomtemplatearn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect template.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `20`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
