---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-localtimezoneconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign LocalTimeZoneConfig
<a name="aws-properties-connectcampaignsv2-campaign-localtimezoneconfig"></a>

The configuration of timezone for recipient.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-localtimezoneconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-localtimezoneconfig-syntax.json"></a>

```
{
  "[DefaultTimeZone](#cfn-connectcampaignsv2-campaign-localtimezoneconfig-defaulttimezone)" : {{String}},
  "[LocalTimeZoneDetection](#cfn-connectcampaignsv2-campaign-localtimezoneconfig-localtimezonedetection)" : {{[ String, ... ]}},
  "[LocalTimeZoneDetectionScope](#cfn-connectcampaignsv2-campaign-localtimezoneconfig-localtimezonedetectionscope)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-localtimezoneconfig-syntax.yaml"></a>

```
  [DefaultTimeZone](#cfn-connectcampaignsv2-campaign-localtimezoneconfig-defaulttimezone): {{String}}
  [LocalTimeZoneDetection](#cfn-connectcampaignsv2-campaign-localtimezoneconfig-localtimezonedetection): {{
    - String}}
  [LocalTimeZoneDetectionScope](#cfn-connectcampaignsv2-campaign-localtimezoneconfig-localtimezonedetectionscope): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-localtimezoneconfig-properties"></a>

`DefaultTimeZone`  <a name="cfn-connectcampaignsv2-campaign-localtimezoneconfig-defaulttimezone"></a>
The timezone to use for all recipients.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalTimeZoneDetection`  <a name="cfn-connectcampaignsv2-campaign-localtimezoneconfig-localtimezonedetection"></a>
Detects methods for the recipient's timezone.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocalTimeZoneDetectionScope`  <a name="cfn-connectcampaignsv2-campaign-localtimezoneconfig-localtimezonedetectionscope"></a>
The scope of profile attributes used for timezone detection.
*Required*: No
*Type*: String
*Allowed values*: `PRIMARY_ONLY | ALL_AVAILABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
