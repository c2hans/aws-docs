---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-codesigningcertificatechain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate CodeSigningCertificateChain
<a name="aws-properties-iot-otaupdate-codesigningcertificatechain"></a>

Describes the certificate chain being used when code signing a file.

## Syntax
<a name="aws-properties-iot-otaupdate-codesigningcertificatechain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-codesigningcertificatechain-syntax.json"></a>

```
{
  "[CertificateName](#cfn-iot-otaupdate-codesigningcertificatechain-certificatename)" : {{String}},
  "[InlineDocument](#cfn-iot-otaupdate-codesigningcertificatechain-inlinedocument)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-codesigningcertificatechain-syntax.yaml"></a>

```
  [CertificateName](#cfn-iot-otaupdate-codesigningcertificatechain-certificatename): {{String}}
  [InlineDocument](#cfn-iot-otaupdate-codesigningcertificatechain-inlinedocument): {{String}}
```

## Properties
<a name="aws-properties-iot-otaupdate-codesigningcertificatechain-properties"></a>

`CertificateName`  <a name="cfn-iot-otaupdate-codesigningcertificatechain-certificatename"></a>
The name of the certificate.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InlineDocument`  <a name="cfn-iot-otaupdate-codesigningcertificatechain-inlinedocument"></a>
A base64 encoded binary representation of the code signing certificate chain.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
