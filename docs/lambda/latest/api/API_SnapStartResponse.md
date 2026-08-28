---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_SnapStartResponse.html
---

# SnapStartResponse
<a name="API_SnapStartResponse"></a>

The function's [SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) setting.

## Contents
<a name="API_SnapStartResponse_Contents"></a>

 ** ApplyOn **   <a name="lambda-Type-SnapStartResponse-ApplyOn"></a>
When set to `PublishedVersions`, Lambda creates a snapshot of the execution environment when you publish a function version.
Type: String
Valid Values: `PublishedVersions | None`
Required: No

 ** OptimizationStatus **   <a name="lambda-Type-SnapStartResponse-OptimizationStatus"></a>
When you provide a [qualified Amazon Resource Name (ARN)](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html#versioning-versions-using), this response element indicates whether SnapStart is activated for the specified function version.
Type: String
Valid Values: `On | Off`
Required: No

## See Also
<a name="API_SnapStartResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/SnapStartResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/SnapStartResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/SnapStartResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
