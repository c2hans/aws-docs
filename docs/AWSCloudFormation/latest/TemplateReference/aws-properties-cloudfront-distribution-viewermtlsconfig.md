---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-viewermtlsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution ViewerMtlsConfig
<a name="aws-properties-cloudfront-distribution-viewermtlsconfig"></a>

A viewer mTLS configuration.

## Syntax
<a name="aws-properties-cloudfront-distribution-viewermtlsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-viewermtlsconfig-syntax.json"></a>

```
{
  "[Mode](#cfn-cloudfront-distribution-viewermtlsconfig-mode)" : {{String}},
  "[TrustStoreConfig](#cfn-cloudfront-distribution-viewermtlsconfig-truststoreconfig)" : {{TrustStoreConfig}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-viewermtlsconfig-syntax.yaml"></a>

```
  [Mode](#cfn-cloudfront-distribution-viewermtlsconfig-mode): {{String}}
  [TrustStoreConfig](#cfn-cloudfront-distribution-viewermtlsconfig-truststoreconfig): {{
    TrustStoreConfig}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-viewermtlsconfig-properties"></a>

`Mode`  <a name="cfn-cloudfront-distribution-viewermtlsconfig-mode"></a>
The viewer mTLS mode.
*Required*: No
*Type*: String
*Allowed values*: `required | optional | passthrough`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrustStoreConfig`  <a name="cfn-cloudfront-distribution-viewermtlsconfig-truststoreconfig"></a>
The trust store configuration associated with the viewer mTLS configuration.
*Required*: No
*Type*: [TrustStoreConfig](aws-properties-cloudfront-distribution-truststoreconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
