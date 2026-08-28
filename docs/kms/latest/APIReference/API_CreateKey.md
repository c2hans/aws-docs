---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html
---

# CreateKey
<a name="API_CreateKey"></a>

Creates a unique customer managed [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms-keys) in your AWS account and Region. You can use a KMS key in cryptographic operations, such as encryption and signing. Some AWS services let you use KMS keys that you create and manage to protect your service resources.

A KMS key is a logical representation of a cryptographic key. In addition to the key material used in cryptographic operations, a KMS key includes metadata, such as the key ID, key policy, creation date, description, and key state.

Use the parameters of `CreateKey` to specify the type of KMS key, the source of its key material, its key policy, description, tags, and other properties.

**Note**
 AWS KMS has replaced the term *customer master key (CMK)* with * AWS Key Management Service key* and *KMS key*. The concept has not changed. To prevent breaking changes, AWS KMS is keeping some variations of this term.

To create different types of KMS keys, use the following guidance:

Symmetric encryption KMS key
By default, `CreateKey` creates a symmetric encryption KMS key with key material that KMS generates. This is the basic and most widely used type of KMS key, and provides the best performance.
To create a symmetric encryption KMS key, you don't need to specify any parameters. The default value for `KeySpec`, `SYMMETRIC_DEFAULT`, the default value for `KeyUsage`, `ENCRYPT_DECRYPT`, and the default value for `Origin`, `AWS_KMS`, create a symmetric encryption KMS key with KMS key material.
If you need a key for basic encryption and decryption or you are creating a KMS key to protect your resources in an AWS service, create a symmetric encryption KMS key. The key material in a symmetric encryption key never leaves AWS KMS unencrypted. You can use a symmetric encryption KMS key to encrypt and decrypt data up to 4,096 bytes, but they are typically used to generate data keys and data keys pairs. For details, see [GenerateDataKey](API_GenerateDataKey.md) and [GenerateDataKeyPair](API_GenerateDataKeyPair.md).

