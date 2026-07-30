---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-communicationlimits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign CommunicationLimits
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimits"></a>

Contains information about communication limits.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimits-syntax.json"></a>

```
{
  "[CommunicationLimitList](#cfn-connectcampaignsv2-campaign-communicationlimits-communicationlimitlist)" : {{[ CommunicationLimit, ... ]}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimits-syntax.yaml"></a>

```
  [CommunicationLimitList](#cfn-connectcampaignsv2-campaign-communicationlimits-communicationlimitlist): {{
    - CommunicationLimit}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-communicationlimits-properties"></a>

`CommunicationLimitList`  <a name="cfn-connectcampaignsv2-campaign-communicationlimits-communicationlimitlist"></a>
The list of CommunicationLimits.
*Required*: No
*Type*: Array of [CommunicationLimit](aws-properties-connectcampaignsv2-campaign-communicationlimit.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
