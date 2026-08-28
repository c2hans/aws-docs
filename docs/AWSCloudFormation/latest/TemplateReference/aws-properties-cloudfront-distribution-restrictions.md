---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-restrictions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution Restrictions
<a name="aws-properties-cloudfront-distribution-restrictions"></a>

A complex type that identifies ways in which you want to restrict distribution of your content.

## Syntax
<a name="aws-properties-cloudfront-distribution-restrictions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-restrictions-syntax.json"></a>

```
{
  "[GeoRestriction](#cfn-cloudfront-distribution-restrictions-georestriction)" : {{GeoRestriction}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-restrictions-syntax.yaml"></a>

```
  [GeoRestriction](#cfn-cloudfront-distribution-restrictions-georestriction): {{
    GeoRestriction}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-restrictions-properties"></a>

`GeoRestriction`  <a name="cfn-cloudfront-distribution-restrictions-georestriction"></a>
A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using `MaxMind` GeoIP databases. To disable geo restriction, remove the [Restrictions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-restrictions) property from your stack template.
*Required*: Yes
*Type*: [GeoRestriction](aws-properties-cloudfront-distribution-georestriction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-cloudfront-distribution-restrictions--seealso"></a>
+ [Restrictions](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Restrictions.html) in the *Amazon CloudFront API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
