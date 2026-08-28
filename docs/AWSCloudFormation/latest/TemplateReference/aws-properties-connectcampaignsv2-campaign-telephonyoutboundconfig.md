---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign TelephonyOutboundConfig
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig"></a>

The outbound configuration for telephony.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig-syntax.json"></a>

```
{
  "[AnswerMachineDetectionConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-answermachinedetectionconfig)" : {{AnswerMachineDetectionConfig}},
  "[ConnectContactFlowId](#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-connectcontactflowid)" : {{String}},
  "[ConnectSourcePhoneNumber](#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-connectsourcephonenumber)" : {{String}},
  "[RingTimeout](#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-ringtimeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig-syntax.yaml"></a>

```
  [AnswerMachineDetectionConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-answermachinedetectionconfig): {{
    AnswerMachineDetectionConfig}}
  [ConnectContactFlowId](#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-connectcontactflowid): {{String}}
  [ConnectSourcePhoneNumber](#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-connectsourcephonenumber): {{String}}
  [RingTimeout](#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-ringtimeout): {{Integer}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig-properties"></a>

`AnswerMachineDetectionConfig`  <a name="cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-answermachinedetectionconfig"></a>
The answering machine detection configuration.
*Required*: No
*Type*: [AnswerMachineDetectionConfig](aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectContactFlowId`  <a name="cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-connectcontactflowid"></a>
The identifier of the published Amazon Connect contact flow.
*Required*: Yes
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectSourcePhoneNumber`  <a name="cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-connectsourcephonenumber"></a>
The Amazon Connect source phone number.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RingTimeout`  <a name="cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-ringtimeout"></a>
The ring timeout configuration for outbound calls. Specifies how long to wait for the call to be answered before timing out.
*Required*: No
*Type*: Integer
*Minimum*: `15`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
