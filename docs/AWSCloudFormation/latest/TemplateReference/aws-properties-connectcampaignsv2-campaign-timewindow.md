---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-timewindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign TimeWindow
<a name="aws-properties-connectcampaignsv2-campaign-timewindow"></a>

Contains information about a time window.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-timewindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-timewindow-syntax.json"></a>

```
{
  "[OpenHours](#cfn-connectcampaignsv2-campaign-timewindow-openhours)" : {{OpenHours}},
  "[RestrictedPeriods](#cfn-connectcampaignsv2-campaign-timewindow-restrictedperiods)" : {{RestrictedPeriods}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-timewindow-syntax.yaml"></a>

```
  [OpenHours](#cfn-connectcampaignsv2-campaign-timewindow-openhours): {{
    OpenHours}}
  [RestrictedPeriods](#cfn-connectcampaignsv2-campaign-timewindow-restrictedperiods): {{
    RestrictedPeriods}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-timewindow-properties"></a>

`OpenHours`  <a name="cfn-connectcampaignsv2-campaign-timewindow-openhours"></a>
The open hours configuration.
*Required*: Yes
*Type*: [OpenHours](aws-properties-connectcampaignsv2-campaign-openhours.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictedPeriods`  <a name="cfn-connectcampaignsv2-campaign-timewindow-restrictedperiods"></a>
The restricted periods configuration.
*Required*: No
*Type*: [RestrictedPeriods](aws-properties-connectcampaignsv2-campaign-restrictedperiods.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
