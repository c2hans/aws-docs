---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_S3MonitoringConfiguration.html
---

# S3MonitoringConfiguration
<a name="API_S3MonitoringConfiguration"></a>

The Amazon S3 configuration for monitoring log publishing. You can configure your jobs to send log information to Amazon S3.

## Contents
<a name="API_S3MonitoringConfiguration_Contents"></a>

 ** encryptionKeyArn **   <a name="emrserverless-Type-S3MonitoringConfiguration-encryptionKeyArn"></a>
The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):kms:[a-zA-Z0-9\-]*:([0-9]{12}):key\/[a-zA-Z0-9-]+`
Required: No

 ** logUri **   <a name="emrserverless-Type-S3MonitoringConfiguration-logUri"></a>
The Amazon S3 destination URI for log publishing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10280.
Pattern: `.*[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\r\n\t]*.*`
Required: No

## See Also
<a name="API_S3MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/S3MonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/S3MonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/S3MonitoringConfiguration)
