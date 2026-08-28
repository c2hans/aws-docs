---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_KeyMetadata.html
---

# KeyMetadata
<a name="API_KeyMetadata"></a>

Contains metadata about a KMS key.

This data type is used as a response element for the [CreateKey](API_CreateKey.md), [DescribeKey](API_DescribeKey.md), and [ReplicateKey](API_ReplicateKey.md) operations.

## Contents
<a name="API_KeyMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** KeyId **   <a name="KMS-Type-KeyMetadata-KeyId"></a>
The globally unique identifier for the KMS key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** Arn **   <a name="KMS-Type-KeyMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the KMS key. For examples, see [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms) in the Example ARNs section of the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** AWSAccountId **   <a name="KMS-Type-KeyMetadata-AWSAccountId"></a>
The twelve-digit account ID of the AWS account that owns the KMS key.
Type: String
Required: No

 ** CloudHsmClusterId **   <a name="KMS-Type-KeyMetadata-CloudHsmClusterId"></a>
The cluster ID of the AWS CloudHSM cluster that contains the key material for the KMS key. When you create a KMS key in an AWS CloudHSM [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html), AWS KMS creates the key material for the KMS key in the associated AWS CloudHSM cluster. This field is present only when the KMS key is created in an AWS CloudHSM key store.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 24.
Pattern: `cluster-[2-7a-zA-Z]{11,16}`
Required: No

 ** CreationDate **   <a name="KMS-Type-KeyMetadata-CreationDate"></a>
The date and time when the KMS key was created.
Type: Timestamp
Required: No

 ** CurrentKeyMaterialId **   <a name="KMS-Type-KeyMetadata-CurrentKeyMaterialId"></a>
Identifies the current key material. This value is present for symmetric encryption keys with `AWS_KMS` or `EXTERNAL` origin. These KMS keys support automatic or on-demand key rotation and can have multiple key materials associated with them. AWS KMS uses the current key material for both encryption and decryption, and the non-current key material for decryption operations only.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `^[a-f0-9]+$`
Required: No

 ** CustomerMasterKeySpec **   <a name="KMS-Type-KeyMetadata-CustomerMasterKeySpec"></a>
 *This member has been deprecated.*
