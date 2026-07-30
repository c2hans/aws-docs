---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-tenantconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution TenantConfig
<a name="aws-properties-cloudfront-distribution-tenantconfig"></a>

**Note**
This field only supports multi-tenant distributions. You can't specify this field for standard distributions. For more information, see [Unsupported features for SaaS Manager for Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html#unsupported-saas) in the *Amazon CloudFront Developer Guide*.

The configuration for a distribution tenant.

## Syntax
<a name="aws-properties-cloudfront-distribution-tenantconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-tenantconfig-syntax.json"></a>

```
{
  "[ParameterDefinitions](#cfn-cloudfront-distribution-tenantconfig-parameterdefinitions)" : {{[ ParameterDefinition, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-tenantconfig-syntax.yaml"></a>

```
  [ParameterDefinitions](#cfn-cloudfront-distribution-tenantconfig-parameterdefinitions): {{
    - ParameterDefinition}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-tenantconfig-properties"></a>

`ParameterDefinitions`  <a name="cfn-cloudfront-distribution-tenantconfig-parameterdefinitions"></a>
The parameters that you specify for a distribution tenant.
*Required*: No
*Type*: Array of [ParameterDefinition](aws-properties-cloudfront-distribution-parameterdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
