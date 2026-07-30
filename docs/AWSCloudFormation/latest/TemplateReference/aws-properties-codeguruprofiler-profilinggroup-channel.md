---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codeguruprofiler-profilinggroup-channel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeGuruProfiler::ProfilingGroup Channel
<a name="aws-properties-codeguruprofiler-profilinggroup-channel"></a>

Notification medium for users to get alerted for events that occur in application profile. We support SNS topic as a notification channel.

## Syntax
<a name="aws-properties-codeguruprofiler-profilinggroup-channel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codeguruprofiler-profilinggroup-channel-syntax.json"></a>

```
{
  "[channelId](#cfn-codeguruprofiler-profilinggroup-channel-channelid)" : {{String}},
  "[channelUri](#cfn-codeguruprofiler-profilinggroup-channel-channeluri)" : {{String}}
}
```

### YAML
<a name="aws-properties-codeguruprofiler-profilinggroup-channel-syntax.yaml"></a>

```
  [channelId](#cfn-codeguruprofiler-profilinggroup-channel-channelid): {{String}}
  [channelUri](#cfn-codeguruprofiler-profilinggroup-channel-channeluri): {{String}}
```

## Properties
<a name="aws-properties-codeguruprofiler-profilinggroup-channel-properties"></a>

`channelId`  <a name="cfn-codeguruprofiler-profilinggroup-channel-channelid"></a>
The channel ID.
*Required*: No
*Type*: String
*Pattern*: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`channelUri`  <a name="cfn-codeguruprofiler-profilinggroup-channel-channeluri"></a>
The channel URI.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws([-\w]*):[a-z-]+:(([a-z]+-)+[0-9]+)?:([0-9]{12}):[^.]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
