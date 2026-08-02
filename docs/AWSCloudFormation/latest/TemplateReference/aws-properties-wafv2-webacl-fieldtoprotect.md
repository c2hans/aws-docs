---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-webacl-fieldtoprotect.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::WebACL FieldToProtect
<a name="aws-properties-wafv2-webacl-fieldtoprotect"></a>

Specifies a field type and keys to protect in stored web request data. This is part of the data protection configuration for a web ACL.

## Syntax
<a name="aws-properties-wafv2-webacl-fieldtoprotect-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-webacl-fieldtoprotect-syntax.json"></a>

```
{
  "[FieldKeys](#cfn-wafv2-webacl-fieldtoprotect-fieldkeys)" : {{[ String, ... ]}},
  "[FieldType](#cfn-wafv2-webacl-fieldtoprotect-fieldtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-wafv2-webacl-fieldtoprotect-syntax.yaml"></a>

```
  [FieldKeys](#cfn-wafv2-webacl-fieldtoprotect-fieldkeys): {{
    - String}}
  [FieldType](#cfn-wafv2-webacl-fieldtoprotect-fieldtype): {{String}}
```

## Properties
<a name="aws-properties-wafv2-webacl-fieldtoprotect-properties"></a>

`FieldKeys`  <a name="cfn-wafv2-webacl-fieldtoprotect-fieldkeys"></a>
Specifies the keys to protect for the specified field type. If you don't specify any key, then all keys for the field type are protected.
*Required*: No
*Type*: Array of String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldType`  <a name="cfn-wafv2-webacl-fieldtoprotect-fieldtype"></a>
Specifies the web request component type to protect.
*Required*: Yes
*Type*: String
*Allowed values*: `SINGLE_HEADER | SINGLE_COOKIE | SINGLE_QUERY_ARGUMENT | QUERY_STRING | BODY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
