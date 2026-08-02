---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-dataprotectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL DataProtectionConfig
<a name="aws-properties-wafv2-webacl-dataprotectionconfig"></a>

Specifies data protection to apply to the web request data for the web ACL. This is a web ACL level data protection option.

The data protection that you configure for the web ACL alters the data that's available for any other data collection activity, including your AWS WAF logging destinations, web ACL request sampling, and Amazon Security Lake data collection and management. Your other option for data protection is in the logging configuration, which only affects logging.

This is part of the data protection configuration for a web ACL.

## Syntax
<a name="aws-properties-wafv2-webacl-dataprotectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-dataprotectionconfig-syntax.json"></a>

```
{
  "[DataProtections](#cfn-wafv2-webacl-dataprotectionconfig-dataprotections)" : {{[ DataProtect, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-dataprotectionconfig-syntax.yaml"></a>

```
  [DataProtections](#cfn-wafv2-webacl-dataprotectionconfig-dataprotections): {{
    - DataProtect}}
```

## Properties
<a name="aws-properties-wafv2-webacl-dataprotectionconfig-properties"></a>

`DataProtections`  <a name="cfn-wafv2-webacl-dataprotectionconfig-dataprotections"></a>
An array of data protection configurations for specific web request field types. This is defined for each web ACL. AWS WAF applies the specified protection to all web requests that the web ACL inspects.
*Required*: Yes
*Type*: Array of [DataProtect](aws-properties-wafv2-webacl-dataprotect.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
