---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-applicationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ApplicationConfig
<a name="aws-properties-wafv2-webacl-applicationconfig"></a>

A list of `ApplicationAttribute`s that contains information about the application.

## Syntax
<a name="aws-properties-wafv2-webacl-applicationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-applicationconfig-syntax.json"></a>

```
{
  "[Attributes](#cfn-wafv2-webacl-applicationconfig-attributes)" : {{[ ApplicationAttribute, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-applicationconfig-syntax.yaml"></a>

```
  [Attributes](#cfn-wafv2-webacl-applicationconfig-attributes): {{
    - ApplicationAttribute}}
```

## Properties
<a name="aws-properties-wafv2-webacl-applicationconfig-properties"></a>

`Attributes`  <a name="cfn-wafv2-webacl-applicationconfig-attributes"></a>
Contains the attribute name and a list of values for that attribute.
*Required*: Yes
*Type*: Array of [ApplicationAttribute](aws-properties-wafv2-webacl-applicationattribute.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
