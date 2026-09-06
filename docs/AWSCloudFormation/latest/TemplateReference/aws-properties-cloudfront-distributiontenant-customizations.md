---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distributiontenant-customizations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant Customizations
<a name="aws-properties-cloudfront-distributiontenant-customizations"></a>

Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.

## Syntax
<a name="aws-properties-cloudfront-distributiontenant-customizations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distributiontenant-customizations-syntax.json"></a>

```
{
  "[Certificate](#cfn-cloudfront-distributiontenant-customizations-certificate)" : {{Certificate}},
  "[GeoRestrictions](#cfn-cloudfront-distributiontenant-customizations-georestrictions)" : {{GeoRestrictionCustomization}},
  "[WebAcl](#cfn-cloudfront-distributiontenant-customizations-webacl)" : {{WebAclCustomization}}
}
```

### YAML
<a name="aws-properties-cloudfront-distributiontenant-customizations-syntax.yaml"></a>

```
  [Certificate](#cfn-cloudfront-distributiontenant-customizations-certificate): {{
    Certificate}}
  [GeoRestrictions](#cfn-cloudfront-distributiontenant-customizations-georestrictions): {{
    GeoRestrictionCustomization}}
  [WebAcl](#cfn-cloudfront-distributiontenant-customizations-webacl): {{
    WebAclCustomization}}
```

## Properties
<a name="aws-properties-cloudfront-distributiontenant-customizations-properties"></a>

`Certificate`  <a name="cfn-cloudfront-distributiontenant-customizations-certificate"></a>
The AWS Certificate Manager (ACM) certificate.
*Required*: No
*Type*: [Certificate](aws-properties-cloudfront-distributiontenant-certificate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GeoRestrictions`  <a name="cfn-cloudfront-distributiontenant-customizations-georestrictions"></a>
The geographic restrictions.
*Required*: No
*Type*: [GeoRestrictionCustomization](aws-properties-cloudfront-distributiontenant-georestrictioncustomization.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebAcl`  <a name="cfn-cloudfront-distributiontenant-customizations-webacl"></a>
The AWS WAF web ACL.
*Required*: No
*Type*: [WebAclCustomization](aws-properties-cloudfront-distributiontenant-webaclcustomization.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
