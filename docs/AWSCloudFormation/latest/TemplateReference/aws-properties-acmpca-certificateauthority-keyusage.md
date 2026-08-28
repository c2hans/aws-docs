---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificateauthority-keyusage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::CertificateAuthority KeyUsage
<a name="aws-properties-acmpca-certificateauthority-keyusage"></a>

Defines one or more purposes for which the key contained in the certificate can be used. Default value for each option is false.

## Syntax
<a name="aws-properties-acmpca-certificateauthority-keyusage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificateauthority-keyusage-syntax.json"></a>

```
{
  "[CRLSign](#cfn-acmpca-certificateauthority-keyusage-crlsign)" : {{Boolean}},
  "[DataEncipherment](#cfn-acmpca-certificateauthority-keyusage-dataencipherment)" : {{Boolean}},
  "[DecipherOnly](#cfn-acmpca-certificateauthority-keyusage-decipheronly)" : {{Boolean}},
  "[DigitalSignature](#cfn-acmpca-certificateauthority-keyusage-digitalsignature)" : {{Boolean}},
  "[EncipherOnly](#cfn-acmpca-certificateauthority-keyusage-encipheronly)" : {{Boolean}},
  "[KeyAgreement](#cfn-acmpca-certificateauthority-keyusage-keyagreement)" : {{Boolean}},
  "[KeyCertSign](#cfn-acmpca-certificateauthority-keyusage-keycertsign)" : {{Boolean}},
  "[KeyEncipherment](#cfn-acmpca-certificateauthority-keyusage-keyencipherment)" : {{Boolean}},
  "[NonRepudiation](#cfn-acmpca-certificateauthority-keyusage-nonrepudiation)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-acmpca-certificateauthority-keyusage-syntax.yaml"></a>

```
  [CRLSign](#cfn-acmpca-certificateauthority-keyusage-crlsign): {{Boolean}}
  [DataEncipherment](#cfn-acmpca-certificateauthority-keyusage-dataencipherment): {{Boolean}}
  [DecipherOnly](#cfn-acmpca-certificateauthority-keyusage-decipheronly): {{Boolean}}
  [DigitalSignature](#cfn-acmpca-certificateauthority-keyusage-digitalsignature): {{Boolean}}
  [EncipherOnly](#cfn-acmpca-certificateauthority-keyusage-encipheronly): {{Boolean}}
  [KeyAgreement](#cfn-acmpca-certificateauthority-keyusage-keyagreement): {{Boolean}}
  [KeyCertSign](#cfn-acmpca-certificateauthority-keyusage-keycertsign): {{Boolean}}
  [KeyEncipherment](#cfn-acmpca-certificateauthority-keyusage-keyencipherment): {{Boolean}}
  [NonRepudiation](#cfn-acmpca-certificateauthority-keyusage-nonrepudiation): {{Boolean}}
```

## Properties
<a name="aws-properties-acmpca-certificateauthority-keyusage-properties"></a>

`CRLSign`  <a name="cfn-acmpca-certificateauthority-keyusage-crlsign"></a>
Key can be used to sign CRLs.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataEncipherment`  <a name="cfn-acmpca-certificateauthority-keyusage-dataencipherment"></a>
Key can be used to decipher data.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DecipherOnly`  <a name="cfn-acmpca-certificateauthority-keyusage-decipheronly"></a>
Key can be used only to decipher data.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DigitalSignature`  <a name="cfn-acmpca-certificateauthority-keyusage-digitalsignature"></a>
 Key can be used for digital signing.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncipherOnly`  <a name="cfn-acmpca-certificateauthority-keyusage-encipheronly"></a>
Key can be used only to encipher data.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KeyAgreement`  <a name="cfn-acmpca-certificateauthority-keyusage-keyagreement"></a>
Key can be used in a key-agreement protocol.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KeyCertSign`  <a name="cfn-acmpca-certificateauthority-keyusage-keycertsign"></a>
Key can be used to sign certificates.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KeyEncipherment`  <a name="cfn-acmpca-certificateauthority-keyusage-keyencipherment"></a>
Key can be used to encipher data.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NonRepudiation`  <a name="cfn-acmpca-certificateauthority-keyusage-nonrepudiation"></a>
Key can be used for non-repudiation.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
