---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-predictiveconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign PredictiveConfig
<a name="aws-properties-connectcampaignsv2-campaign-predictiveconfig"></a>

Contains predictive outbound mode configuration.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-predictiveconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-predictiveconfig-syntax.json"></a>

```
{
  "[BandwidthAllocation](#cfn-connectcampaignsv2-campaign-predictiveconfig-bandwidthallocation)" : {{Number}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-predictiveconfig-syntax.yaml"></a>

```
  [BandwidthAllocation](#cfn-connectcampaignsv2-campaign-predictiveconfig-bandwidthallocation): {{Number}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-predictiveconfig-properties"></a>

`BandwidthAllocation`  <a name="cfn-connectcampaignsv2-campaign-predictiveconfig-bandwidthallocation"></a>
Bandwidth allocation for the predictive outbound mode.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
