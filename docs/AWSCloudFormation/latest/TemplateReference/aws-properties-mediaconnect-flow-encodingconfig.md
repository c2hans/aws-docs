---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-encodingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow EncodingConfig
<a name="aws-properties-mediaconnect-flow-encodingconfig"></a>

 The encoding configuration to apply to the NDI® source when transcoding it to a transport stream for downstream distribution. You can choose between several predefined encoding profiles based on common use cases.

## Syntax
<a name="aws-properties-mediaconnect-flow-encodingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-encodingconfig-syntax.json"></a>

```
{
  "[EncodingProfile](#cfn-mediaconnect-flow-encodingconfig-encodingprofile)" : {{String}},
  "[VideoMaxBitrate](#cfn-mediaconnect-flow-encodingconfig-videomaxbitrate)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-encodingconfig-syntax.yaml"></a>

```
  [EncodingProfile](#cfn-mediaconnect-flow-encodingconfig-encodingprofile): {{String}}
  [VideoMaxBitrate](#cfn-mediaconnect-flow-encodingconfig-videomaxbitrate): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-encodingconfig-properties"></a>

`EncodingProfile`  <a name="cfn-mediaconnect-flow-encodingconfig-encodingprofile"></a>
 The encoding profile to use when transcoding the NDI source content to a transport stream. You can change this value while the flow is running.
*Required*: No
*Type*: String
*Allowed values*: `DISTRIBUTION_H264_DEFAULT | CONTRIBUTION_H264_DEFAULT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoMaxBitrate`  <a name="cfn-mediaconnect-flow-encodingconfig-videomaxbitrate"></a>
 The maximum video bitrate to use when transcoding the NDI source to a transport stream. This parameter enables you to override the default video bitrate within the encoding profile's supported range.
 The supported range is 10,000,000 - 50,000,000 bits per second (bps). If you don't specify a value, MediaConnect uses the default value of 20,000,000 bps.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
