---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_LambdaLayerAggregation.html
---

# LambdaLayerAggregation
<a name="API_LambdaLayerAggregation"></a>

The details that define a findings aggregation based on an AWS Lambda function's layers.

## Contents
<a name="API_LambdaLayerAggregation_Contents"></a>

 ** functionNames **   <a name="inspector2-Type-LambdaLayerAggregation-functionNames"></a>
The names of the AWS Lambda functions associated with the layers.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** layerArns **   <a name="inspector2-Type-LambdaLayerAggregation-layerArns"></a>
The Amazon Resource Name (ARN) of the AWS Lambda function layer.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** resourceIds **   <a name="inspector2-Type-LambdaLayerAggregation-resourceIds"></a>
The resource IDs for the AWS Lambda function layers.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-LambdaLayerAggregation-sortBy"></a>
The finding severity to use for sorting the results.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-LambdaLayerAggregation-sortOrder"></a>
The order to use for sorting the results.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_LambdaLayerAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/LambdaLayerAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/LambdaLayerAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/LambdaLayerAggregation)
