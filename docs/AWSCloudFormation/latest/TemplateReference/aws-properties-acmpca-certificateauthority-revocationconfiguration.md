---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-revocationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority RevocationConfiguration
<a name="aws-properties-acmpca-certificateauthority-revocationconfiguration"></a>

Certificate revocation information used by the [CreateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) and [UpdateCertificateAuthority](https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html) actions. Your private certificate authority (CA) can configure Online Certificate Status Protocol (OCSP) support and/or maintain a certificate revocation list (CRL). OCSP returns validation information about certificates as requested by clients, and a CRL contains an updated list of certificates revoked by your CA. For more information, see [RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html) in the *AWS Private CA API Reference* and [Setting up a certificate revocation method](https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html) in the *AWS Private CA User Guide*.

The following requirements and constraints apply to revocation configurations.
+ A configuration disabling CRLs or OCSP must contain only the `Enabled=False` parameter, and will fail if other parameters such as `CustomCname` or `ExpirationInDays` are included.
+ In a CRL configuration, the `S3BucketName` parameter must conform to the [Amazon S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
+ A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to [RFC2396](https://www.ietf.org/rfc/rfc2396.txt) restrictions on the use of special characters in a CNAME.
+ In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".
+ To revoke a certificate, delete the resource from your template, and call the AWS Private CA[RevokeCertificate](https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html) API and specify the resource's certificate authority ARN.

## Syntax
<a name="aws-properties-acmpca-certificateauthority-revocationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-revocationconfiguration-syntax.json"></a>

```
{
  "[CrlConfiguration](#cfn-acmpca-certificateauthority-revocationconfiguration-crlconfiguration)" : {{CrlConfiguration}},
  "[OcspConfiguration](#cfn-acmpca-certificateauthority-revocationconfiguration-ocspconfiguration)" : {{OcspConfiguration}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-revocationconfiguration-syntax.yaml"></a>

```
  [CrlConfiguration](#cfn-acmpca-certificateauthority-revocationconfiguration-crlconfiguration): {{
    CrlConfiguration}}
  [OcspConfiguration](#cfn-acmpca-certificateauthority-revocationconfiguration-ocspconfiguration): {{
    OcspConfiguration}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-revocationconfiguration-properties"></a>

`CrlConfiguration`  <a name="cfn-acmpca-certificateauthority-revocationconfiguration-crlconfiguration"></a>
Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
*Required*: No
*Type*: [CrlConfiguration](aws-properties-acmpca-certificateauthority-crlconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OcspConfiguration`  <a name="cfn-acmpca-certificateauthority-revocationconfiguration-ocspconfiguration"></a>
Configuration of Online Certificate Status Protocol (OCSP) support, if any, maintained by your private CA.
*Required*: No
*Type*: [OcspConfiguration](aws-properties-acmpca-certificateauthority-ocspconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
