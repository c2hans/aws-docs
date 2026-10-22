---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-srtsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input SrtSettings
<a name="aws-properties-medialive-input-srtsettings"></a>

<a name="aws-properties-medialive-input-srtsettings-description"></a>The `SrtSettings` property type specifies Property description not available. for an [AWS::MediaLive::Input](aws-resource-medialive-input.md).

## Syntax
<a name="aws-properties-medialive-input-srtsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-srtsettings-syntax.json"></a>

```
{
  "[SrtCallerSources](#cfn-medialive-input-srtsettings-srtcallersources)" : {{[ SrtCallerSource, ... ]}},
  "[SrtListenerSettings](#cfn-medialive-input-srtsettings-srtlistenersettings)" : {{SrtListenerSettings}}
}
```

### YAML
<a name="aws-properties-medialive-input-srtsettings-syntax.yaml"></a>

```
  [SrtCallerSources](#cfn-medialive-input-srtsettings-srtcallersources): {{
    - SrtCallerSource}}
  [SrtListenerSettings](#cfn-medialive-input-srtsettings-srtlistenersettings): {{
    SrtListenerSettings}}
```

## Properties
<a name="aws-properties-medialive-input-srtsettings-properties"></a>

`SrtCallerSources`  <a name="cfn-medialive-input-srtsettings-srtcallersources"></a>
Property description not available.
*Required*: No
*Type*: Array of [SrtCallerSource](aws-properties-medialive-input-srtcallersource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtListenerSettings`  <a name="cfn-medialive-input-srtsettings-srtlistenersettings"></a>
Property description not available.
*Required*: No
*Type*: [SrtListenerSettings](aws-properties-medialive-input-srtlistenersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
