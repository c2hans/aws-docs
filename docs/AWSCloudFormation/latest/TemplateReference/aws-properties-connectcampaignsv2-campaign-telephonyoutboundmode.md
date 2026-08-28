---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign TelephonyOutboundMode
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode"></a>

Contains information about telephony outbound mode.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode-syntax.json"></a>

```
{
  "[AgentlessConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-agentlessconfig)" : {{Json}},
  "[PredictiveConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-predictiveconfig)" : {{PredictiveConfig}},
  "[PreviewConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-previewconfig)" : {{PreviewConfig}},
  "[ProgressiveConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-progressiveconfig)" : {{ProgressiveConfig}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode-syntax.yaml"></a>

```
  [AgentlessConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-agentlessconfig): {{Json}}
  [PredictiveConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-predictiveconfig): {{
    PredictiveConfig}}
  [PreviewConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-previewconfig): {{
    PreviewConfig}}
  [ProgressiveConfig](#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-progressiveconfig): {{
    ProgressiveConfig}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode-properties"></a>

`AgentlessConfig`  <a name="cfn-connectcampaignsv2-campaign-telephonyoutboundmode-agentlessconfig"></a>
The agentless outbound mode configuration for telephony.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PredictiveConfig`  <a name="cfn-connectcampaignsv2-campaign-telephonyoutboundmode-predictiveconfig"></a>
Contains predictive outbound mode configuration.
*Required*: No
*Type*: [PredictiveConfig](aws-properties-connectcampaignsv2-campaign-predictiveconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreviewConfig`  <a name="cfn-connectcampaignsv2-campaign-telephonyoutboundmode-previewconfig"></a>
Contains preview outbound mode configuration.
*Required*: No
*Type*: [PreviewConfig](aws-properties-connectcampaignsv2-campaign-previewconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgressiveConfig`  <a name="cfn-connectcampaignsv2-campaign-telephonyoutboundmode-progressiveconfig"></a>
Contains progressive telephony outbound mode configuration.
*Required*: No
*Type*: [ProgressiveConfig](aws-properties-connectcampaignsv2-campaign-progressiveconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
