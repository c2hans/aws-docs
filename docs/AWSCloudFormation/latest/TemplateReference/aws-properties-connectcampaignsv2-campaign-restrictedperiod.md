---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-restrictedperiod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign RestrictedPeriod
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiod"></a>

Contains information about a restricted period.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiod-syntax.json"></a>

```
{
  "[EndDate](#cfn-connectcampaignsv2-campaign-restrictedperiod-enddate)" : {{String}},
  "[Name](#cfn-connectcampaignsv2-campaign-restrictedperiod-name)" : {{String}},
  "[StartDate](#cfn-connectcampaignsv2-campaign-restrictedperiod-startdate)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiod-syntax.yaml"></a>

```
  [EndDate](#cfn-connectcampaignsv2-campaign-restrictedperiod-enddate): {{String}}
  [Name](#cfn-connectcampaignsv2-campaign-restrictedperiod-name): {{String}}
  [StartDate](#cfn-connectcampaignsv2-campaign-restrictedperiod-startdate): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-restrictedperiod-properties"></a>

`EndDate`  <a name="cfn-connectcampaignsv2-campaign-restrictedperiod-enddate"></a>
The end date of the restricted period.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connectcampaignsv2-campaign-restrictedperiod-name"></a>
The name of the restricted period.
*Required*: No
*Type*: String
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartDate`  <a name="cfn-connectcampaignsv2-campaign-restrictedperiod-startdate"></a>
The start date of the restricted period.
*Required*: Yes
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
