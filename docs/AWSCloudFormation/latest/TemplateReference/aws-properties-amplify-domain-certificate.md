---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amplify-domain-certificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Amplify::Domain Certificate
<a name="aws-properties-amplify-domain-certificate"></a>

Describes the SSL/TLS certificate for the domain association. This can be your own custom certificate or the default certificate that Amplify provisions for you.

If you are updating your domain to use a different certificate, `Certificate` points to the new certificate that is being created instead of the current active certificate. Otherwise, `Certificate` points to the current active certificate.

## Syntax
<a name="aws-properties-amplify-domain-certificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amplify-domain-certificate-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-amplify-domain-certificate-certificatearn)" : {{String}},
  "[CertificateType](#cfn-amplify-domain-certificate-certificatetype)" : {{String}},
  "[CertificateVerificationDNSRecord](#cfn-amplify-domain-certificate-certificateverificationdnsrecord)" : {{String}}
}
```

### YAML
<a name="aws-properties-amplify-domain-certificate-syntax.yaml"></a>

```
  [CertificateArn](#cfn-amplify-domain-certificate-certificatearn): {{String}}
  [CertificateType](#cfn-amplify-domain-certificate-certificatetype): {{String}}
  [CertificateVerificationDNSRecord](#cfn-amplify-domain-certificate-certificateverificationdnsrecord): {{String}}
```

## Properties
<a name="aws-properties-amplify-domain-certificate-properties"></a>

`CertificateArn`  <a name="cfn-amplify-domain-certificate-certificatearn"></a>
The Amazon resource name (ARN) for a custom certificate that you have already added to AWS Certificate Manager in your AWS account.
This field is required only when the certificate type is `CUSTOM`.
*Required*: No
*Type*: String
*Pattern*: `"^arn:aws:acm:[a-z0-9-]+:\d{12}:certificate\/.+$"`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateType`  <a name="cfn-amplify-domain-certificate-certificatetype"></a>
The type of SSL/TLS certificate that you want to use.
Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.
Specify `CUSTOM` to use your own certificate that you have already added to AWS Certificate Manager in your AWS account. Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide*.
*Required*: No
*Type*: String
*Allowed values*: `AMPLIFY_MANAGED | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CertificateVerificationDNSRecord`  <a name="cfn-amplify-domain-certificate-certificateverificationdnsrecord"></a>
The DNS record for certificate verification.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
