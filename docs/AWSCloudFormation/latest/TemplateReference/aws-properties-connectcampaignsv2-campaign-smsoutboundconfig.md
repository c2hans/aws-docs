---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-smsoutboundconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign SmsOutboundConfig
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundconfig"></a>

The outbound configuration for SMS.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundconfig-syntax.json"></a>

```
{
  "[ConnectSourcePhoneNumberArn](#cfn-connectcampaignsv2-campaign-smsoutboundconfig-connectsourcephonenumberarn)" : {{String}},
  "[WisdomTemplateArn](#cfn-connectcampaignsv2-campaign-smsoutboundconfig-wisdomtemplatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundconfig-syntax.yaml"></a>

```
  [ConnectSourcePhoneNumberArn](#cfn-connectcampaignsv2-campaign-smsoutboundconfig-connectsourcephonenumberarn): {{String}}
  [WisdomTemplateArn](#cfn-connectcampaignsv2-campaign-smsoutboundconfig-wisdomtemplatearn): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundconfig-properties"></a>

`ConnectSourcePhoneNumberArn`  <a name="cfn-connectcampaignsv2-campaign-smsoutboundconfig-connectsourcephonenumberarn"></a>
The Amazon Resource Name (ARN) of the Amazon Connect source SMS phone number.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `20`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WisdomTemplateArn`  <a name="cfn-connectcampaignsv2-campaign-smsoutboundconfig-wisdomtemplatearn"></a>
The Amazon Resource Name (ARN) of the Amazon Q in Connect template.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `20`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
