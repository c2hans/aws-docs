---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-mediaconnectflow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input MediaConnectFlow
<a name="aws-properties-medialive-input-mediaconnectflow"></a>

The settings for a MediaConnect Flow.

## Syntax
<a name="aws-properties-medialive-input-mediaconnectflow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-mediaconnectflow-syntax.json"></a>

```
{
  "[FlowArn](#cfn-medialive-input-mediaconnectflow-flowarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-mediaconnectflow-syntax.yaml"></a>

```
  [FlowArn](#cfn-medialive-input-mediaconnectflow-flowarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-mediaconnectflow-properties"></a>

`FlowArn`  <a name="cfn-medialive-input-mediaconnectflow-flowarn"></a>
The unique ARN of the MediaConnect Flow being used as a source.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
