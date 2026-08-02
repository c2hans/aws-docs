---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_ReportS3Configuration.html
---

# ReportS3Configuration
<a name="API_ReportS3Configuration"></a>

## Contents
<a name="API_ReportS3Configuration_Contents"></a>

 ** BucketName **   <a name="timestream-Type-ReportS3Configuration-BucketName"></a>

Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: Yes

 ** EncryptionOption **   <a name="timestream-Type-ReportS3Configuration-EncryptionOption"></a>

Type: String
Valid Values: `SSE_S3 | SSE_KMS`
Required: No

 ** KmsKeyId **   <a name="timestream-Type-ReportS3Configuration-KmsKeyId"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ObjectKeyPrefix **   <a name="timestream-Type-ReportS3Configuration-ObjectKeyPrefix"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 928.
Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`
Required: No

## See Also
<a name="API_ReportS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/ReportS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/ReportS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/ReportS3Configuration)
