---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-channelengineversionrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel ChannelEngineVersionRequest
<a name="aws-properties-medialive-channel-channelengineversionrequest"></a>

The desired engine version for this channel.

## Syntax
<a name="aws-properties-medialive-channel-channelengineversionrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-channelengineversionrequest-syntax.json"></a>

```
{
  "[Version](#cfn-medialive-channel-channelengineversionrequest-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-channelengineversionrequest-syntax.yaml"></a>

```
  [Version](#cfn-medialive-channel-channelengineversionrequest-version): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-channelengineversionrequest-properties"></a>

`Version`  <a name="cfn-medialive-channel-channelengineversionrequest-version"></a>
The build identifier of the engine version to use for this channel. Specify 'DEFAULT' to reset to the default version.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
