---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-openhours.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign OpenHours
<a name="aws-properties-connectcampaignsv2-campaign-openhours"></a>

Contains information about open hours.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-openhours-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-openhours-syntax.json"></a>

```
{
  "[DailyHours](#cfn-connectcampaignsv2-campaign-openhours-dailyhours)" : {{[ DailyHour, ... ]}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-openhours-syntax.yaml"></a>

```
  [DailyHours](#cfn-connectcampaignsv2-campaign-openhours-dailyhours): {{
    - DailyHour}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-openhours-properties"></a>

`DailyHours`  <a name="cfn-connectcampaignsv2-campaign-openhours-dailyhours"></a>
The daily hours configuration.
*Required*: Yes
*Type*: Array of [DailyHour](aws-properties-connectcampaignsv2-campaign-dailyhour.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
