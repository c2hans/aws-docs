---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-dailyhour.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign DailyHour
<a name="aws-properties-connectcampaignsv2-campaign-dailyhour"></a>

The daily hours configuration.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-dailyhour-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-dailyhour-syntax.json"></a>

```
{
  "[Key](#cfn-connectcampaignsv2-campaign-dailyhour-key)" : {{String}},
  "[Value](#cfn-connectcampaignsv2-campaign-dailyhour-value)" : {{[ TimeRange, ... ]}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-dailyhour-syntax.yaml"></a>

```
  [Key](#cfn-connectcampaignsv2-campaign-dailyhour-key): {{String}}
  [Value](#cfn-connectcampaignsv2-campaign-dailyhour-value): {{
    - TimeRange}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-dailyhour-properties"></a>

`Key`  <a name="cfn-connectcampaignsv2-campaign-dailyhour-key"></a>
The key for DailyHour.
*Required*: No
*Type*: String
*Allowed values*: `MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-connectcampaignsv2-campaign-dailyhour-value"></a>
The value for DailyHour.
*Required*: No
*Type*: Array of [TimeRange](aws-properties-connectcampaignsv2-campaign-timerange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
