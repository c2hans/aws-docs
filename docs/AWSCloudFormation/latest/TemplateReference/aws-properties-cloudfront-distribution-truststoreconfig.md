---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-truststoreconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution TrustStoreConfig
<a name="aws-properties-cloudfront-distribution-truststoreconfig"></a>

A trust store configuration.

## Syntax
<a name="aws-properties-cloudfront-distribution-truststoreconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-truststoreconfig-syntax.json"></a>

```
{
  "[AdvertiseTrustStoreCaNames](#cfn-cloudfront-distribution-truststoreconfig-advertisetruststorecanames)" : {{Boolean}},
  "[IgnoreCertificateExpiry](#cfn-cloudfront-distribution-truststoreconfig-ignorecertificateexpiry)" : {{Boolean}},
  "[TrustStoreId](#cfn-cloudfront-distribution-truststoreconfig-truststoreid)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-truststoreconfig-syntax.yaml"></a>

```
  [AdvertiseTrustStoreCaNames](#cfn-cloudfront-distribution-truststoreconfig-advertisetruststorecanames): {{Boolean}}
  [IgnoreCertificateExpiry](#cfn-cloudfront-distribution-truststoreconfig-ignorecertificateexpiry): {{Boolean}}
  [TrustStoreId](#cfn-cloudfront-distribution-truststoreconfig-truststoreid): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-truststoreconfig-properties"></a>

`AdvertiseTrustStoreCaNames`  <a name="cfn-cloudfront-distribution-truststoreconfig-advertisetruststorecanames"></a>
The configuration to use to advertise trust store CA names.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IgnoreCertificateExpiry`  <a name="cfn-cloudfront-distribution-truststoreconfig-ignorecertificateexpiry"></a>
The configuration to use to ignore certificate expiration.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustStoreId`  <a name="cfn-cloudfront-distribution-truststoreconfig-truststoreid"></a>
The trust store ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
