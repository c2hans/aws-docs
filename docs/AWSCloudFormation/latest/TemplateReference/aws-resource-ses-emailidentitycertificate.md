---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-emailidentitycertificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::EmailIdentityCertificate
<a name="aws-resource-ses-emailidentitycertificate"></a>

<a name="aws-resource-ses-emailidentitycertificate-description"></a>The `AWS::SES::EmailIdentityCertificate` resource Property description not available. for SES.

## Syntax
<a name="aws-resource-ses-emailidentitycertificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-emailidentitycertificate-syntax.json"></a>

```
{
  "Type" : "AWS::SES::EmailIdentityCertificate",
  "Properties" : {
      "[CertificateArn](#cfn-ses-emailidentitycertificate-certificatearn)" : {{String}},
      "[EmailIdentity](#cfn-ses-emailidentitycertificate-emailidentity)" : {{String}},
      "[FromAddress](#cfn-ses-emailidentitycertificate-fromaddress)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ses-emailidentitycertificate-syntax.yaml"></a>

```
Type: AWS::SES::EmailIdentityCertificate
Properties:
  [CertificateArn](#cfn-ses-emailidentitycertificate-certificatearn): {{String}}
  [EmailIdentity](#cfn-ses-emailidentitycertificate-emailidentity): {{String}}
  [FromAddress](#cfn-ses-emailidentitycertificate-fromaddress): {{String}}
```

## Properties
<a name="aws-resource-ses-emailidentitycertificate-properties"></a>

`CertificateArn`  <a name="cfn-ses-emailidentitycertificate-certificatearn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate to associate with the email identity.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z0-9-]*:acm:[a-z0-9-]+:\d{12}:certificate/[^\s]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EmailIdentity`  <a name="cfn-ses-emailidentitycertificate-emailidentity"></a>
The email identity, either an email address or a domain, to associate the certificate with.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `320`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FromAddress`  <a name="cfn-ses-emailidentitycertificate-fromaddress"></a>
The email address that the certificate applies to. This value is required when the email identity is a domain, and the address must belong to that domain or one of its subdomains. When the email identity is an email address, this value is optional. If you specify it, it must exactly match the email identity.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `320`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ses-emailidentitycertificate-return-values"></a>

### Ref
<a name="aws-resource-ses-emailidentitycertificate-return-values-ref"></a>
