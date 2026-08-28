---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-videomonitoringsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow VideoMonitoringSetting
<a name="aws-properties-mediaconnect-flow-videomonitoringsetting"></a>

Specifies the configuration for video stream metrics monitoring.

## Syntax
<a name="aws-properties-mediaconnect-flow-videomonitoringsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-videomonitoringsetting-syntax.json"></a>

```
{
  "[BlackFrames](#cfn-mediaconnect-flow-videomonitoringsetting-blackframes)" : {{BlackFrames}},
  "[FrozenFrames](#cfn-mediaconnect-flow-videomonitoringsetting-frozenframes)" : {{FrozenFrames}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-videomonitoringsetting-syntax.yaml"></a>

```
  [BlackFrames](#cfn-mediaconnect-flow-videomonitoringsetting-blackframes): {{
    BlackFrames}}
  [FrozenFrames](#cfn-mediaconnect-flow-videomonitoringsetting-frozenframes): {{
    FrozenFrames}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-videomonitoringsetting-properties"></a>

`BlackFrames`  <a name="cfn-mediaconnect-flow-videomonitoringsetting-blackframes"></a>
Detects video frames that are black.
*Required*: No
*Type*: [BlackFrames](aws-properties-mediaconnect-flow-blackframes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FrozenFrames`  <a name="cfn-mediaconnect-flow-videomonitoringsetting-frozenframes"></a>
Detects video frames that have not changed.
*Required*: No
*Type*: [FrozenFrames](aws-properties-mediaconnect-flow-frozenframes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
