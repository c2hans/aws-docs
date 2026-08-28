---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distributiontenant-georestrictioncustomization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant GeoRestrictionCustomization
<a name="aws-properties-cloudfront-distributiontenant-georestrictioncustomization"></a>

The customizations that you specified for the distribution tenant for geographic restrictions.

## Syntax
<a name="aws-properties-cloudfront-distributiontenant-georestrictioncustomization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distributiontenant-georestrictioncustomization-syntax.json"></a>

```
{
  "[Locations](#cfn-cloudfront-distributiontenant-georestrictioncustomization-locations)" : {{[ String, ... ]}},
  "[RestrictionType](#cfn-cloudfront-distributiontenant-georestrictioncustomization-restrictiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distributiontenant-georestrictioncustomization-syntax.yaml"></a>

```
  [Locations](#cfn-cloudfront-distributiontenant-georestrictioncustomization-locations): {{
    - String}}
  [RestrictionType](#cfn-cloudfront-distributiontenant-georestrictioncustomization-restrictiontype): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distributiontenant-georestrictioncustomization-properties"></a>

`Locations`  <a name="cfn-cloudfront-distributiontenant-georestrictioncustomization-locations"></a>
The locations for geographic restrictions.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestrictionType`  <a name="cfn-cloudfront-distributiontenant-georestrictioncustomization-restrictiontype"></a>
The method that you want to use to restrict distribution of your content by country:
+ `none`: No geographic restriction is enabled, meaning access to content is not restricted by client geo location.
+ `blacklist`: The `Location` elements specify the countries in which you don't want CloudFront to distribute your content.
+ `whitelist`: The `Location` elements specify the countries in which you want CloudFront to distribute your content.
*Required*: No
*Type*: String
*Allowed values*: `blacklist | whitelist | none`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
