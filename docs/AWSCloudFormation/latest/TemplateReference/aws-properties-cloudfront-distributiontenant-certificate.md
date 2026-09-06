---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distributiontenant-certificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFront::DistributionTenant Certificate
<a name="aws-properties-cloudfront-distributiontenant-certificate"></a>

The AWS Certificate Manager (ACM) certificate associated with your distribution.

## Syntax
<a name="aws-properties-cloudfront-distributiontenant-certificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudfront-distributiontenant-certificate-syntax.json"></a>

```
{
  "[Arn](#cfn-cloudfront-distributiontenant-certificate-arn)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudfront-distributiontenant-certificate-syntax.yaml"></a>

```
  [Arn](#cfn-cloudfront-distributiontenant-certificate-arn): {{String}}
```

## Properties
<a name="aws-properties-cloudfront-distributiontenant-certificate-properties"></a>

`Arn`  <a name="cfn-cloudfront-distributiontenant-certificate-arn"></a>
The Amazon Resource Name (ARN) of the ACM certificate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
