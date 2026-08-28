---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-paymentcryptography-key.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PaymentCryptography::Key
<a name="aws-resource-paymentcryptography-key"></a>

Creates an AWS Payment Cryptography key, a logical representation of a cryptographic key, that is unique in your account and AWS Region. You use keys for cryptographic functions such as encryption and decryption.

In addition to the key material used in cryptographic operations, an AWS Payment Cryptography key includes metadata such as the key ARN, key usage, key origin, creation date, description, and key state.

When you create a key, you specify both immutable and mutable data about the key. The immutable data contains key attributes that define the scope and cryptographic operations that you can perform using the key, for example key class (example: `SYMMETRIC_KEY`), key algorithm (example: `TDES_2KEY`), key usage (example: `TR31_P0_PIN_ENCRYPTION_KEY`) and key modes of use (example: `Encrypt`). AWS Payment Cryptography binds key attributes to keys using key blocks when you store or export them. AWS Payment Cryptography stores the key contents wrapped and never stores or transmits them in the clear.

For information about valid combinations of key attributes, see [Understanding key attributes](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html) in the *AWS Payment Cryptography User Guide*. The mutable data contained within a key includes usage timestamp and key deletion timestamp and can be modified after creation.

You can use the `CreateKey` operation to generate an ECC (Elliptic Curve Cryptography) key pair used for establishing an ECDH (Elliptic Curve Diffie-Hellman) key agreement between two parties. In the ECDH key agreement process, both parties generate their own ECC key pair with key usage K3 and exchange the public keys. Each party then use their private key, the received public key from the other party, and the key derivation parameters including key derivation function, hash algorithm, derivation data, and key algorithm to derive a shared key.

To maintain the single-use principle of cryptographic keys in payments, ECDH derived keys should not be used for multiple purposes, such as a `TR31_P0_PIN_ENCRYPTION_KEY` and `TR31_K1_KEY_BLOCK_PROTECTION_KEY`. When creating ECC key pairs in AWS Payment Cryptography you can optionally set the `DeriveKeyUsage` parameter, which defines the key usage bound to the symmetric key that will be derived using the ECC key pair.

**Cross-account use**: This operation can't be used across different AWS accounts.

 **Related operations:**
+  [DeleteKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html)
+  [GetKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html)
+  [ListKeys](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html)

## Syntax
<a name="aws-resource-paymentcryptography-key-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-paymentcryptography-key-syntax.json"></a>

```
{
  "Type" : "AWS::PaymentCryptography::Key",
  "Properties" : {
      "[DeriveKeyUsage](#cfn-paymentcryptography-key-derivekeyusage)" : {{String}},
      "[Enabled](#cfn-paymentcryptography-key-enabled)" : {{Boolean}},
      "[Exportable](#cfn-paymentcryptography-key-exportable)" : {{Boolean}},
      "[KeyAttributes](#cfn-paymentcryptography-key-keyattributes)" : {{KeyAttributes}},
      "[KeyCheckValueAlgorithm](#cfn-paymentcryptography-key-keycheckvaluealgorithm)" : {{String}},
      "[Policy](#cfn-paymentcryptography-key-policy)" : {{String}},
      "[ReplicationRegions](#cfn-paymentcryptography-key-replicationregions)" : {{[ String, ... ]}},
      "[Tags](#cfn-paymentcryptography-key-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-paymentcryptography-key-syntax.yaml"></a>

```
Type: AWS::PaymentCryptography::Key
Properties:
  [DeriveKeyUsage](#cfn-paymentcryptography-key-derivekeyusage): {{String}}
  [Enabled](#cfn-paymentcryptography-key-enabled): {{Boolean}}
  [Exportable](#cfn-paymentcryptography-key-exportable): {{Boolean}}
  [KeyAttributes](#cfn-paymentcryptography-key-keyattributes): {{
    KeyAttributes}}
  [KeyCheckValueAlgorithm](#cfn-paymentcryptography-key-keycheckvaluealgorithm): {{String}}
  [Policy](#cfn-paymentcryptography-key-policy): {{String}}
  [ReplicationRegions](#cfn-paymentcryptography-key-replicationregions): {{
    - String}}
  [Tags](#cfn-paymentcryptography-key-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-paymentcryptography-key-properties"></a>

`DeriveKeyUsage`  <a name="cfn-paymentcryptography-key-derivekeyusage"></a>
The cryptographic usage of an ECDH derived key as deﬁned in section A.5.2 of the TR-31 spec.
*Required*: No
*Type*: String
*Allowed values*: `TR31_B0_BASE_DERIVATION_KEY | TR31_C0_CARD_VERIFICATION_KEY | TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY | TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS | TR31_E1_EMV_MKEY_CONFIDENTIALITY | TR31_E2_EMV_MKEY_INTEGRITY | TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS | TR31_E5_EMV_MKEY_CARD_PERSONALIZATION | TR31_E6_EMV_MKEY_OTHER | TR31_K0_KEY_ENCRYPTION_KEY | TR31_K1_KEY_BLOCK_PROTECTION_KEY | TR31_M3_ISO_9797_3_MAC_KEY | TR31_M1_ISO_9797_1_MAC_KEY | TR31_M6_ISO_9797_5_CMAC_KEY | TR31_M7_HMAC_KEY | TR31_P0_PIN_ENCRYPTION_KEY | TR31_P1_PIN_GENERATION_KEY | TR31_V1_IBM3624_PIN_VERIFICATION_KEY | TR31_V2_VISA_PIN_VERIFICATION_KEY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-paymentcryptography-key-enabled"></a>
Specifies whether the key is enabled.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exportable`  <a name="cfn-paymentcryptography-key-exportable"></a>
Specifies whether the key is exportable. This data is immutable after the key is created.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyAttributes`  <a name="cfn-paymentcryptography-key-keyattributes"></a>
The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.
*Required*: Yes
*Type*: [KeyAttributes](aws-properties-paymentcryptography-key-keyattributes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyCheckValueAlgorithm`  <a name="cfn-paymentcryptography-key-keycheckvaluealgorithm"></a>
The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.
For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.
*Required*: No
*Type*: String
*Allowed values*: `CMAC | ANSI_X9_24 | HMAC | SHA_1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Policy`  <a name="cfn-paymentcryptography-key-policy"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\u0009\u000A\u000D\u0020-\u00FF]+$`
*Minimum*: `1`
*Maximum*: `20480`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationRegions`  <a name="cfn-paymentcryptography-key-replicationregions"></a>
The list of AWS Regions to remove from the key's replication configuration.
The key will no longer be available for cryptographic operations in these regions after removal. Ensure no active operations depend on the key in these regions before removal.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-paymentcryptography-key-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-paymentcryptography-key-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-paymentcryptography-key-return-values"></a>

### Ref
<a name="aws-resource-paymentcryptography-key-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-paymentcryptography-key-return-values-fn--getatt"></a>

####
<a name="aws-resource-paymentcryptography-key-return-values-fn--getatt-fn--getatt"></a>

`KeyIdentifier`  <a name="KeyIdentifier-fn::getatt"></a>
Property description not available.

`KeyOrigin`  <a name="KeyOrigin-fn::getatt"></a>
The source of the key material. For keys created within AWS Payment Cryptography, the value is `AWS_PAYMENT_CRYPTOGRAPHY`. For keys imported into AWS Payment Cryptography, the value is `EXTERNAL`.

`KeyState`  <a name="KeyState-fn::getatt"></a>
The state of key that is being created or deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
