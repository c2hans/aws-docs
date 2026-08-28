---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ConnectionFunctionSummary.html
---

# ConnectionFunctionSummary
<a name="API_ConnectionFunctionSummary"></a>

A connection function summary.

## Contents
<a name="API_ConnectionFunctionSummary_Contents"></a>

 ** ConnectionFunctionArn **   <a name="cloudfront-Type-ConnectionFunctionSummary-ConnectionFunctionArn"></a>
The connection function Amazon Resource Name (ARN).
Type: String
Required: Yes

 ** ConnectionFunctionConfig **   <a name="cloudfront-Type-ConnectionFunctionSummary-ConnectionFunctionConfig"></a>
Contains configuration information about a CloudFront function.
Type: [FunctionConfig](API_FunctionConfig.md) object
Required: Yes

 ** CreatedTime **   <a name="cloudfront-Type-ConnectionFunctionSummary-CreatedTime"></a>
The connection function created time.
Type: Timestamp
Required: Yes

 ** Id **   <a name="cloudfront-Type-ConnectionFunctionSummary-Id"></a>
The connection function ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-ConnectionFunctionSummary-LastModifiedTime"></a>
The connection function last modified time.
Type: Timestamp
Required: Yes

 ** Name **   <a name="cloudfront-Type-ConnectionFunctionSummary-Name"></a>
The connection function name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]{1,64}`
Required: Yes

 ** Stage **   <a name="cloudfront-Type-ConnectionFunctionSummary-Stage"></a>
The connection function stage.
Type: String
Valid Values: `DEVELOPMENT | LIVE`
Required: Yes

 ** Status **   <a name="cloudfront-Type-ConnectionFunctionSummary-Status"></a>
The connection function status.
Type: String
Required: Yes

## See Also
<a name="API_ConnectionFunctionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ConnectionFunctionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ConnectionFunctionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ConnectionFunctionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
