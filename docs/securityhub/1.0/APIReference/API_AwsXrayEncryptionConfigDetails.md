---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsXrayEncryptionConfigDetails.html
---

# AwsXrayEncryptionConfigDetails
<a name="API_AwsXrayEncryptionConfigDetails"></a>

Information about the encryption configuration for AWS X-Ray.

## Contents
<a name="API_AwsXrayEncryptionConfigDetails_Contents"></a>

 ** KeyId **   <a name="securityhub-Type-AwsXrayEncryptionConfigDetails-KeyId"></a>
The identifier of the KMS key that is used for encryption. Provided if `Type` is `KMS`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsXrayEncryptionConfigDetails-Status"></a>
The current status of the encryption configuration. Valid values are `ACTIVE` or `UPDATING`.
When `Status` is equal to `UPDATING`, AWS X-Ray might use both the old and new encryption.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsXrayEncryptionConfigDetails-Type"></a>
The type of encryption. `KMS` indicates that the encryption uses KMS keys. `NONE` indicates the default encryption.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsXrayEncryptionConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsXrayEncryptionConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsXrayEncryptionConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsXrayEncryptionConfigDetails)
