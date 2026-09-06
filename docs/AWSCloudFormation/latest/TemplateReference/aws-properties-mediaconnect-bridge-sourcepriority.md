---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-bridge-sourcepriority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Bridge SourcePriority
<a name="aws-properties-mediaconnect-bridge-sourcepriority"></a>

 The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.

## Syntax
<a name="aws-properties-mediaconnect-bridge-sourcepriority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-bridge-sourcepriority-syntax.json"></a>

```
{
  "[PrimarySource](#cfn-mediaconnect-bridge-sourcepriority-primarysource)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-bridge-sourcepriority-syntax.yaml"></a>

```
  [PrimarySource](#cfn-mediaconnect-bridge-sourcepriority-primarysource): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-bridge-sourcepriority-properties"></a>

`PrimarySource`  <a name="cfn-mediaconnect-bridge-sourcepriority-primarysource"></a>
 The name of the source you choose as the primary source for this flow.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
