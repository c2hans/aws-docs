---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-audiomonitoringsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow AudioMonitoringSetting
<a name="aws-properties-mediaconnect-flow-audiomonitoringsetting"></a>

 Specifies the configuration for audio stream metrics monitoring.

## Syntax
<a name="aws-properties-mediaconnect-flow-audiomonitoringsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-audiomonitoringsetting-syntax.json"></a>

```
{
  "[SilentAudio](#cfn-mediaconnect-flow-audiomonitoringsetting-silentaudio)" : {{SilentAudio}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-audiomonitoringsetting-syntax.yaml"></a>

```
  [SilentAudio](#cfn-mediaconnect-flow-audiomonitoringsetting-silentaudio): {{
    SilentAudio}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-audiomonitoringsetting-properties"></a>

`SilentAudio`  <a name="cfn-mediaconnect-flow-audiomonitoringsetting-silentaudio"></a>
 Detects periods of silence.
*Required*: No
*Type*: [SilentAudio](aws-properties-mediaconnect-flow-silentaudio.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
