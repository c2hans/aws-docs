---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaigns-campaign-dialerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaigns::Campaign DialerConfig
<a name="aws-properties-connectcampaigns-campaign-dialerconfig"></a>

Contains dialer configuration for an outbound campaign.

## Syntax
<a name="aws-properties-connectcampaigns-campaign-dialerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaigns-campaign-dialerconfig-syntax.json"></a>

```
{
  "[AgentlessDialerConfig](#cfn-connectcampaigns-campaign-dialerconfig-agentlessdialerconfig)" : {{AgentlessDialerConfig}},
  "[PredictiveDialerConfig](#cfn-connectcampaigns-campaign-dialerconfig-predictivedialerconfig)" : {{PredictiveDialerConfig}},
  "[ProgressiveDialerConfig](#cfn-connectcampaigns-campaign-dialerconfig-progressivedialerconfig)" : {{ProgressiveDialerConfig}}
}
```

### YAML
<a name="aws-properties-connectcampaigns-campaign-dialerconfig-syntax.yaml"></a>

```
  [AgentlessDialerConfig](#cfn-connectcampaigns-campaign-dialerconfig-agentlessdialerconfig): {{
    AgentlessDialerConfig}}
  [PredictiveDialerConfig](#cfn-connectcampaigns-campaign-dialerconfig-predictivedialerconfig): {{
    PredictiveDialerConfig}}
  [ProgressiveDialerConfig](#cfn-connectcampaigns-campaign-dialerconfig-progressivedialerconfig): {{
    ProgressiveDialerConfig}}
```

## Properties
<a name="aws-properties-connectcampaigns-campaign-dialerconfig-properties"></a>

`AgentlessDialerConfig`  <a name="cfn-connectcampaigns-campaign-dialerconfig-agentlessdialerconfig"></a>
The configuration of the agentless dialer.
*Required*: No
*Type*: [AgentlessDialerConfig](aws-properties-connectcampaigns-campaign-agentlessdialerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PredictiveDialerConfig`  <a name="cfn-connectcampaigns-campaign-dialerconfig-predictivedialerconfig"></a>
The configuration of the predictive dialer.
*Required*: No
*Type*: [PredictiveDialerConfig](aws-properties-connectcampaigns-campaign-predictivedialerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgressiveDialerConfig`  <a name="cfn-connectcampaigns-campaign-dialerconfig-progressivedialerconfig"></a>
The configuration of the progressive dialer.
*Required*: No
*Type*: [ProgressiveDialerConfig](aws-properties-connectcampaigns-campaign-progressivedialerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
