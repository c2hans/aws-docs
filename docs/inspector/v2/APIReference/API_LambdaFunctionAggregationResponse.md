---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaFunctionAggregationResponse.html
---

# LambdaFunctionAggregationResponse
<a name="API_LambdaFunctionAggregationResponse"></a>

A response that contains the results of an AWS Lambda function finding aggregation.

## Contents
<a name="API_LambdaFunctionAggregationResponse_Contents"></a>

 ** resourceId **   <a name="inspector2-Type-LambdaFunctionAggregationResponse-resourceId"></a>
The resource IDs included in the aggregation results.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** accountId **   <a name="inspector2-Type-LambdaFunctionAggregationResponse-accountId"></a>
The ID of the AWS account that owns the AWS Lambda function.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** functionName **   <a name="inspector2-Type-LambdaFunctionAggregationResponse-functionName"></a>
The AWS Lambda function names included in the aggregation results.
Type: String
Required: No

 ** lambdaTags **   <a name="inspector2-Type-LambdaFunctionAggregationResponse-lambdaTags"></a>
The tags included in the aggregation results.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** lastModifiedAt **   <a name="inspector2-Type-LambdaFunctionAggregationResponse-lastModifiedAt"></a>
The date that the AWS Lambda function included in the aggregation results was last changed.
Type: Timestamp
Required: No

 ** runtime **   <a name="inspector2-Type-LambdaFunctionAggregationResponse-runtime"></a>
The runtimes included in the aggregation results.
Type: String
Required: No

 ** severityCounts **   <a name="inspector2-Type-LambdaFunctionAggregationResponse-severityCounts"></a>
An object that contains the counts of aggregated finding per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_LambdaFunctionAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/LambdaFunctionAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/LambdaFunctionAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/LambdaFunctionAggregationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
