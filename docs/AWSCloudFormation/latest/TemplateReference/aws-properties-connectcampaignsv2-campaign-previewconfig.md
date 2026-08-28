---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-previewconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign PreviewConfig
<a name="aws-properties-connectcampaignsv2-campaign-previewconfig"></a>

Contains preview outbound mode configuration.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-previewconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-previewconfig-syntax.json"></a>

```
{
  "[AgentActions](#cfn-connectcampaignsv2-campaign-previewconfig-agentactions)" : {{[ String, ... ]}},
  "[BandwidthAllocation](#cfn-connectcampaignsv2-campaign-previewconfig-bandwidthallocation)" : {{Number}},
  "[TimeoutConfig](#cfn-connectcampaignsv2-campaign-previewconfig-timeoutconfig)" : {{TimeoutConfig}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-previewconfig-syntax.yaml"></a>

```
  [AgentActions](#cfn-connectcampaignsv2-campaign-previewconfig-agentactions): {{
    - String}}
  [BandwidthAllocation](#cfn-connectcampaignsv2-campaign-previewconfig-bandwidthallocation): {{Number}}
  [TimeoutConfig](#cfn-connectcampaignsv2-campaign-previewconfig-timeoutconfig): {{
    TimeoutConfig}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-previewconfig-properties"></a>

`AgentActions`  <a name="cfn-connectcampaignsv2-campaign-previewconfig-agentactions"></a>
Agent actions for the preview outbound mode.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BandwidthAllocation`  <a name="cfn-connectcampaignsv2-campaign-previewconfig-bandwidthallocation"></a>
Bandwidth allocation for the preview outbound mode.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutConfig`  <a name="cfn-connectcampaignsv2-campaign-previewconfig-timeoutconfig"></a>
Countdown timer configuration for preview outbound mode.
*Required*: Yes
*Type*: [TimeoutConfig](aws-properties-connectcampaignsv2-campaign-timeoutconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
