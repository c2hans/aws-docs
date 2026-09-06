---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_EncryptionDetails.html
---

# EncryptionDetails
<a name="API_EncryptionDetails"></a>

Configuration details about encryption for the cluster including the AWS KMS key ARN, encryption type, and encryption status.

## Contents
<a name="API_EncryptionDetails_Contents"></a>

 ** encryptionStatus **   <a name="auroradsql-Type-EncryptionDetails-encryptionStatus"></a>
The status of encryption for the cluster.
Type: String
Valid Values: `ENABLED | UPDATING | KMS_KEY_INACCESSIBLE | ENABLING`
Required: Yes

 ** encryptionType **   <a name="auroradsql-Type-EncryptionDetails-encryptionType"></a>
The type of encryption that protects the data on your cluster.
Type: String
Valid Values: `AWS_OWNED_KMS_KEY | CUSTOMER_MANAGED_KMS_KEY`
Required: Yes

 ** kmsKeyArn **   <a name="auroradsql-Type-EncryptionDetails-kmsKeyArn"></a>
The ARN of the AWS KMS key that encrypts data in the cluster.
Type: String
Required: No

## See Also
<a name="API_EncryptionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/EncryptionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/EncryptionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/EncryptionDetails)
