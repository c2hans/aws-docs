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
