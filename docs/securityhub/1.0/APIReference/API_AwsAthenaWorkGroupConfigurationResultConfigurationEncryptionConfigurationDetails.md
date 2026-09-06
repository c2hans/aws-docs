---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails.html
---

# AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails
<a name="API_AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails"></a>

 Specifies the method used to encrypt the user’s data stores in the Athena workgroup.

## Contents
<a name="API_AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails_Contents"></a>

 ** EncryptionOption **   <a name="securityhub-Type-AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails-EncryptionOption"></a>
 Indicates whether Amazon Simple Storage Service (Amazon S3) server-side encryption with Amazon S3 managed keys (SSE\_S3), server-side encryption with AWS KMS keys (SSE\_KMS), or client-side encryption with AWS KMS customer managed keys (CSE\_KMS) is used.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KmsKey **   <a name="securityhub-Type-AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails-KmsKey"></a>
 For `SSE_KMS` and `CSE_KMS`, this is the KMS key Amazon Resource Name (ARN) or ID.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails)
