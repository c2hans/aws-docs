---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaigns-campaign-progressivedialerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaigns::Campaign ProgressiveDialerConfig
<a name="aws-properties-connectcampaigns-campaign-progressivedialerconfig"></a>

Contains progressive dialer configuration for an outbound campaign.

## Syntax
<a name="aws-properties-connectcampaigns-campaign-progressivedialerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaigns-campaign-progressivedialerconfig-syntax.json"></a>

```
{
  "[BandwidthAllocation](#cfn-connectcampaigns-campaign-progressivedialerconfig-bandwidthallocation)" : {{Number}},
  "[DialingCapacity](#cfn-connectcampaigns-campaign-progressivedialerconfig-dialingcapacity)" : {{Number}}
}
```

### YAML
<a name="aws-properties-connectcampaigns-campaign-progressivedialerconfig-syntax.yaml"></a>

```
  [BandwidthAllocation](#cfn-connectcampaigns-campaign-progressivedialerconfig-bandwidthallocation): {{Number}}
  [DialingCapacity](#cfn-connectcampaigns-campaign-progressivedialerconfig-dialingcapacity): {{Number}}
```

## Properties
<a name="aws-properties-connectcampaigns-campaign-progressivedialerconfig-properties"></a>

`BandwidthAllocation`  <a name="cfn-connectcampaigns-campaign-progressivedialerconfig-bandwidthallocation"></a>
Bandwidth allocation for the progressive dialer.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DialingCapacity`  <a name="cfn-connectcampaigns-campaign-progressivedialerconfig-dialingcapacity"></a>
The allocation of dialing capacity between multiple active campaigns.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
