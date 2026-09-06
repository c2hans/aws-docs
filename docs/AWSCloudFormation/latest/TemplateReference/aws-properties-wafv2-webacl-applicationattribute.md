---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-applicationattribute.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL ApplicationAttribute
<a name="aws-properties-wafv2-webacl-applicationattribute"></a>

Application details defined during the web ACL creation process. Application attributes help AWS WAF give recommendations for protection packs.

## Syntax
<a name="aws-properties-wafv2-webacl-applicationattribute-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-applicationattribute-syntax.json"></a>

```
{
  "[Name](#cfn-wafv2-webacl-applicationattribute-name)" : {{String}},
  "[Values](#cfn-wafv2-webacl-applicationattribute-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-applicationattribute-syntax.yaml"></a>

```
  [Name](#cfn-wafv2-webacl-applicationattribute-name): {{String}}
  [Values](#cfn-wafv2-webacl-applicationattribute-values): {{
    - String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-applicationattribute-properties"></a>

`Name`  <a name="cfn-wafv2-webacl-applicationattribute-name"></a>
Specifies the attribute name.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-wafv2-webacl-applicationattribute-values"></a>
Specifies the attribute value.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
