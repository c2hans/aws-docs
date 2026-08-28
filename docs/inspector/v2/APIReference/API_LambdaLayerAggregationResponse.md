---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaLayerAggregationResponse.html
---

# LambdaLayerAggregationResponse
<a name="API_LambdaLayerAggregationResponse"></a>

A response that contains the results of an AWS Lambda function layer finding aggregation.

## Contents
<a name="API_LambdaLayerAggregationResponse_Contents"></a>

 ** accountId **   <a name="inspector2-Type-LambdaLayerAggregationResponse-accountId"></a>
The account ID of the AWS Lambda function layer.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** functionName **   <a name="inspector2-Type-LambdaLayerAggregationResponse-functionName"></a>
The names of the AWS Lambda functions associated with the layers.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** layerArn **   <a name="inspector2-Type-LambdaLayerAggregationResponse-layerArn"></a>
The Amazon Resource Name (ARN) of the AWS Lambda function layer.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** resourceId **   <a name="inspector2-Type-LambdaLayerAggregationResponse-resourceId"></a>
The Resource ID of the AWS Lambda function layer.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** severityCounts **   <a name="inspector2-Type-LambdaLayerAggregationResponse-severityCounts"></a>
An object that contains the counts of aggregated finding per severity.
Type: [SeverityCounts](API_SeverityCounts.md) object
Required: No

## See Also
<a name="API_LambdaLayerAggregationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/LambdaLayerAggregationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/LambdaLayerAggregationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/LambdaLayerAggregationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
