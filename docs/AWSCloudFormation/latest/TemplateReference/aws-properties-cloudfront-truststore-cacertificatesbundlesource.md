---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-truststore-cacertificatesbundlesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::TrustStore CaCertificatesBundleSource
<a name="aws-properties-cloudfront-truststore-cacertificatesbundlesource"></a>

A CA certificates bundle source.

## Syntax
<a name="aws-properties-cloudfront-truststore-cacertificatesbundlesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-truststore-cacertificatesbundlesource-syntax.json"></a>

```
{
  "[CaCertificatesBundleS3Location](#cfn-cloudfront-truststore-cacertificatesbundlesource-cacertificatesbundles3location)" : {{CaCertificatesBundleS3Location}}
}
```

### YAML
<a name="aws-properties-cloudfront-truststore-cacertificatesbundlesource-syntax.yaml"></a>

```
  [CaCertificatesBundleS3Location](#cfn-cloudfront-truststore-cacertificatesbundlesource-cacertificatesbundles3location): {{
    CaCertificatesBundleS3Location}}
```

## Properties
<a name="aws-properties-cloudfront-truststore-cacertificatesbundlesource-properties"></a>

`CaCertificatesBundleS3Location`  <a name="cfn-cloudfront-truststore-cacertificatesbundlesource-cacertificatesbundles3location"></a>
The CA certificates bundle location in Amazon S3.
*Required*: Yes
*Type*: [CaCertificatesBundleS3Location](aws-properties-cloudfront-truststore-cacertificatesbundles3location.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
