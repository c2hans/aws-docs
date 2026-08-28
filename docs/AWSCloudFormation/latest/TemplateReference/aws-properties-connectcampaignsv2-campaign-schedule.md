---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-schedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign Schedule
<a name="aws-properties-connectcampaignsv2-campaign-schedule"></a>

Contains the schedule configuration.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-schedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-schedule-syntax.json"></a>

```
{
  "[EndTime](#cfn-connectcampaignsv2-campaign-schedule-endtime)" : {{String}},
  "[RefreshFrequency](#cfn-connectcampaignsv2-campaign-schedule-refreshfrequency)" : {{String}},
  "[StartTime](#cfn-connectcampaignsv2-campaign-schedule-starttime)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-schedule-syntax.yaml"></a>

```
  [EndTime](#cfn-connectcampaignsv2-campaign-schedule-endtime): {{String}}
  [RefreshFrequency](#cfn-connectcampaignsv2-campaign-schedule-refreshfrequency): {{String}}
  [StartTime](#cfn-connectcampaignsv2-campaign-schedule-starttime): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-schedule-properties"></a>

`EndTime`  <a name="cfn-connectcampaignsv2-campaign-schedule-endtime"></a>
The end time of the schedule in UTC.
*Required*: Yes
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RefreshFrequency`  <a name="cfn-connectcampaignsv2-campaign-schedule-refreshfrequency"></a>
The refresh frequency of the campaign.
*Required*: No
*Type*: String
*Pattern*: `^P(?:([-+]?[0-9]+)D)?(T(?:([-+]?[0-9]+)H)?(?:([-+]?[0-9]+)M)?(?:([-+]?[0-9]+)(?:[.,]([0-9]{0,9}))?S)?)?$`
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTime`  <a name="cfn-connectcampaignsv2-campaign-schedule-starttime"></a>
The start time of the schedule in UTC.
*Required*: Yes
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
