---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_CloudWatchLogging.html
---

# CloudWatchLogging
<a name="API_CloudWatchLogging"></a>

Configuration for Amazon CloudWatch Logs logging.

## Contents
<a name="API_CloudWatchLogging_Contents"></a>

 ** logGroup **   <a name="lambdamicrovm-Type-CloudWatchLogging-logGroup"></a>
The name of the CloudWatch Logs log group to send logs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9_\-/.#]+`
Required: No

 ** logStream **   <a name="lambdamicrovm-Type-CloudWatchLogging-logStream"></a>
The name of the CloudWatch Logs log stream within the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

## See Also
<a name="API_CloudWatchLogging_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/CloudWatchLogging)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/CloudWatchLogging)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/CloudWatchLogging)
