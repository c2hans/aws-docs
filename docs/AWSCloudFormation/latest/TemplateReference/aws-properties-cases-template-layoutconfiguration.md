---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-template-layoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::Template LayoutConfiguration
<a name="aws-properties-cases-template-layoutconfiguration"></a>

Object to store configuration of layouts associated to the template.

## Syntax
<a name="aws-properties-cases-template-layoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-template-layoutconfiguration-syntax.json"></a>

```
{
  "[DefaultLayout](#cfn-cases-template-layoutconfiguration-defaultlayout)" : {{String}}
}
```

### YAML
<a name="aws-properties-cases-template-layoutconfiguration-syntax.yaml"></a>

```
  [DefaultLayout](#cfn-cases-template-layoutconfiguration-defaultlayout): {{String}}
```

## Properties
<a name="aws-properties-cases-template-layoutconfiguration-properties"></a>

`DefaultLayout`  <a name="cfn-cases-template-layoutconfiguration-defaultlayout"></a>
 Unique identifier of a layout.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
