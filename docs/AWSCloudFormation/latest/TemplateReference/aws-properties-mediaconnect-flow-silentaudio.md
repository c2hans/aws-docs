---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-silentaudio.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow SilentAudio
<a name="aws-properties-mediaconnect-flow-silentaudio"></a>

Configures settings for the `SilentAudio` metric.

## Syntax
<a name="aws-properties-mediaconnect-flow-silentaudio-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-silentaudio-syntax.json"></a>

```
{
  "[State](#cfn-mediaconnect-flow-silentaudio-state)" : {{String}},
  "[ThresholdSeconds](#cfn-mediaconnect-flow-silentaudio-thresholdseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-silentaudio-syntax.yaml"></a>

```
  [State](#cfn-mediaconnect-flow-silentaudio-state): {{String}}
  [ThresholdSeconds](#cfn-mediaconnect-flow-silentaudio-thresholdseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-silentaudio-properties"></a>

`State`  <a name="cfn-mediaconnect-flow-silentaudio-state"></a>
Indicates whether the `SilentAudio` metric is enabled or disabled.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdSeconds`  <a name="cfn-mediaconnect-flow-silentaudio-thresholdseconds"></a>
Specifies the number of consecutive seconds of silence that triggers an event or alert.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
