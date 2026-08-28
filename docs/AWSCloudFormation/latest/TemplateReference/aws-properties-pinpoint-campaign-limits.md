---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-campaign-limits.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Campaign Limits
<a name="aws-properties-pinpoint-campaign-limits"></a>

Specifies the limits on the messages that a campaign can send.

## Syntax
<a name="aws-properties-pinpoint-campaign-limits-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-campaign-limits-syntax.json"></a>

```
{
  "[Daily](#cfn-pinpoint-campaign-limits-daily)" : {{Integer}},
  "[MaximumDuration](#cfn-pinpoint-campaign-limits-maximumduration)" : {{Integer}},
  "[MessagesPerSecond](#cfn-pinpoint-campaign-limits-messagespersecond)" : {{Integer}},
  "[Session](#cfn-pinpoint-campaign-limits-session)" : {{Integer}},
  "[Total](#cfn-pinpoint-campaign-limits-total)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-pinpoint-campaign-limits-syntax.yaml"></a>

```
  [Daily](#cfn-pinpoint-campaign-limits-daily): {{Integer}}
  [MaximumDuration](#cfn-pinpoint-campaign-limits-maximumduration): {{Integer}}
  [MessagesPerSecond](#cfn-pinpoint-campaign-limits-messagespersecond): {{Integer}}
  [Session](#cfn-pinpoint-campaign-limits-session): {{Integer}}
  [Total](#cfn-pinpoint-campaign-limits-total): {{Integer}}
```

## Properties
<a name="aws-properties-pinpoint-campaign-limits-properties"></a>

`Daily`  <a name="cfn-pinpoint-campaign-limits-daily"></a>
The maximum number of messages that a campaign can send to a single endpoint during a 24-hour period. The maximum value is 100.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumDuration`  <a name="cfn-pinpoint-campaign-limits-maximumduration"></a>
The maximum amount of time, in seconds, that a campaign can attempt to deliver a message after the scheduled start time for the campaign. The minimum value is 60 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessagesPerSecond`  <a name="cfn-pinpoint-campaign-limits-messagespersecond"></a>
The maximum number of messages that a campaign can send each second. The minimum value is 1. The maximum value is 20,000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Session`  <a name="cfn-pinpoint-campaign-limits-session"></a>
The maximum number of messages that the campaign can send per user session.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Total`  <a name="cfn-pinpoint-campaign-limits-total"></a>
The maximum number of messages that a campaign can send to a single endpoint during the course of the campaign. The maximum value is 100.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
