---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connectcampaignsv2-campaign-timeoutconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ConnectCampaignsV2::Campaign TimeoutConfig
<a name="aws-properties-connectcampaignsv2-campaign-timeoutconfig"></a>

Contains preview outbound mode timeout configuration.

## Syntax
<a name="aws-properties-connectcampaignsv2-campaign-timeoutconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connectcampaignsv2-campaign-timeoutconfig-syntax.json"></a>

```
{
  "[DurationInSeconds](#cfn-connectcampaignsv2-campaign-timeoutconfig-durationinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-connectcampaignsv2-campaign-timeoutconfig-syntax.yaml"></a>

```
  [DurationInSeconds](#cfn-connectcampaignsv2-campaign-timeoutconfig-durationinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-connectcampaignsv2-campaign-timeoutconfig-properties"></a>

`DurationInSeconds`  <a name="cfn-connectcampaignsv2-campaign-timeoutconfig-durationinseconds"></a>
Duration in seconds for the countdown timer.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
