---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaigns-campaign-agentlessdialerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaigns::Campaign AgentlessDialerConfig
<a name="aws-properties-connectcampaigns-campaign-agentlessdialerconfig"></a>

Contains agentless dialer configuration for an outbound campaign.

## Syntax
<a name="aws-properties-connectcampaigns-campaign-agentlessdialerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaigns-campaign-agentlessdialerconfig-syntax.json"></a>

```
{
  "[DialingCapacity](#cfn-connectcampaigns-campaign-agentlessdialerconfig-dialingcapacity)" : {{Number}}
}
```

### YAML
<a name="aws-properties-connectcampaigns-campaign-agentlessdialerconfig-syntax.yaml"></a>

```
  [DialingCapacity](#cfn-connectcampaigns-campaign-agentlessdialerconfig-dialingcapacity): {{Number}}
```

## Properties
<a name="aws-properties-connectcampaigns-campaign-agentlessdialerconfig-properties"></a>

`DialingCapacity`  <a name="cfn-connectcampaigns-campaign-agentlessdialerconfig-dialingcapacity"></a>
The allocation of dialing capacity between multiple active campaigns.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
