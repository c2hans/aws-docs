---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FunctionMetadata.html
---

# FunctionMetadata
<a name="API_FunctionMetadata"></a>

Contains metadata about a CloudFront function.

## Contents
<a name="API_FunctionMetadata_Contents"></a>

 ** FunctionARN **   <a name="cloudfront-Type-FunctionMetadata-FunctionARN"></a>
The Amazon Resource Name (ARN) of the function. The ARN uniquely identifies the function.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="cloudfront-Type-FunctionMetadata-LastModifiedTime"></a>
The date and time when the function was most recently updated.
Type: Timestamp
Required: Yes

 ** CreatedTime **   <a name="cloudfront-Type-FunctionMetadata-CreatedTime"></a>
The date and time when the function was created.
Type: Timestamp
Required: No

 ** Stage **   <a name="cloudfront-Type-FunctionMetadata-Stage"></a>
The stage that the function is in, either `DEVELOPMENT` or `LIVE`.
When a function is in the `DEVELOPMENT` stage, you can test the function with `TestFunction`, and update it with `UpdateFunction`.
When a function is in the `LIVE` stage, you can attach the function to a distribution's cache behavior, using the function's ARN.
Type: String
Valid Values: `DEVELOPMENT | LIVE`
Required: No

## See Also
<a name="API_FunctionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
