---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pinpoint-segment-behavior.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pinpoint::Segment Behavior
<a name="aws-properties-pinpoint-segment-behavior"></a>

Specifies behavior-based criteria for the segment, such as how recently users have used your app.

## Syntax
<a name="aws-properties-pinpoint-segment-behavior-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pinpoint-segment-behavior-syntax.json"></a>

```
{
  "[Recency](#cfn-pinpoint-segment-behavior-recency)" : {{Recency}}
}
```

### YAML
<a name="aws-properties-pinpoint-segment-behavior-syntax.yaml"></a>

```
  [Recency](#cfn-pinpoint-segment-behavior-recency): {{
    Recency}}
```

## Properties
<a name="aws-properties-pinpoint-segment-behavior-properties"></a>

`Recency`  <a name="cfn-pinpoint-segment-behavior-recency"></a>
Specifies how recently segment members were active.
*Required*: No
*Type*: [Recency](aws-properties-pinpoint-segment-recency.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
