---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-otaupdate-customcodesigning.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::OTAUpdate CustomCodeSigning
<a name="aws-properties-iot-otaupdate-customcodesigning"></a>

Describes a custom method used to code sign a file.

## Syntax
<a name="aws-properties-iot-otaupdate-customcodesigning-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-otaupdate-customcodesigning-syntax.json"></a>

```
{
  "[CertificateChain](#cfn-iot-otaupdate-customcodesigning-certificatechain)" : {{CodeSigningCertificateChain}},
  "[HashAlgorithm](#cfn-iot-otaupdate-customcodesigning-hashalgorithm)" : {{String}},
  "[Signature](#cfn-iot-otaupdate-customcodesigning-signature)" : {{CodeSigningSignature}},
  "[SignatureAlgorithm](#cfn-iot-otaupdate-customcodesigning-signaturealgorithm)" : {{String}}
}
```

### YAML
<a name="aws-properties-iot-otaupdate-customcodesigning-syntax.yaml"></a>

```
  [CertificateChain](#cfn-iot-otaupdate-customcodesigning-certificatechain): {{
    CodeSigningCertificateChain}}
  [HashAlgorithm](#cfn-iot-otaupdate-customcodesigning-hashalgorithm): {{String}}
  [Signature](#cfn-iot-otaupdate-customcodesigning-signature): {{
    CodeSigningSignature}}
  [SignatureAlgorithm](#cfn-iot-otaupdate-customcodesigning-signaturealgorithm): {{String}}
```

## Properties
<a name="aws-properties-iot-otaupdate-customcodesigning-properties"></a>

`CertificateChain`  <a name="cfn-iot-otaupdate-customcodesigning-certificatechain"></a>
The certificate chain.
*Required*: No
*Type*: [CodeSigningCertificateChain](aws-properties-iot-otaupdate-codesigningcertificatechain.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HashAlgorithm`  <a name="cfn-iot-otaupdate-customcodesigning-hashalgorithm"></a>
The hash algorithm used to code sign the file. You can use a string as the algorithm name if the target over-the-air (OTA) update devices are able to verify the signature that was generated using the same signature algorithm. For example, FreeRTOS uses `SHA256` or `SHA1`, so you can pass either of them based on which was used for generating the signature.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Signature`  <a name="cfn-iot-otaupdate-customcodesigning-signature"></a>
The signature for the file.
*Required*: No
*Type*: [CodeSigningSignature](aws-properties-iot-otaupdate-codesigningsignature.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SignatureAlgorithm`  <a name="cfn-iot-otaupdate-customcodesigning-signaturealgorithm"></a>
The signature algorithm used to code sign the file. You can use a string as the algorithm name if the target over-the-air (OTA) update devices are able to verify the signature that was generated using the same signature algorithm. For example, FreeRTOS uses `ECDSA` or `RSA`, so you can pass either of them based on which was used for generating the signature.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
