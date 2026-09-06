---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_EncryptionSpecification.html
---

# EncryptionSpecification
<a name="API_EncryptionSpecification"></a>

Amazon Keyspaces encrypts and decrypts the table data at rest transparently and integrates with AWS Key Management Service for storing and managing the encryption key. You can choose one of the following AWS KMS keys (KMS keys):
+  AWS owned key - This is the default encryption type. The key is owned by Amazon Keyspaces (no additional charge).
+ Customer managed key - This key is stored in your account and is created, owned, and managed by you. You have full control over the customer managed key (AWS KMS charges apply).

For more information about encryption at rest in Amazon Keyspaces, see [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide*.

For more information about AWS KMS, see [AWS KMS management service concepts](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the * AWS Key Management Service Developer Guide*.

## Contents
<a name="API_EncryptionSpecification_Contents"></a>

 ** type **   <a name="keyspaces-Type-EncryptionSpecification-type"></a>
The encryption option specified for the table. You can choose one of the following KMS keys (KMS keys):
+  `type:AWS_OWNED_KMS_KEY` - This key is owned by Amazon Keyspaces.
+  `type:CUSTOMER_MANAGED_KMS_KEY` - This key is stored in your account and is created, owned, and managed by you. This option requires the `kms_key_identifier` of the KMS key in Amazon Resource Name (ARN) format as input.
The default is `type:AWS_OWNED_KMS_KEY`.
For more information, see [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html) in the *Amazon Keyspaces Developer Guide*.
Type: String
Valid Values: `CUSTOMER_MANAGED_KMS_KEY | AWS_OWNED_KMS_KEY`
Required: Yes

 ** kmsKeyIdentifier **   <a name="keyspaces-Type-EncryptionSpecification-kmsKeyIdentifier"></a>
The Amazon Resource Name (ARN) of the customer managed KMS key, for example `kms_key_identifier:ARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5096.
Required: No

## See Also
<a name="API_EncryptionSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/EncryptionSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/EncryptionSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/EncryptionSpecification)