Instead, use the `KeySpec` field.
The `KeySpec` and `CustomerMasterKeySpec` fields have the same value. We recommend that you use the `KeySpec` field in your code. However, to avoid breaking changes, AWS KMS supports both fields.
Type: String
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SYMMETRIC_DEFAULT | HMAC_224 | HMAC_256 | HMAC_384 | HMAC_512 | SM2`
Required: No

 ** CustomKeyStoreId **   <a name="KMS-Type-KeyMetadata-CustomKeyStoreId"></a>
A unique identifier for the [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) that contains the KMS key. This field is present only when the KMS key is created in a custom key store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** DeletionDate **   <a name="KMS-Type-KeyMetadata-DeletionDate"></a>
The date and time after which AWS KMS deletes this KMS key. This value is present only when the KMS key is scheduled for deletion, that is, when its `KeyState` is `PendingDeletion`.
When the primary key in a multi-Region key is scheduled for deletion but still has replica keys, its key state is `PendingReplicaDeletion` and the length of its waiting period is displayed in the `PendingDeletionWindowInDays` field.
Type: Timestamp
Required: No

 ** Description **   <a name="KMS-Type-KeyMetadata-Description"></a>
The description of the KMS key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** Enabled **   <a name="KMS-Type-KeyMetadata-Enabled"></a>
Specifies whether the KMS key is enabled. When `KeyState` is `Enabled` this value is true, otherwise it is false.
Type: Boolean
Required: No

 ** EncryptionAlgorithms **   <a name="KMS-Type-KeyMetadata-EncryptionAlgorithms"></a>
The encryption algorithms that the KMS key supports. You cannot use the KMS key with other encryption algorithms within AWS KMS.
This value is present only when the `KeyUsage` of the KMS key is `ENCRYPT_DECRYPT`.
Type: Array of strings
Valid Values: `SYMMETRIC_DEFAULT | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256 | SM2PKE`
Required: No

 ** ExpirationModel **   <a name="KMS-Type-KeyMetadata-ExpirationModel"></a>
Specifies whether the KMS key's key material expires. This value is present only when `Origin` is `EXTERNAL`, otherwise this value is omitted.
Type: String
Valid Values: `KEY_MATERIAL_EXPIRES | KEY_MATERIAL_DOES_NOT_EXPIRE`
Required: No

 ** KeyAgreementAlgorithms **   <a name="KMS-Type-KeyMetadata-KeyAgreementAlgorithms"></a>
The key agreement algorithm used to derive a shared secret.
Type: Array of strings
Valid Values: `ECDH`
Required: No

 ** KeyManager **   <a name="KMS-Type-KeyMetadata-KeyManager"></a>
The manager of the KMS key. KMS keys in your AWS account are either customer managed or AWS managed. For more information about the difference, see [KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) in the * AWS Key Management Service Developer Guide*.
Type: String
Valid Values: `AWS | CUSTOMER`
Required: No

 ** KeySpec **   <a name="KMS-Type-KeyMetadata-KeySpec"></a>
Describes the type of key material in the KMS key.
Type: String
Valid Values: `RSA_2048 | RSA_3072 | RSA_4096 | ECC_NIST_P256 | ECC_NIST_P384 | ECC_NIST_P521 | ECC_SECG_P256K1 | SYMMETRIC_DEFAULT | HMAC_224 | HMAC_256 | HMAC_384 | HMAC_512 | SM2 | ML_DSA_44 | ML_DSA_65 | ML_DSA_87 | ECC_NIST_EDWARDS25519`
Required: No

 ** KeyState **   <a name="KMS-Type-KeyMetadata-KeyState"></a>
The current status of the KMS key.
For more information about how key state affects the use of a KMS key, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.
Type: String
Valid Values: `Creating | Enabled | Disabled | PendingDeletion | PendingImport | PendingReplicaDeletion | Unavailable | Updating`
Required: No

 ** KeyUsage **   <a name="KMS-Type-KeyMetadata-KeyUsage"></a>
The [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations) for which you can use the KMS key.
Type: String
Valid Values: `SIGN_VERIFY | ENCRYPT_DECRYPT | GENERATE_VERIFY_MAC | KEY_AGREEMENT`
Required: No

 ** MacAlgorithms **   <a name="KMS-Type-KeyMetadata-MacAlgorithms"></a>
The message authentication code (MAC) algorithm that the HMAC KMS key supports.
This value is present only when the `KeyUsage` of the KMS key is `GENERATE_VERIFY_MAC`.
Type: Array of strings
Valid Values: `HMAC_SHA_224 | HMAC_SHA_256 | HMAC_SHA_384 | HMAC_SHA_512`
Required: No

 ** MultiRegion **   <a name="KMS-Type-KeyMetadata-MultiRegion"></a>
Indicates whether the KMS key is a multi-Region (`True`) or regional (`False`) key. This value is `True` for multi-Region primary and replica keys and `False` for regional KMS keys.
For more information about multi-Region keys, see [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** MultiRegionConfiguration **   <a name="KMS-Type-KeyMetadata-MultiRegionConfiguration"></a>
Lists the primary and replica keys in same multi-Region key. This field is present only when the value of the `MultiRegion` field is `True`.
For more information about any listed KMS key, use the [DescribeKey](API_DescribeKey.md) operation.
+  `MultiRegionKeyType` indicates whether the KMS key is a `PRIMARY` or `REPLICA` key.
+  `PrimaryKey` displays the key ARN and Region of the primary key. This field displays the current KMS key if it is the primary key.
+  `ReplicaKeys` displays the key ARNs and Regions of all replica keys. This field includes the current KMS key if it is a replica key.
Type: [MultiRegionConfiguration](API_MultiRegionConfiguration.md) object
Required: No

 ** Origin **   <a name="KMS-Type-KeyMetadata-Origin"></a>
The source of the key material for the KMS key. When this value is `AWS_KMS`, AWS KMS created the key material. When this value is `EXTERNAL`, the key material was imported or the KMS key doesn't have any key material. When this value is `AWS_CLOUDHSM`, the key material was created in the AWS CloudHSM cluster associated with a custom key store.
Type: String
Valid Values: `AWS_KMS | EXTERNAL | AWS_CLOUDHSM | EXTERNAL_KEY_STORE`
Required: No

 ** PendingDeletionWindowInDays **   <a name="KMS-Type-KeyMetadata-PendingDeletionWindowInDays"></a>
The waiting period before the primary key in a multi-Region key is deleted. This waiting period begins when the last of its replica keys is deleted. This value is present only when the `KeyState` of the KMS key is `PendingReplicaDeletion`. That indicates that the KMS key is the primary key in a multi-Region key, it is scheduled for deletion, and it still has existing replica keys.
When a single-Region KMS key or a multi-Region replica key is scheduled for deletion, its deletion date is displayed in the `DeletionDate` field. However, when the primary key in a multi-Region key is scheduled for deletion, its waiting period doesn't begin until all of its replica keys are deleted. This value displays that waiting period. When the last replica key in the multi-Region key is deleted, the `KeyState` of the scheduled primary key changes from `PendingReplicaDeletion` to `PendingDeletion` and the deletion date appears in the `DeletionDate` field.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 365.
Required: No

 ** SigningAlgorithms **   <a name="KMS-Type-KeyMetadata-SigningAlgorithms"></a>
The signing algorithms that the KMS key supports. You cannot use the KMS key with other signing algorithms within AWS KMS.
This field appears only when the `KeyUsage` of the KMS key is `SIGN_VERIFY`.
Type: Array of strings
Valid Values: `RSASSA_PSS_SHA_256 | RSASSA_PSS_SHA_384 | RSASSA_PSS_SHA_512 | RSASSA_PKCS1_V1_5_SHA_256 | RSASSA_PKCS1_V1_5_SHA_384 | RSASSA_PKCS1_V1_5_SHA_512 | ECDSA_SHA_256 | ECDSA_SHA_384 | ECDSA_SHA_512 | SM2DSA | ML_DSA_SHAKE_256 | ED25519_SHA_512 | ED25519_PH_SHA_512`
Required: No

 ** ValidTo **   <a name="KMS-Type-KeyMetadata-ValidTo"></a>
The earliest time at which any imported key material permanently associated with this KMS key expires. When a key material expires, AWS KMS deletes the key material and the KMS key becomes unusable. This value is present only for KMS keys whose `Origin` is `EXTERNAL` and the `ExpirationModel` is `KEY_MATERIAL_EXPIRES`, otherwise this value is omitted.
Type: Timestamp
Required: No

 ** XksKeyConfiguration **   <a name="KMS-Type-KeyMetadata-XksKeyConfiguration"></a>
Information about the external key that is associated with a KMS key in an external key store.
For more information, see [External key](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-external-key) in the * AWS Key Management Service Developer Guide*.
Type: [XksKeyConfigurationType](API_XksKeyConfigurationType.md) object
Required: No

## See Also
<a name="API_KeyMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/KeyMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/KeyMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/KeyMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