Asymmetric KMS keys
To create an asymmetric KMS key, use the `KeySpec` parameter to specify the type of key material in the KMS key. Then, use the `KeyUsage` parameter to determine whether the KMS key will be used to encrypt and decrypt or sign and verify. You can't change these properties after the KMS key is created.
Asymmetric KMS keys contain an RSA key pair, Elliptic Curve (ECC) key pair, ML-DSA key pair or an SM2 key pair (China Regions only). The private key in an asymmetric KMS key never leaves AWS KMS unencrypted. However, you can use the [GetPublicKey](API_GetPublicKey.md) operation to download the public key so it can be used outside of AWS KMS. Each KMS key can have only one key usage. KMS keys with RSA key pairs can be used to encrypt and decrypt data or sign and verify messages (but not both). KMS keys with NIST-standard ECC key pairs can be used to sign and verify messages or derive shared secrets (but not both). KMS keys with `ECC_SECG_P256K1` can be used only to sign and verify messages. KMS keys with ML-DSA key pairs can be used to sign and verify messages. KMS keys with SM2 key pairs (China Regions only) can be used to either encrypt and decrypt data, sign and verify messages, or derive shared secrets (you must choose one key usage type). For information about asymmetric KMS keys, see [Asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the * AWS Key Management Service Developer Guide*.

HMAC KMS key
To create an HMAC KMS key, set the `KeySpec` parameter to a key spec value for HMAC KMS keys. Then set the `KeyUsage` parameter to `GENERATE_VERIFY_MAC`. You must set the key usage even though `GENERATE_VERIFY_MAC` is the only valid key usage value for HMAC KMS keys. You can't change these properties after the KMS key is created.
HMAC KMS keys are symmetric keys that never leave AWS KMS unencrypted. You can use HMAC keys to generate ([GenerateMac](API_GenerateMac.md)) and verify ([VerifyMac](API_VerifyMac.md)) HMAC codes for messages up to 4096 bytes.

Multi-Region primary keys
To create a multi-Region *primary key* in the local AWS Region, use the `MultiRegion` parameter with a value of `True`. To create a multi-Region *replica key*, that is, a KMS key with the same key ID and key material as a primary key, but in a different AWS Region, use the [ReplicateKey](API_ReplicateKey.md) operation. To change a replica key to a primary key, and its primary key to a replica key, use the [UpdatePrimaryRegion](API_UpdatePrimaryRegion.md) operation.
You can create multi-Region KMS keys for all supported KMS key types: symmetric encryption KMS keys, HMAC KMS keys, asymmetric encryption KMS keys, and asymmetric signing KMS keys. You can also create multi-Region keys with imported key material. However, you can't create multi-Region keys in a custom key store.
This operation supports *multi-Region keys*, an AWS KMS feature that lets you create multiple interoperable KMS keys in different AWS Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them interchangeably to encrypt data in one AWS Region and decrypt it in a different AWS Region without re-encrypting the data or making a cross-Region call. For more information about multi-Region keys, see [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the * AWS Key Management Service Developer Guide*.

Imported key material
To import your own key material into a KMS key, begin by creating a KMS key with no key material. To do this, use the `Origin` parameter of `CreateKey` with a value of `EXTERNAL`. Next, use [GetParametersForImport](API_GetParametersForImport.md) operation to get a public key and import token. Use the wrapping public key to encrypt your key material. Then, use [ImportKeyMaterial](API_ImportKeyMaterial.md) with your import token to import the key material. For step-by-step instructions, see [Importing Key Material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the * * AWS Key Management Service Developer Guide* *.
You can import key material into KMS keys of all supported KMS key types: symmetric encryption KMS keys, HMAC KMS keys, asymmetric encryption KMS keys, and asymmetric signing KMS keys. You can also create multi-Region keys with imported key material. However, you can't import key material into a KMS key in a custom key store.
To create a multi-Region primary key with imported key material, use the `Origin` parameter of `CreateKey` with a value of `EXTERNAL` and the `MultiRegion` parameter with a value of `True`. To create replicas of the multi-Region primary key, use the [ReplicateKey](API_ReplicateKey.md) operation. For instructions, see [Importing key material step 1](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html ). For more information about multi-Region keys, see [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the * AWS Key Management Service Developer Guide*.

Custom key store
A [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) lets you protect your AWS resources using keys in a backing key store that you own and manage. When you request a cryptographic operation with a KMS key in a custom key store, the operation is performed in the backing key store using its cryptographic keys.
 AWS KMS supports [AWS CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html) backed by an AWS CloudHSM cluster and [external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) backed by an external key manager outside of AWS. When you create a KMS key in an AWS CloudHSM key store, AWS KMS generates an encryption key in the AWS CloudHSM cluster and associates it with the KMS key. When you create a KMS key in an external key store, you specify an existing encryption key in the external key manager.
Some external key managers provide a simpler method for creating a KMS key in an external key store. For details, see your external key manager documentation.
Before you create a KMS key in a custom key store, the `ConnectionState` of the key store must be `CONNECTED`. To connect the custom key store, use the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation. To find the `ConnectionState`, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
To create a KMS key in a custom key store, use the `CustomKeyStoreId`. Use the default `KeySpec` value, `SYMMETRIC_DEFAULT`, and the default `KeyUsage` value, `ENCRYPT_DECRYPT` to create a symmetric encryption key. No other key type is supported in a custom key store.
To create a KMS key in an [AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-cmk-keystore.html), use the `Origin` parameter with a value of `AWS_CLOUDHSM`. The AWS CloudHSM cluster that is associated with the custom key store must have at least two active HSMs in different Availability Zones in the AWS Region.
To create a KMS key in an [external key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keys.html), use the `Origin` parameter with a value of `EXTERNAL_KEY_STORE` and an `XksKeyId` parameter that identifies an existing external key.
Some external key managers provide a simpler method for creating a KMS key in an external key store. For details, see your external key manager documentation.

 **Cross-account use**: No. You cannot use this operation to create a KMS key in a different AWS account.

 **Required permissions**: [kms:CreateKey](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy). To use the `Tags` parameter, [kms:TagResource](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy). For examples and information about related permissions, see [Allow a user to create KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/customer-managed-policies.html#iam-policy-example-create-key) in the * AWS Key Management Service Developer Guide*.

 **Related operations:**
+  [DescribeKey](API_DescribeKey.md)
+  [ListKeys](API_ListKeys.md)
+  [ScheduleKeyDeletion](API_ScheduleKeyDeletion.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_CreateKey_RequestSyntax"></a>

```
{
   "BypassPolicyLockoutSafetyCheck": {{boolean}},
   "CustomerMasterKeySpec": "{{string}}",
   "CustomKeyStoreId": "{{string}}",
   "Description": "{{string}}",
   "KeySpec": "{{string}}",
   "KeyUsage": "{{string}}",
   "MultiRegion": {{boolean}},
   "Origin": "{{string}}",
   "Policy": "{{string}}",
   "Tags": [
      {
         "TagKey": "{{string}}",
         "TagValue": "{{string}}"
      }
   ],
   "XksKeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BypassPolicyLockoutSafetyCheck](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-BypassPolicyLockoutSafetyCheck"></a>
Skips ("bypasses") the key policy lockout safety check. The default value is false.
Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.
For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the * AWS Key Management Service Developer Guide*.
Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) request on the KMS key.
Type: Boolean
Required: No

 ** [CustomerMasterKeySpec](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-CustomerMasterKeySpec"></a>
 *This parameter has been deprecated.*
Instead, use the `KeySpec` parameter.
The `KeySpec` and `CustomerMasterKeySpec` parameters work the same way. Only the names differ. We recommend that you use `KeySpec` parameter in your code. However, to avoid breaking changes, AWS KMS supports both parameters.
Type: String
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SYMMETRIC_DEFAULT | HMAC_224 | HMAC_256 | HMAC_384 | HMAC_512 | SM2`
Required: No

 ** [CustomKeyStoreId](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-CustomKeyStoreId"></a>
Creates the KMS key in the specified [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html). The `ConnectionState` of the custom key store must be `CONNECTED`. To find the CustomKeyStoreID and ConnectionState use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
This parameter is valid only for symmetric encryption KMS keys in a single Region. You cannot create any other type of KMS key in a custom key store.
When you create a KMS key in an AWS CloudHSM key store, AWS KMS generates a non-exportable 256-bit symmetric key in its associated AWS CloudHSM cluster and associates it with the KMS key. When you create a KMS key in an external key store, you must use the `XksKeyId` parameter to specify an external key that serves as key material for the KMS key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [Description](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-Description"></a>
A description of the KMS key. Use a description that helps you decide whether the KMS key is appropriate for a task. The default value is an empty string (no description).
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
To set or change the description after the key is created, use [UpdateKeyDescription](API_UpdateKeyDescription.md).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** [KeySpec](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-KeySpec"></a>
Specifies the type of KMS key to create. The default value, `SYMMETRIC_DEFAULT`, creates a KMS key with a 256-bit AES-GCM key that is used for encryption and decryption, except in China Regions, where it creates a 128-bit symmetric key that uses SM4 encryption. For a detailed description of all supported key specs, see [Key spec reference](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose-key-spec.html) in the * * AWS Key Management Service Developer Guide* *.
The `KeySpec` determines whether the KMS key contains a symmetric key or an asymmetric key pair. It also determines the algorithms that the KMS key supports. You can't change the `KeySpec` after the KMS key is created. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see [kms:EncryptionAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-algorithm), [kms:MacAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-mac-algorithm), [kms:KeyAgreementAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-key-agreement-algorithm), or [kms:SigningAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-signing-algorithm) in the * * AWS Key Management Service Developer Guide* *.
 [AWS services that are integrated with AWS KMS](http://aws.amazon.com/kms/features/#AWS_Service_Integration) use symmetric encryption KMS keys to protect your data. These services do not support asymmetric KMS keys or HMAC KMS keys.
 AWS KMS supports the following key specs for KMS keys:
+ Symmetric encryption key (default)
  +  `SYMMETRIC_DEFAULT`
+ HMAC keys (symmetric)
  +  `HMAC_224`
  +  `HMAC_256`
  +  `HMAC_384`
  +  `HMAC_512`
+ Asymmetric RSA key pairs (encryption and decryption -or- signing and verification)
  +  `RSA_2048`
  +  `RSA_3072`
  +  `RSA_4096`
+ Asymmetric NIST-standard elliptic curve key pairs (signing and verification -or- deriving shared secrets)
  +  `ECC_NIST_P256` (secp256r1)
  +  `ECC_NIST_P384` (secp384r1)
  +  `ECC_NIST_P521` (secp521r1)
  +  `ECC_NIST_EDWARDS25519` (ed25519) - signing and verification only
    +  **Note:** For ECC\_NIST\_EDWARDS25519 KMS keys, the ED25519\_SHA\_512 signing algorithm requires [`MessageType:RAW`](kms/latest/APIReference/API_Sign.html#KMS-Sign-request-MessageType), while ED25519\_PH\_SHA\_512 requires [`MessageType:DIGEST`](kms/latest/APIReference/API_Sign.html#KMS-Sign-request-MessageType). These message types cannot be used interchangeably.
+ Other asymmetric elliptic curve key pairs (signing and verification)
  +  `ECC_SECG_P256K1` (secp256k1), commonly used for cryptocurrencies.
+ Asymmetric ML-DSA key pairs (signing and verification)
  +  `ML_DSA_44`
  +  `ML_DSA_65`
  +  `ML_DSA_87`
+ SM2 key pairs (encryption and decryption -or- signing and verification -or- deriving shared secrets)
  +  `SM2` (China Regions only)
Type: String
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SYMMETRIC_DEFAULT | HMAC_224 | HMAC_256 | HMAC_384 | HMAC_512 | SM2 | ML_DSA_44 | ML_DSA_65 | ML_DSA_87 | ECC_NIST_EDWARDS25519`
Required: No

 ** [KeyUsage](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-KeyUsage"></a>
Determines the [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations) for which you can use the KMS key. The default value is `ENCRYPT_DECRYPT`. This parameter is optional when you are creating a symmetric encryption KMS key; otherwise, it is required. You can't change the [`KeyUsage`](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#key-usage) value after the KMS key is created. Each AWS KMS key can have only one key usage. This follows key usage best practices according to [NIST SP 800-57 Recommendations for Key Management](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), section 5.2, Key usage.
Select only one valid value.
+ For symmetric encryption KMS keys, omit the parameter or specify `ENCRYPT_DECRYPT`.
+ For HMAC KMS keys (symmetric), specify `GENERATE_VERIFY_MAC`.
+ For asymmetric KMS keys with RSA key pairs, specify `ENCRYPT_DECRYPT` or `SIGN_VERIFY`.
+ For asymmetric KMS keys with NIST-standard elliptic curve key pairs, specify `SIGN_VERIFY` or `KEY_AGREEMENT`.
+ For asymmetric KMS keys with `ECC_SECG_P256K1` key pairs, specify `SIGN_VERIFY`.
+ For asymmetric KMS keys with ML-DSA key pairs, specify `SIGN_VERIFY`.
+ For asymmetric KMS keys with SM2 key pairs (China Regions only), specify `ENCRYPT_DECRYPT`, `SIGN_VERIFY`, or `KEY_AGREEMENT`.
Type: String
Valid Values: `SIGN_VERIFY | ENCRYPT_DECRYPT | GENERATE_VERIFY_MAC | KEY_AGREEMENT`
Required: No

 ** [MultiRegion](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-MultiRegion"></a>
Creates a multi-Region primary key that you can replicate into other AWS Regions. You cannot change this value after you create the KMS key.
For a multi-Region key, set this parameter to `True`. For a single-Region KMS key, omit this parameter or set it to `False`. The default value is `False`.
This operation supports *multi-Region keys*, an AWS KMS feature that lets you create multiple interoperable KMS keys in different AWS Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them interchangeably to encrypt data in one AWS Region and decrypt it in a different AWS Region without re-encrypting the data or making a cross-Region call. For more information about multi-Region keys, see [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the * AWS Key Management Service Developer Guide*.
This value creates a *primary key*, not a replica. To create a *replica key*, use the [ReplicateKey](API_ReplicateKey.md) operation.
You can create a symmetric or asymmetric multi-Region key, and you can create a multi-Region key with imported key material. However, you cannot create a multi-Region key in a custom key store.
Type: Boolean
Required: No

 ** [Origin](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-Origin"></a>
The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is `AWS_KMS`, which means that AWS KMS creates the key material.
To [create a KMS key with no key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html) (for imported key material), set this value to `EXTERNAL`. For more information about importing key material into AWS KMS, see [Importing Key Material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the * AWS Key Management Service Developer Guide*. The `EXTERNAL` origin value is valid only for symmetric KMS keys.
To [create a KMS key in an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-cmk-keystore.html) and create its key material in the associated AWS CloudHSM cluster, set this value to `AWS_CLOUDHSM`. You must also use the `CustomKeyStoreId` parameter to identify the AWS CloudHSM key store. The `KeySpec` value must be `SYMMETRIC_DEFAULT`.
To [create a KMS key in an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keys.html), set this value to `EXTERNAL_KEY_STORE`. You must also use the `CustomKeyStoreId` parameter to identify the external key store and the `XksKeyId` parameter to identify the associated external key. The `KeySpec` value must be `SYMMETRIC_DEFAULT`.
Type: String
Valid Values: `AWS_KMS | EXTERNAL | AWS_CLOUDHSM | EXTERNAL_KEY_STORE`
Required: No

 ** [Policy](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-Policy"></a>
The key policy to attach to the KMS key.
If you provide a key policy, it must meet the following criteria:
+ The key policy must allow the calling principal to make a subsequent `PutKeyPolicy` request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the * AWS Key Management Service Developer Guide*. (To omit this condition, set `BypassPolicyLockoutSafetyCheck` to true.)
+ Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal, you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS. For more information, see [Changes that I make are not always immediately visible](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the * AWS Identity and Access Management User Guide*.
If either of the required `Resource` or `Action` elements are missing from a key policy statement, the policy statement has no effect. When a key policy statement is missing one of these elements, the AWS KMS console correctly reports an error, but the `CreateKey` and `PutKeyPolicy` API requests succeed, even though the policy statement is ineffective.
For more information on required key policy elements, see [Elements in a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html#key-policy-elements) in the * AWS Key Management Service Developer Guide*.
If you do not provide a key policy, AWS KMS attaches a default key policy to the KMS key. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html) in the * AWS Key Management Service Developer Guide*.
If the key policy exceeds the length constraint, AWS KMS returns a `LimitExceededException`.
For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the * * AWS Identity and Access Management User Guide* *.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** [Tags](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-Tags"></a>
Assigns one or more tags to the KMS key. Use this parameter to tag the KMS key when it is created. To tag an existing KMS key, use the [TagResource](API_TagResource.md) operation.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see [ABAC for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the * AWS Key Management Service Developer Guide*.
To use this parameter, you must have [kms:TagResource](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) permission in an IAM policy.
Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You cannot have more than one tag on a KMS key with the same tag key. If you specify an existing tag key with a different tag value, AWS KMS replaces the current tag value with the specified one.
When you add tags to an AWS resource, AWS generates a cost allocation report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For details, see [Tags in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html).
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [XksKeyId](#API_CreateKey_RequestSyntax) **   <a name="KMS-CreateKey-request-XksKeyId"></a>
Identifies the [external key](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-external-key) that serves as key material for the KMS key in an [external key store](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html). Specify the ID that the [external key store proxy](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-xks-proxy) uses to refer to the external key. For help, see the documentation for your external key store proxy.
This parameter is required for a KMS key with an `Origin` value of `EXTERNAL_KEY_STORE`. It is not valid for KMS keys with any other `Origin` value.
The external key must be an existing 256-bit AES symmetric encryption key hosted outside of AWS in an external key manager associated with the external key store specified by the `CustomKeyStoreId` parameter. This key must be enabled and configured to perform encryption and decryption. Each KMS key in an external key store must use a different external key. For details, see [Requirements for a KMS key in an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keys.html#xks-key-requirements) in the * AWS Key Management Service Developer Guide*.
Each KMS key in an external key store is associated two backing keys. One is key material that AWS KMS generates. The other is the external key specified by this parameter. When you use the KMS key in an external key store to encrypt data, the encryption operation is performed first by AWS KMS using the AWS KMS key material, and then by the external key manager using the specified external key, a process known as *double encryption*. For details, see [Double encryption](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-double-encryption) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_.]+$`
Required: No

## Response Syntax
<a name="API_CreateKey_ResponseSyntax"></a>

```
{
   "KeyMetadata": {
      "Arn": "string",
      "AWSAccountId": "string",
      "CloudHsmClusterId": "string",
      "CreationDate": number,
      "CurrentKeyMaterialId": "string",
      "CustomerMasterKeySpec": "string",
      "CustomKeyStoreId": "string",
      "DeletionDate": number,
      "Description": "string",
      "Enabled": boolean,
      "EncryptionAlgorithms": [ "string" ],
      "ExpirationModel": "string",
      "KeyAgreementAlgorithms": [ "string" ],
      "KeyId": "string",
      "KeyManager": "string",
      "KeySpec": "string",
      "KeyState": "string",
      "KeyUsage": "string",
      "MacAlgorithms": [ "string" ],
      "MultiRegion": boolean,
      "MultiRegionConfiguration": {
         "MultiRegionKeyType": "string",
         "PrimaryKey": {
            "Arn": "string",
            "Region": "string"
         },
         "ReplicaKeys": [
            {
               "Arn": "string",
               "Region": "string"
            }
         ]
      },
      "Origin": "string",
      "PendingDeletionWindowInDays": number,
      "SigningAlgorithms": [ "string" ],
      "ValidTo": number,
      "XksKeyConfiguration": {
         "Id": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyMetadata](#API_CreateKey_ResponseSyntax) **   <a name="KMS-CreateKey-response-KeyMetadata"></a>
Metadata associated with the KMS key.
Type: [KeyMetadata](API_KeyMetadata.md) object

## Errors
<a name="API_CreateKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudHsmClusterInvalidConfigurationException **
The request was rejected because the associated AWS CloudHSM cluster did not meet the configuration requirements for an AWS CloudHSM key store.
+ The AWS CloudHSM cluster must be configured with private subnets in at least two different Availability Zones in the Region.
+ The [security group for the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html) (cloudhsm-cluster-*<cluster-id>*-sg) must include inbound rules and outbound rules that allow TCP traffic on ports 2223-2225. The **Source** in the inbound rules and the **Destination** in the outbound rules must match the security group ID. These rules are set by default when you create the AWS CloudHSM cluster. Do not delete or change them. To get information about a particular security group, use the [DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html) operation.
+ The AWS CloudHSM cluster must contain at least as many HSMs as the operation requires. To add HSMs, use the AWS CloudHSM [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html) operation.

  For the [CreateCustomKeyStore](API_CreateCustomKeyStore.md), [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md), and [CreateKey](#API_CreateKey) operations, the AWS CloudHSM cluster must have at least two active HSMs, each in a different Availability Zone. For the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation, the AWS CloudHSM must contain at least one active HSM.
For information about the requirements for an AWS CloudHSM cluster that is associated with an AWS CloudHSM key store, see [Assemble the Prerequisites](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore) in the * AWS Key Management Service Developer Guide*. For information about creating a private subnet for an AWS CloudHSM cluster, see [Create a Private Subnet](https://docs.aws.amazon.com/cloudhsm/latest/userguide/create-subnets.html) in the * AWS CloudHSM User Guide*. For information about cluster security groups, see [Configure a Default Security Group](https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-sg.html) in the * * AWS CloudHSM User Guide* *.
HTTP Status Code: 400

 ** CustomKeyStoreInvalidStateException **
The request was rejected because of the `ConnectionState` of the custom key store. To get the `ConnectionState` of a custom key store, use the [DescribeCustomKeyStores](API_DescribeCustomKeyStores.md) operation.
This exception is thrown under the following conditions:
+ You requested the [ConnectCustomKeyStore](API_ConnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `FAILED`. This operation is valid for all other `ConnectionState` values. To reconnect a custom key store in a `FAILED` state, disconnect it ([DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md)), then connect it (`ConnectCustomKeyStore`).
+ You requested the [CreateKey](#API_CreateKey) operation in a custom key store that is not connected. This operations is valid only when the custom key store `ConnectionState` is `CONNECTED`.
+ You requested the [DisconnectCustomKeyStore](API_DisconnectCustomKeyStore.md) operation on a custom key store with a `ConnectionState` of `DISCONNECTING` or `DISCONNECTED`. This operation is valid for all other `ConnectionState` values.
+ You requested the [UpdateCustomKeyStore](API_UpdateCustomKeyStore.md) or [DeleteCustomKeyStore](API_DeleteCustomKeyStore.md) operation on a custom key store that is not disconnected. `UpdateCustomKeyStore` can be called on a custom key store in the `CONNECTED` state only to update `NewCustomKeyStoreName`. For all other properties, the custom key store `ConnectionState` must be `DISCONNECTED`.
+ You requested the [GenerateRandom](API_GenerateRandom.md) operation in an AWS CloudHSM key store that is not connected. This operation is valid only when the AWS CloudHSM key store `ConnectionState` is `CONNECTED`.
HTTP Status Code: 400

 ** CustomKeyStoreNotFoundException **
The request was rejected because AWS KMS cannot find a custom key store with the specified key store name or ID.
HTTP Status Code: 400

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** LimitExceededException **
The request was rejected because a length constraint or quota was exceeded. For more information, see [Quotas](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the * AWS Key Management Service Developer Guide*.
HTTP Status Code: 400

 ** MalformedPolicyDocumentException **
The request was rejected because the specified policy is not syntactically or semantically correct.
HTTP Status Code: 400

 ** TagException **
The request was rejected because one or more tags are not valid.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

 ** XksKeyAlreadyInUseException **
The request was rejected because the (`XksKeyId`) is already associated with another KMS key in this external key store. Each KMS key in an external key store must be associated with a different external key.
HTTP Status Code: 400

 ** XksKeyInvalidConfigurationException **
The request was rejected because the external key specified by the `XksKeyId` parameter did not meet the configuration requirements for an external key store.
The external key must be an AES-256 symmetric key that is enabled and performs encryption and decryption.
HTTP Status Code: 400

 ** XksKeyNotFoundException **
The request was rejected because the external key store proxy could not find the external key. This exception is thrown when the value of the `XksKeyId` parameter doesn't identify a key in the external key manager associated with the external key proxy.
Verify that the `XksKeyId` represents an existing key in the external key manager. Use the key identifier that the external key store proxy uses to identify the key. For details, see the documentation provided with your external key store proxy or key manager.
HTTP Status Code: 400

## Examples
<a name="API_CreateKey_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_CreateKey_Example_1"></a>

This example illustrates one usage of CreateKey.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20170705/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=8fb59aa17854a97df47aae69f560b66178ed0b5e1ebe334be516c4f3f59acedc
X-Amz-Target: TrentService.CreateKey
X-Amz-Date: 20170705T210455Z
Content-Length: 62

{
  "Tags": [{
    "TagValue": "ExampleUser",
    "TagKey": "CreatedBy"
  }]
}
```

### Example Response
<a name="API_CreateKey_Example_2"></a>

This example illustrates one usage of CreateKey.

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 05 Jul 2017 21:04:55 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 335
Connection: keep-alive
x-amzn-RequestId: 98b2de61-61c5-11e7-bd87-9fc4a74e147b

{
  "KeyMetadata": {
    "AWSAccountId": "111122223333",
    "Arn": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "CreationDate": "2025-04-16T16:03:04.060000-07:00",
    "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
    "Description": "",
    "Enabled": true,
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "KeyManager": "CUSTOMER",
    "KeySpec": "SYMMETRIC_DEFAULT",
    "KeyState": "Enabled",
    "KeyUsage": "ENCRYPT_DECRYPT",
    "MultiRegion": false,
    "Origin": "AWS_KMS",
    "EncryptionAlgorithms": [
      "SYMMETRIC_DEFAULT"
    ],
    "CurrentKeyMaterialId": "0b7fd7ddbac6eef27907413567cad8c810e2883dc8a7534067a82ee1142fc1e6"
  }
}
```

## See Also
<a name="API_CreateKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/CreateKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/CreateKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/CreateKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/CreateKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/CreateKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/CreateKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/CreateKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/CreateKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/CreateKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/CreateKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
