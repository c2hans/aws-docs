---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_StreamingLoggingConfig.html
---

# StreamingLoggingConfig
<a name="API_StreamingLoggingConfig"></a>

A complex type that controls whether access logs are written for this streaming distribution.

## Contents
<a name="API_StreamingLoggingConfig_Contents"></a>

 ** Bucket **   <a name="cloudfront-Type-StreamingLoggingConfig-Bucket"></a>
The Amazon S3 bucket to store the access logs in, for example, `amzn-s3-demo-bucket.s3.amazonaws.com`.
Type: String
Required: Yes

 ** Enabled **   <a name="cloudfront-Type-StreamingLoggingConfig-Enabled"></a>
Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you don't want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify `false` for `Enabled`, and specify `empty Bucket` and `Prefix` elements. If you specify `false` for `Enabled` but you specify values for `Bucket` and `Prefix`, the values are automatically deleted.
Type: Boolean
Required: Yes

 ** Prefix **   <a name="cloudfront-Type-StreamingLoggingConfig-Prefix"></a>
An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, `myprefix/`. If you want to enable logging, but you don't want to specify a prefix, you still must include an empty `Prefix` element in the `Logging` element.
Type: String
Required: Yes

## See Also
<a name="API_StreamingLoggingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/StreamingLoggingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/StreamingLoggingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/StreamingLoggingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
