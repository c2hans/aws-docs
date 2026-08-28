---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-originmtlsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::Distribution OriginMtlsConfig
<a name="aws-properties-cloudfront-distribution-originmtlsconfig"></a>

Configures mutual TLS authentication between CloudFront and your origin server.

## Syntax
<a name="aws-properties-cloudfront-distribution-originmtlsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distribution-originmtlsconfig-syntax.json"></a>

```
{
  "[ClientCertificateArn](#cfn-cloudfront-distribution-originmtlsconfig-clientcertificatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distribution-originmtlsconfig-syntax.yaml"></a>

```
  [ClientCertificateArn](#cfn-cloudfront-distribution-originmtlsconfig-clientcertificatearn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distribution-originmtlsconfig-properties"></a>

`ClientCertificateArn`  <a name="cfn-cloudfront-distribution-originmtlsconfig-clientcertificatearn"></a>
The Amazon Resource Name (ARN) of the client certificate stored in AWS Certificate Manager (ACM) that CloudFront uses to authenticate with your origin using Mutual TLS.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
