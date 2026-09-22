---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_S3Logs.html
---

# S3Logs
<a name="API_S3Logs"></a>

Amazon S3 logging configuration.

## Contents
<a name="API_S3Logs_Contents"></a>

 ** s3BucketName **   <a name="imagebuilder-Type-S3Logs-s3BucketName"></a>
The name of an existing Amazon S3 bucket where Image Builder saves build logs. The bucket isn't validated when you create or update the configuration, and Image Builder doesn't create it. The instance profile associated with this infrastructure configuration must have permission to write to the bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** s3KeyPrefix **   <a name="imagebuilder-Type-S3Logs-s3KeyPrefix"></a>
The Amazon S3 key prefix under which Image Builder writes build and test logs in the bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3Logs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/S3Logs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/S3Logs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/S3Logs)
