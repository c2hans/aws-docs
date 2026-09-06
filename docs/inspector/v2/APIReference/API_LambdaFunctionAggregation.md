---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaFunctionAggregation.html
---

# LambdaFunctionAggregation
<a name="API_LambdaFunctionAggregation"></a>

The details that define a findings aggregation based on AWS Lambda functions.

## Contents
<a name="API_LambdaFunctionAggregation_Contents"></a>

 ** functionNames **   <a name="inspector2-Type-LambdaFunctionAggregation-functionNames"></a>
The AWS Lambda function names to include in the aggregation results.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** functionTags **   <a name="inspector2-Type-LambdaFunctionAggregation-functionTags"></a>
The tags to include in the aggregation results.
Type: Array of [MapFilter](API_MapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceIds **   <a name="inspector2-Type-LambdaFunctionAggregation-resourceIds"></a>
The resource IDs to include in the aggregation results.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** runtimes **   <a name="inspector2-Type-LambdaFunctionAggregation-runtimes"></a>
Returns findings aggregated by AWS Lambda function runtime environments.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-LambdaFunctionAggregation-sortBy"></a>
The finding severity to use for sorting the results.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-LambdaFunctionAggregation-sortOrder"></a>
The order to use for sorting the results.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_LambdaFunctionAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/LambdaFunctionAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/LambdaFunctionAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/LambdaFunctionAggregation)
