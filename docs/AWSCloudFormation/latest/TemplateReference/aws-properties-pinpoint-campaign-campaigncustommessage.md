---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-campaign-campaigncustommessage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Campaign CampaignCustomMessage
<a name="aws-properties-pinpoint-campaign-campaigncustommessage"></a>

Specifies the contents of a message that's sent through a custom channel to recipients of a campaign.

## Syntax
<a name="aws-properties-pinpoint-campaign-campaigncustommessage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-campaign-campaigncustommessage-syntax.json"></a>

```
{
  "[Data](#cfn-pinpoint-campaign-campaigncustommessage-data)" : {{String}}
}
```

### YAML
<a name="aws-properties-pinpoint-campaign-campaigncustommessage-syntax.yaml"></a>

```
  [Data](#cfn-pinpoint-campaign-campaigncustommessage-data): {{String}}
```

## Properties
<a name="aws-properties-pinpoint-campaign-campaigncustommessage-properties"></a>

`Data`  <a name="cfn-pinpoint-campaign-campaigncustommessage-data"></a>
The raw, JSON-formatted string to use as the payload for the message. The maximum size is 5 KB.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
