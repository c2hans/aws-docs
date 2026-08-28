---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-followerchannelsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel FollowerChannelSettings
<a name="aws-properties-medialive-channel-followerchannelsettings"></a>

Settings for a follower channel in a linked pair.

## Syntax
<a name="aws-properties-medialive-channel-followerchannelsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-followerchannelsettings-syntax.json"></a>

```
{
  "[LinkedChannelType](#cfn-medialive-channel-followerchannelsettings-linkedchanneltype)" : {{String}},
  "[PrimaryChannelArn](#cfn-medialive-channel-followerchannelsettings-primarychannelarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-followerchannelsettings-syntax.yaml"></a>

```
  [LinkedChannelType](#cfn-medialive-channel-followerchannelsettings-linkedchanneltype): {{String}}
  [PrimaryChannelArn](#cfn-medialive-channel-followerchannelsettings-primarychannelarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-followerchannelsettings-properties"></a>

`LinkedChannelType`  <a name="cfn-medialive-channel-followerchannelsettings-linkedchanneltype"></a>
Specifies this as a follower channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryChannelArn`  <a name="cfn-medialive-channel-followerchannelsettings-primarychannelarn"></a>
The ARN of the primary channel to follow.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
