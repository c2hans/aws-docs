---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ManagedLoggingConfiguration.html
---

# ManagedLoggingConfiguration
<a name="API_ManagedLoggingConfiguration"></a>

Configuration settings for delivering logs to Amazon S3 buckets.

## Contents
<a name="API_ManagedLoggingConfiguration_Contents"></a>

 ** Enabled **   <a name="athena-Type-ManagedLoggingConfiguration-Enabled"></a>
Enables mamanged log persistence.
Type: Boolean
Required: Yes

 ** KmsKey **   <a name="athena-Type-ManagedLoggingConfiguration-KmsKey"></a>
The KMS key ARN to encrypt the logs stored in managed log persistence.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:key/?[a-zA-Z_0-9+=,.@\-_/]+$|^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:alias/?[a-zA-Z_0-9+=,.@\-_/]+$|^alias/[a-zA-Z0-9/_-]+$|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

## See Also
<a name="API_ManagedLoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ManagedLoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ManagedLoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ManagedLoggingConfiguration)
