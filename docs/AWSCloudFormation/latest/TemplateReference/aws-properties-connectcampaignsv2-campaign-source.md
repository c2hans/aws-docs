---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign Source
<a name="aws-properties-connectcampaignsv2-campaign-source"></a>

Contains source configuration.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-source-syntax.json"></a>

```
{
  "[CustomerProfilesSegmentArn](#cfn-connectcampaignsv2-campaign-source-customerprofilessegmentarn)" : {{String}},
  "[EventTrigger](#cfn-connectcampaignsv2-campaign-source-eventtrigger)" : {{EventTrigger}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-source-syntax.yaml"></a>

```
  [CustomerProfilesSegmentArn](#cfn-connectcampaignsv2-campaign-source-customerprofilessegmentarn): {{String}}
  [EventTrigger](#cfn-connectcampaignsv2-campaign-source-eventtrigger): {{
    EventTrigger}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-source-properties"></a>

`CustomerProfilesSegmentArn`  <a name="cfn-connectcampaignsv2-campaign-source-customerprofilessegmentarn"></a>
The Amazon Resource Name (ARN) of the Customer Profiles segment.
*Required*: No
*Type*: String
*Pattern*: `^arn:.*$`
*Minimum*: `20`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventTrigger`  <a name="cfn-connectcampaignsv2-campaign-source-eventtrigger"></a>
The event trigger of the campaign.
*Required*: No
*Type*: [EventTrigger](aws-properties-connectcampaignsv2-campaign-eventtrigger.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
