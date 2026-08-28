---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_Key.html
---

# Key
<a name="API_Key"></a>

Metadata about an AWS Payment Cryptography key.

## Contents
<a name="API_Key_Contents"></a>

 ** CreateTimestamp **   <a name="paymentcryptography-Type-Key-CreateTimestamp"></a>
The date and time when the key was created.
Type: Timestamp
Required: Yes

 ** Enabled **   <a name="paymentcryptography-Type-Key-Enabled"></a>
Specifies whether the key is enabled.
Type: Boolean
Required: Yes

 ** Exportable **   <a name="paymentcryptography-Type-Key-Exportable"></a>
Specifies whether the key is exportable. This data is immutable after the key is created.
Type: Boolean
Required: Yes

 ** KeyArn **   <a name="paymentcryptography-Type-Key-KeyArn"></a>
The Amazon Resource Name (ARN) of the key.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: Yes

 ** KeyAttributes **   <a name="paymentcryptography-Type-Key-KeyAttributes"></a>
The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.
Type: [KeyAttributes](API_KeyAttributes.md) object
Required: Yes

 ** KeyCheckValue **   <a name="paymentcryptography-Type-Key-KeyCheckValue"></a>
The key check value (KCV) is used to check if all parties holding a given key have the same key or to detect that a key has changed.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** KeyCheckValueAlgorithm **   <a name="paymentcryptography-Type-Key-KeyCheckValueAlgorithm"></a>
The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.
For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result. For HMAC keys, the KCV is computed using the hash selected at key creation on a zero-length message, taking the leftmost 3 bytes.
Type: String
Valid Values: `CMAC | ANSI_X9_24 | HMAC | SHA_1`
Required: Yes

 ** KeyOrigin **   <a name="paymentcryptography-Type-Key-KeyOrigin"></a>
The source of the key material. For keys created within AWS Payment Cryptography, the value is `AWS_PAYMENT_CRYPTOGRAPHY`. For keys imported into AWS Payment Cryptography, the value is `EXTERNAL`.
Type: String
Valid Values: `EXTERNAL | AWS_PAYMENT_CRYPTOGRAPHY`
Required: Yes

 ** KeyState **   <a name="paymentcryptography-Type-Key-KeyState"></a>
The state of key that is being created or deleted.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_COMPLETE | DELETE_PENDING | DELETE_COMPLETE`
Required: Yes

 ** DeletePendingTimestamp **   <a name="paymentcryptography-Type-Key-DeletePendingTimestamp"></a>
The date and time after which AWS Payment Cryptography will delete the key. This value is present only when `KeyState` is `DELETE_PENDING` and the key is scheduled for deletion.
Type: Timestamp
Required: No

 ** DeleteTimestamp **   <a name="paymentcryptography-Type-Key-DeleteTimestamp"></a>
The date and time after which AWS Payment Cryptography will delete the key. This value is present only when when the `KeyState` is `DELETE_COMPLETE` and the AWS Payment Cryptography key is deleted.
Type: Timestamp
Required: No

 ** DeriveKeyUsage **   <a name="paymentcryptography-Type-Key-DeriveKeyUsage"></a>
The cryptographic usage of an ECDH derived key as deﬁned in section A.5.2 of the TR-31 spec.
Type: String
Valid Values: `TR31_B0_BASE_DERIVATION_KEY | TR31_C0_CARD_VERIFICATION_KEY | TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY | TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS | TR31_E1_EMV_MKEY_CONFIDENTIALITY | TR31_E2_EMV_MKEY_INTEGRITY | TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS | TR31_E5_EMV_MKEY_CARD_PERSONALIZATION | TR31_E6_EMV_MKEY_OTHER | TR31_K0_KEY_ENCRYPTION_KEY | TR31_K1_KEY_BLOCK_PROTECTION_KEY | TR31_M3_ISO_9797_3_MAC_KEY | TR31_M1_ISO_9797_1_MAC_KEY | TR31_M6_ISO_9797_5_CMAC_KEY | TR31_M7_HMAC_KEY | TR31_P0_PIN_ENCRYPTION_KEY | TR31_P1_PIN_GENERATION_KEY | TR31_V1_IBM3624_PIN_VERIFICATION_KEY | TR31_V2_VISA_PIN_VERIFICATION_KEY`
Required: No

 ** MpaStatus **   <a name="paymentcryptography-Type-Key-MpaStatus"></a>
The Multi-Party Approval (MPA) status for the key, if applicable.
Type: [MpaStatus](API_MpaStatus.md) object
Required: No

 ** MultiRegionKeyType **   <a name="paymentcryptography-Type-Key-MultiRegionKeyType"></a>
Indicates whether this key is a Multi-Region key and its role in the Multi-Region key hierarchy.
Multi-Region replication keys allow the same key material to be used across multiple AWS Regions. This field specifies whether the key is a Primary Region key (PRK) (which can be replicated to other AWS Regions) or a Replica Region key (RRK) (which is a copy of a PRK in another Region). For more information, see [Multi-Region key replication](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html).
Type: String
Valid Values: `PRIMARY | REPLICA`
Required: No

 ** PrimaryRegion **   <a name="paymentcryptography-Type-Key-PrimaryRegion"></a>
An AWS Region identifier in the standard format (e.g., `us-east-1`, `eu-west-1`).
Used to specify regions for key replication operations. The region must be a valid AWS Region where AWS Payment Cryptography is available.
Type: String
Pattern: `[a-z]{2}-[a-z]{1,16}-[0-9]+`
Required: No

 ** ReplicationStatus **   <a name="paymentcryptography-Type-Key-ReplicationStatus"></a>
Information about the replication status of the key across different AWS Regions.
This field provides details about the current state of key replication, including any status messages or operational information. It helps track the progress and health of key replication operations.
Type: String to [ReplicationStatusType](API_ReplicationStatusType.md) object map
Key Pattern: `[a-z]{2}-[a-z]{1,16}-[0-9]+`
Required: No

 ** UsageStartTimestamp **   <a name="paymentcryptography-Type-Key-UsageStartTimestamp"></a>
The date and time after which AWS Payment Cryptography will start using the key material for cryptographic operations.
Type: Timestamp
Required: No

 ** UsageStopTimestamp **   <a name="paymentcryptography-Type-Key-UsageStopTimestamp"></a>
The date and time after which AWS Payment Cryptography will stop using the key material for cryptographic operations.
Type: Timestamp
Required: No

 ** UsingDefaultReplicationRegions **   <a name="paymentcryptography-Type-Key-UsingDefaultReplicationRegions"></a>
Indicates whether this key is using the account's default replication regions configuration for [Multi-Region key replication](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html).
When set to `true`, the key automatically replicates to the regions specified in the account's default replication settings. When set to `false`, the key has a custom replication configuration that overrides the account defaults.
Type: Boolean
Required: No

## See Also
<a name="API_Key_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/Key)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/Key)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/Key)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Payment Cryptography Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query payment-cryptography` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
