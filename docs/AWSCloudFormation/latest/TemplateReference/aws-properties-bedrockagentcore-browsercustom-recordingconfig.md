---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserCustom RecordingConfig
<a name="aws-properties-bedrockagentcore-browsercustom-recordingconfig"></a>

The recording configuration for a browser. This structure defines how browser sessions are recorded.

## Syntax
<a name="aws-properties-bedrockagentcore-browsercustom-recordingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-browsercustom-recordingconfig-syntax.json"></a>

```
{
  "[Enabled](#cfn-bedrockagentcore-browsercustom-recordingconfig-enabled)" : {{Boolean}},
  "[S3Location](#cfn-bedrockagentcore-browsercustom-recordingconfig-s3location)" : {{S3Location}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-browsercustom-recordingconfig-syntax.yaml"></a>

```
  [Enabled](#cfn-bedrockagentcore-browsercustom-recordingconfig-enabled): {{Boolean}}
  [S3Location](#cfn-bedrockagentcore-browsercustom-recordingconfig-s3location): {{
    S3Location}}
```

## Properties
<a name="aws-properties-bedrockagentcore-browsercustom-recordingconfig-properties"></a>

`Enabled`  <a name="cfn-bedrockagentcore-browsercustom-recordingconfig-enabled"></a>
Indicates whether recording is enabled for the browser. When set to true, browser sessions are recorded.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Location`  <a name="cfn-bedrockagentcore-browsercustom-recordingconfig-s3location"></a>
The Amazon S3 location where browser recordings are stored. This location contains the recorded browser sessions.
*Required*: No
*Type*: [S3Location](aws-properties-bedrockagentcore-browsercustom-s3location.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
