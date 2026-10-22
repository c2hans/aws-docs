---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayResourceFailure.html
---

# GatewayResourceFailure
<a name="API_GatewayResourceFailure"></a>

The failures for a single resource that was touched by an asynchronous gateway process.

## Contents
<a name="API_GatewayResourceFailure_Contents"></a>

 ** arn **   <a name="ECS-Type-GatewayResourceFailure-arn"></a>
The Amazon Resource Name (ARN) of the resource that failed to update, such as a load balancer ARN.
Type: String
Required: No

 ** errors **   <a name="ECS-Type-GatewayResourceFailure-errors"></a>
The errors that were encountered while operating on the resource.
Type: Array of [GatewayOperationError](API_GatewayOperationError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_GatewayResourceFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayResourceFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayResourceFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayResourceFailure)
