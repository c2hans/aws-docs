---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-smsoutboundmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign SmsOutboundMode
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundmode"></a>

Contains information about the SMS outbound mode.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundmode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundmode-syntax.json"></a>

```
{
  "[AgentlessConfig](#cfn-connectcampaignsv2-campaign-smsoutboundmode-agentlessconfig)" : {{Json}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundmode-syntax.yaml"></a>

```
  [AgentlessConfig](#cfn-connectcampaignsv2-campaign-smsoutboundmode-agentlessconfig): {{Json}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-smsoutboundmode-properties"></a>

`AgentlessConfig`  <a name="cfn-connectcampaignsv2-campaign-smsoutboundmode-agentlessconfig"></a>
Contains agentless outbound mode configuration.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
