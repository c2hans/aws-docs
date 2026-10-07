---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-adconfiguration-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::AdConfiguration Tag
<a name="aws-properties-ivs-adconfiguration-tag"></a>

<a name="aws-properties-ivs-adconfiguration-tag-description"></a>The `Tag` property type specifies Property description not available. for an [AWS::IVS::AdConfiguration](aws-resource-ivs-adconfiguration.md).

## Syntax
<a name="aws-properties-ivs-adconfiguration-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-adconfiguration-tag-syntax.json"></a>

```
{
  "[Key](#cfn-ivs-adconfiguration-tag-key)" : {{String}},
  "[Value](#cfn-ivs-adconfiguration-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ivs-adconfiguration-tag-syntax.yaml"></a>

```
  [Key](#cfn-ivs-adconfiguration-tag-key): {{String}}
  [Value](#cfn-ivs-adconfiguration-tag-value): {{String}}
```

## Properties
<a name="aws-properties-ivs-adconfiguration-tag-properties"></a>

`Key`  <a name="cfn-ivs-adconfiguration-tag-key"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ivs-adconfiguration-tag-value"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
