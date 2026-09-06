---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-networkanalyzerconfiguration-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::NetworkAnalyzerConfiguration Tag
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tag"></a>

The tags to attach to the network analyzer configuration. Tags are metadata that you can use to manage a resource.

## Syntax
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tag-syntax.json"></a>

```
{
  "[Key](#cfn-iotwireless-networkanalyzerconfiguration-tag-key)" : {{String}},
  "[Value](#cfn-iotwireless-networkanalyzerconfiguration-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tag-syntax.yaml"></a>

```
  [Key](#cfn-iotwireless-networkanalyzerconfiguration-tag-key): {{String}}
  [Value](#cfn-iotwireless-networkanalyzerconfiguration-tag-value): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-networkanalyzerconfiguration-tag-properties"></a>

`Key`  <a name="cfn-iotwireless-networkanalyzerconfiguration-tag-key"></a>
The tag's key value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iotwireless-networkanalyzerconfiguration-tag-value"></a>
The tag's value.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
