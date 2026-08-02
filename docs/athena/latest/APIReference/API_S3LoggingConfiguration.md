---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_S3LoggingConfiguration.html
---

# S3LoggingConfiguration
<a name="API_S3LoggingConfiguration"></a>

Configuration settings for delivering logs to Amazon S3 buckets.

## Contents
<a name="API_S3LoggingConfiguration_Contents"></a>

 ** Enabled **   <a name="athena-Type-S3LoggingConfiguration-Enabled"></a>
Enables S3 log delivery.
Type: Boolean
Required: Yes

 ** KmsKey **   <a name="athena-Type-S3LoggingConfiguration-KmsKey"></a>
The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:key/?[a-zA-Z_0-9+=,.@\-_/]+$|^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:alias/?[a-zA-Z_0-9+=,.@\-_/]+$|^alias/[a-zA-Z0-9/_-]+$|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** LogLocation **   <a name="athena-Type-S3LoggingConfiguration-LogLocation"></a>
The Amazon S3 destination URI for log publishing.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^s3://[a-z0-9][a-z0-9\-]*[a-z0-9](/.*)?$`
Required: No

## See Also
<a name="API_S3LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/S3LoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/S3LoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/S3LoggingConfiguration)
