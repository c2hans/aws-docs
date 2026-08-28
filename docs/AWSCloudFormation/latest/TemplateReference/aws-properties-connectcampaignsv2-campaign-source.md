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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
