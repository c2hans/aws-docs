---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-domain-certificatesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Domain CertificateSettings
<a name="aws-properties-amplify-domain-certificatesettings"></a>

The type of SSL/TLS certificate to use for your custom domain. If a certificate type isn't specified, Amplify uses the default `AMPLIFY_MANAGED` certificate.

## Syntax
<a name="aws-properties-amplify-domain-certificatesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-domain-certificatesettings-syntax.json"></a>

```
{
  "[CertificateType](#cfn-amplify-domain-certificatesettings-certificatetype)" : {{String}},
  "[CustomCertificateArn](#cfn-amplify-domain-certificatesettings-customcertificatearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-domain-certificatesettings-syntax.yaml"></a>

```
  [CertificateType](#cfn-amplify-domain-certificatesettings-certificatetype): {{String}}
  [CustomCertificateArn](#cfn-amplify-domain-certificatesettings-customcertificatearn): {{String}}
```

## Properties
<a name="aws-properties-amplify-domain-certificatesettings-properties"></a>

`CertificateType`  <a name="cfn-amplify-domain-certificatesettings-certificatetype"></a>
The certificate type.
Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.
Specify `CUSTOM` to use your own certificate that you have already added to AWS Certificate Manager in your AWS account. Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide*.
*Required*: No
*Type*: String
*Allowed values*: `AMPLIFY_MANAGED | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomCertificateArn`  <a name="cfn-amplify-domain-certificatesettings-customcertificatearn"></a>
The Amazon resource name (ARN) for the custom certificate that you have already added to AWS Certificate Manager in your AWS account.
This field is required only when the certificate type is `CUSTOM`.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws:acm:[a-z0-9-]+:\d{12}:certificate\/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
