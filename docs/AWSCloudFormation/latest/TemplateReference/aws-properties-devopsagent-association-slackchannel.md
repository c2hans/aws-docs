---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-slackchannel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association SlackChannel
<a name="aws-properties-devopsagent-association-slackchannel"></a>

Represents a Slack channel with its unique identifier and optional display name.

## Syntax
<a name="aws-properties-devopsagent-association-slackchannel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-slackchannel-syntax.json"></a>

```
{
  "[ChannelId](#cfn-devopsagent-association-slackchannel-channelid)" : {{String}},
  "[ChannelName](#cfn-devopsagent-association-slackchannel-channelname)" : {{String}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-slackchannel-syntax.yaml"></a>

```
  [ChannelId](#cfn-devopsagent-association-slackchannel-channelid): {{String}}
  [ChannelName](#cfn-devopsagent-association-slackchannel-channelname): {{String}}
```

## Properties
<a name="aws-properties-devopsagent-association-slackchannel-properties"></a>

`ChannelId`  <a name="cfn-devopsagent-association-slackchannel-channelid"></a>
The Slack channel ID.
The ID must match the pattern `^[CGD][A-Z0-9]+$` and be between 8 and 16 characters.
*Required*: Yes
*Type*: String
*Pattern*: `^[CGD][A-Z0-9]+$`
*Minimum*: `8`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelName`  <a name="cfn-devopsagent-association-slackchannel-channelname"></a>
Slack channel name.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
