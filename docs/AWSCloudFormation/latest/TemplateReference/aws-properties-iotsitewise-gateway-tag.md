---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-gateway-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Gateway Tag
<a name="aws-properties-iotsitewise-gateway-tag"></a>

A list of key-value pairs that contain metadata for the gateway. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the *AWS IoT SiteWise User Guide*.

## Syntax
<a name="aws-properties-iotsitewise-gateway-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-gateway-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotsitewise-gateway-tag-key)" : {{String}},
  "[Value](#cfn-iotsitewise-gateway-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotsitewise-gateway-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotsitewise-gateway-tag-key): {{String}}
  [Value](#cfn-iotsitewise-gateway-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotsitewise-gateway-tag-properties"></a>

`Key`  <a name="cfn-iotsitewise-gateway-tag-key"></a>
The key or name that identifies the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotsitewise-gateway-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
