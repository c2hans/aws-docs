---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_KeySummary.html
---

# KeySummary
<a name="API_KeySummary"></a>

Metadata about an AWS Payment Cryptography key.

## Contents
<a name="API_KeySummary_Contents"></a>

 ** Enabled **   <a name="paymentcryptography-Type-KeySummary-Enabled"></a>
Specifies whether the key is enabled.
Type: Boolean
Required: Yes

 ** Exportable **   <a name="paymentcryptography-Type-KeySummary-Exportable"></a>
Specifies whether the key is exportable. This data is immutable after the key is created.
Type: Boolean
Required: Yes

 ** KeyArn **   <a name="paymentcryptography-Type-KeySummary-KeyArn"></a>
The Amazon Resource Name (ARN) of the key.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: Yes

 ** KeyAttributes **   <a name="paymentcryptography-Type-KeySummary-KeyAttributes"></a>
The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.
Type: [KeyAttributes](API_KeyAttributes.md) object
Required: Yes

 ** KeyCheckValue **   <a name="paymentcryptography-Type-KeySummary-KeyCheckValue"></a>
The key check value (KCV) is used to check if all parties holding a given key have the same key or to detect that a key has changed.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** KeyState **   <a name="paymentcryptography-Type-KeySummary-KeyState"></a>
The state of an AWS Payment Cryptography that is being created or deleted.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_COMPLETE | DELETE_PENDING | DELETE_COMPLETE`
Required: Yes

 ** MultiRegionKeyType **   <a name="paymentcryptography-Type-KeySummary-MultiRegionKeyType"></a>
Indicates whether this key is a Multi-Region key and its role in the Multi-Region key hierarchy.
Multi-Region replication keys allow the same key material to be used across multiple AWS Regions. This field specifies whether the key is a Primary Region key (PRK) (which can be replicated to other AWS Regions) or a Replica Region key (RRK) (which is a copy of a PRK in another Region). For more information, see [Multi-Region key replication](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-multi-region-replication.html).
Type: String
Valid Values: `PRIMARY | REPLICA`
Required: No

 ** PrimaryRegion **   <a name="paymentcryptography-Type-KeySummary-PrimaryRegion"></a>
An AWS Region identifier in the standard format (e.g., `us-east-1`, `eu-west-1`).
Used to specify regions for key replication operations. The region must be a valid AWS Region where AWS Payment Cryptography is available.
Type: String
Pattern: `[a-z]{2}-[a-z]{1,16}-[0-9]+`
Required: No

## See Also
<a name="API_KeySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/KeySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/KeySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/KeySummary)
