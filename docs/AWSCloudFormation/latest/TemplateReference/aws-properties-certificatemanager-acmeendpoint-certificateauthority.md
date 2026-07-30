---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-certificatemanager-acmeendpoint-certificateauthority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CertificateManager::AcmeEndpoint CertificateAuthority
<a name="aws-properties-certificatemanager-acmeendpoint-certificateauthority"></a>

Defines the certificate authority to use for an ACME endpoint.

## Syntax
<a name="aws-properties-certificatemanager-acmeendpoint-certificateauthority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-certificatemanager-acmeendpoint-certificateauthority-syntax.json"></a>

```
{
  "[PublicCertificateAuthority](#cfn-certificatemanager-acmeendpoint-certificateauthority-publiccertificateauthority)" : {{PublicCertificateAuthority}}
}
```

### YAML
<a name="aws-properties-certificatemanager-acmeendpoint-certificateauthority-syntax.yaml"></a>

```
  [PublicCertificateAuthority](#cfn-certificatemanager-acmeendpoint-certificateauthority-publiccertificateauthority): {{
    PublicCertificateAuthority}}
```

## Properties
<a name="aws-properties-certificatemanager-acmeendpoint-certificateauthority-properties"></a>

`PublicCertificateAuthority`  <a name="cfn-certificatemanager-acmeendpoint-certificateauthority-publiccertificateauthority"></a>
Configuration for using a public certificate authority.
*Required*: Yes
*Type*: [PublicCertificateAuthority](aws-properties-certificatemanager-acmeendpoint-publiccertificateauthority.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
