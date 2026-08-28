---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-campaign-quiettime.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Campaign QuietTime
<a name="aws-properties-pinpoint-campaign-quiettime"></a>

Specifies the start and end times that define a time range when messages aren't sent to endpoints.

## Syntax
<a name="aws-properties-pinpoint-campaign-quiettime-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-campaign-quiettime-syntax.json"></a>

```
{
  "[End](#cfn-pinpoint-campaign-quiettime-end)" : {{String}},
  "[Start](#cfn-pinpoint-campaign-quiettime-start)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-campaign-quiettime-syntax.yaml"></a>

```
  [End](#cfn-pinpoint-campaign-quiettime-end): {{String}}
  [Start](#cfn-pinpoint-campaign-quiettime-start): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-campaign-quiettime-properties"></a>

`End`  <a name="cfn-pinpoint-campaign-quiettime-end"></a>
The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Start`  <a name="cfn-pinpoint-campaign-quiettime-start"></a>
The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use `02:30` to represent 2:30 AM, or `14:30` to represent 2:30 PM.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
