---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-paymentcryptography-key-keyattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PaymentCryptography::Key KeyAttributes
<a name="aws-properties-paymentcryptography-key-keyattributes"></a>

The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.

## Syntax
<a name="aws-properties-paymentcryptography-key-keyattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-paymentcryptography-key-keyattributes-syntax.json"></a>

```
{
  "[KeyAlgorithm](#cfn-paymentcryptography-key-keyattributes-keyalgorithm)" : {{String}},
  "[KeyClass](#cfn-paymentcryptography-key-keyattributes-keyclass)" : {{String}},
  "[KeyModesOfUse](#cfn-paymentcryptography-key-keyattributes-keymodesofuse)" : {{KeyModesOfUse}},
  "[KeyUsage](#cfn-paymentcryptography-key-keyattributes-keyusage)" : {{String}}
}
```

### YAML
<a name="aws-properties-paymentcryptography-key-keyattributes-syntax.yaml"></a>

```
  [KeyAlgorithm](#cfn-paymentcryptography-key-keyattributes-keyalgorithm): {{String}}
  [KeyClass](#cfn-paymentcryptography-key-keyattributes-keyclass): {{String}}
  [KeyModesOfUse](#cfn-paymentcryptography-key-keyattributes-keymodesofuse): {{
    KeyModesOfUse}}
  [KeyUsage](#cfn-paymentcryptography-key-keyattributes-keyusage): {{String}}
```

## Properties
<a name="aws-properties-paymentcryptography-key-keyattributes-properties"></a>

`KeyAlgorithm`  <a name="cfn-paymentcryptography-key-keyattributes-keyalgorithm"></a>
The key algorithm to be use during creation of an AWS Payment Cryptography key.
For symmetric keys, AWS Payment Cryptography supports `AES` and `TDES` algorithms. For asymmetric keys, AWS Payment Cryptography supports `RSA` and `ECC_NIST` algorithms.
*Required*: Yes
*Type*: String
*Allowed values*: `TDES_2KEY | TDES_3KEY | AES_128 | AES_192 | AES_256 | HMAC_SHA256 | HMAC_SHA384 | HMAC_SHA512 | HMAC_SHA224 | RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyClass`  <a name="cfn-paymentcryptography-key-keyattributes-keyclass"></a>
The type of AWS Payment Cryptography key to create, which determines the classiﬁcation of the cryptographic method and whether AWS Payment Cryptography key contains a symmetric key or an asymmetric key pair.
*Required*: Yes
*Type*: String
*Allowed values*: `SYMMETRIC_KEY | ASYMMETRIC_KEY_PAIR | PRIVATE_KEY | PUBLIC_KEY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyModesOfUse`  <a name="cfn-paymentcryptography-key-keyattributes-keymodesofuse"></a>
The list of cryptographic operations that you can perform using the key.
*Required*: Yes
*Type*: [KeyModesOfUse](aws-properties-paymentcryptography-key-keymodesofuse.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyUsage`  <a name="cfn-paymentcryptography-key-keyattributes-keyusage"></a>
The cryptographic usage of an AWS Payment Cryptography key as deﬁned in section A.5.2 of the TR-31 spec.
*Required*: Yes
*Type*: String
*Allowed values*: `TR31_B0_BASE_DERIVATION_KEY | TR31_C0_CARD_VERIFICATION_KEY | TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY | TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION | TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS | TR31_E1_EMV_MKEY_CONFIDENTIALITY | TR31_E2_EMV_MKEY_INTEGRITY | TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS | TR31_E5_EMV_MKEY_CARD_PERSONALIZATION | TR31_E6_EMV_MKEY_OTHER | TR31_K0_KEY_ENCRYPTION_KEY | TR31_K1_KEY_BLOCK_PROTECTION_KEY | TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT | TR31_M0_ISO_16609_MAC_KEY | TR31_M3_ISO_9797_3_MAC_KEY | TR31_M1_ISO_9797_1_MAC_KEY | TR31_M6_ISO_9797_5_CMAC_KEY | TR31_M7_HMAC_KEY | TR31_P0_PIN_ENCRYPTION_KEY | TR31_P1_PIN_GENERATION_KEY | TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE | TR31_V1_IBM3624_PIN_VERIFICATION_KEY | TR31_V2_VISA_PIN_VERIFICATION_KEY | TR31_K2_TR34_ASYMMETRIC_KEY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
