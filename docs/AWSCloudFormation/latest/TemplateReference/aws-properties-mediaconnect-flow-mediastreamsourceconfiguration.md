---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-mediastreamsourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow MediaStreamSourceConfiguration
<a name="aws-properties-mediaconnect-flow-mediastreamsourceconfiguration"></a>

The media stream that is associated with the source, and the parameters for that association.

## Syntax
<a name="aws-properties-mediaconnect-flow-mediastreamsourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-mediastreamsourceconfiguration-syntax.json"></a>

```
{
  "[EncodingName](#cfn-mediaconnect-flow-mediastreamsourceconfiguration-encodingname)" : {{String}},
  "[InputConfigurations](#cfn-mediaconnect-flow-mediastreamsourceconfiguration-inputconfigurations)" : {{[ InputConfiguration, ... ]}},
  "[MediaStreamName](#cfn-mediaconnect-flow-mediastreamsourceconfiguration-mediastreamname)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-mediastreamsourceconfiguration-syntax.yaml"></a>

```
  [EncodingName](#cfn-mediaconnect-flow-mediastreamsourceconfiguration-encodingname): {{String}}
  [InputConfigurations](#cfn-mediaconnect-flow-mediastreamsourceconfiguration-inputconfigurations): {{
    - InputConfiguration}}
  [MediaStreamName](#cfn-mediaconnect-flow-mediastreamsourceconfiguration-mediastreamname): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-mediastreamsourceconfiguration-properties"></a>

`EncodingName`  <a name="cfn-mediaconnect-flow-mediastreamsourceconfiguration-encodingname"></a>
 The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.
*Required*: Yes
*Type*: String
*Allowed values*: `jxsv | raw | smpte291 | pcm`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputConfigurations`  <a name="cfn-mediaconnect-flow-mediastreamsourceconfiguration-inputconfigurations"></a>
The media streams that you want to associate with the source.
*Required*: No
*Type*: Array of [InputConfiguration](aws-properties-mediaconnect-flow-inputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaStreamName`  <a name="cfn-mediaconnect-flow-mediastreamsourceconfiguration-mediastreamname"></a>
A name that helps you distinguish one media stream from another.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
