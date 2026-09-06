---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-progressiveconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign ProgressiveConfig
<a name="aws-properties-connectcampaignsv2-campaign-progressiveconfig"></a>

Contains the progressive outbound mode configuration.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-progressiveconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-progressiveconfig-syntax.json"></a>

```
{
  "[BandwidthAllocation](#cfn-connectcampaignsv2-campaign-progressiveconfig-bandwidthallocation)" : {{Number}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-progressiveconfig-syntax.yaml"></a>

```
  [BandwidthAllocation](#cfn-connectcampaignsv2-campaign-progressiveconfig-bandwidthallocation): {{Number}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-progressiveconfig-properties"></a>

`BandwidthAllocation`  <a name="cfn-connectcampaignsv2-campaign-progressiveconfig-bandwidthallocation"></a>
Bandwidth allocation for the progressive outbound mode.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
