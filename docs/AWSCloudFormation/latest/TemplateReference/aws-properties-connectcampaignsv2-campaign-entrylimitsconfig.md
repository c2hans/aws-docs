---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-entrylimitsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign EntryLimitsConfig
<a name="aws-properties-connectcampaignsv2-campaign-entrylimitsconfig"></a>

Contains entry limits configuration for an outbound campaign. Entry limits control how many times a participant can enter a campaign and the minimum time interval between re-entries.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-entrylimitsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-entrylimitsconfig-syntax.json"></a>

```
{
  "[MaxEntryCount](#cfn-connectcampaignsv2-campaign-entrylimitsconfig-maxentrycount)" : {{Integer}},
  "[MinEntryInterval](#cfn-connectcampaignsv2-campaign-entrylimitsconfig-minentryinterval)" : {{String}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-entrylimitsconfig-syntax.yaml"></a>

```
  [MaxEntryCount](#cfn-connectcampaignsv2-campaign-entrylimitsconfig-maxentrycount): {{Integer}}
  [MinEntryInterval](#cfn-connectcampaignsv2-campaign-entrylimitsconfig-minentryinterval): {{String}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-entrylimitsconfig-properties"></a>

`MaxEntryCount`  <a name="cfn-connectcampaignsv2-campaign-entrylimitsconfig-maxentrycount"></a>
The maximum number of times a participant can enter the campaign. A value of `0` indicates unlimited entries. Values of `1` or greater specify the exact number of entries allowed.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinEntryInterval`  <a name="cfn-connectcampaignsv2-campaign-entrylimitsconfig-minentryinterval"></a>
The minimum time interval that must pass before a participant can enter the campaign again, specified as an ISO 8601 duration string (for example, `PT4H` for 4 hours). A value of zero (for example, `PT0H`) indicates no minimum interval restriction, allowing participants to re-enter regardless of when they last entered.
*Required*: Yes
*Type*: String
*Pattern*: `^P(?:([-+]?[0-9]+)D)?(T(?:([-+]?[0-9]+)H)?(?:([-+]?[0-9]+)M)?(?:([-+]?[0-9]+)(?:[.,]([0-9]{0,9}))?S)?)?$`
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
