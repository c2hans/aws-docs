---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-restrictedperiods.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign RestrictedPeriods
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiods"></a>

Contains information about restricted periods.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiods-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiods-syntax.json"></a>

```
{
  "[RestrictedPeriodList](#cfn-connectcampaignsv2-campaign-restrictedperiods-restrictedperiodlist)" : {{[ RestrictedPeriod, ... ]}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiods-syntax.yaml"></a>

```
  [RestrictedPeriodList](#cfn-connectcampaignsv2-campaign-restrictedperiods-restrictedperiodlist): {{
    - RestrictedPeriod}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiods-properties"></a>

`RestrictedPeriodList`  <a name="cfn-connectcampaignsv2-campaign-restrictedperiods-restrictedperiodlist"></a>
The restricted period list.
*Required*: No
*Type*: Array of [RestrictedPeriod](aws-properties-connectcampaignsv2-campaign-restrictedperiod.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
