---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_BucketAccessLogConfig.html
---

# BucketAccessLogConfig
<a name="API_BucketAccessLogConfig"></a>

Describes the access log configuration for a bucket in the Amazon Lightsail object storage service.

For more information about bucket access logs, see [Logging bucket requests using access logging in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-bucket-access-logs) in the *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_BucketAccessLogConfig_Contents"></a>

 ** enabled **   <a name="Lightsail-Type-BucketAccessLogConfig-enabled"></a>
A Boolean value that indicates whether bucket access logging is enabled for the bucket.
Type: Boolean
Required: Yes

 ** destination **   <a name="Lightsail-Type-BucketAccessLogConfig-destination"></a>
The name of the bucket where the access logs are saved. The destination can be a Lightsail bucket in the same account, and in the same AWS Region as the source bucket.
This parameter is required when enabling the access log for a bucket, and should be omitted when disabling the access log.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 54.
Pattern: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
Required: No

 ** prefix **   <a name="Lightsail-Type-BucketAccessLogConfig-prefix"></a>
The optional object prefix for the bucket access log.
The prefix is an optional addition to the object key that organizes your access log files in the destination bucket. For example, if you specify a `logs/` prefix, then each log object will begin with the `logs/` prefix in its key (for example, `logs/2021-11-01-21-32-16-E568B2907131C0C0`).
This parameter can be optionally specified when enabling the access log for a bucket, and should be omitted when disabling the access log.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w/!.*')(-]+$`
Required: No

## See Also
<a name="API_BucketAccessLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/BucketAccessLogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/BucketAccessLogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/BucketAccessLogConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
