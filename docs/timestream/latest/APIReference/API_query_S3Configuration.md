---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_S3Configuration.html
---

# S3Configuration
<a name="API_query_S3Configuration"></a>

Details on S3 location for error reports that result from running a query.

## Contents
<a name="API_query_S3Configuration_Contents"></a>

 ** BucketName **   <a name="timestream-Type-query_S3Configuration-BucketName"></a>
 Name of the S3 bucket under which error reports will be created.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: Yes

 ** EncryptionOption **   <a name="timestream-Type-query_S3Configuration-EncryptionOption"></a>
 Encryption at rest options for the error reports. If no encryption option is specified, Timestream will choose SSE\_S3 as default.
Type: String
Valid Values: `SSE_S3 | SSE_KMS`
Required: No

 ** ObjectKeyPrefix **   <a name="timestream-Type-query_S3Configuration-ObjectKeyPrefix"></a>
 Prefix for the error report key. Timestream by default adds the following prefix to the error report path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 896.
Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`
Required: No

## See Also
<a name="API_query_S3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/S3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/S3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/S3Configuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
