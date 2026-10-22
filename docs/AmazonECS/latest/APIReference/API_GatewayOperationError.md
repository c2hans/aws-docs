---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayOperationError.html
---

# GatewayOperationError
<a name="API_GatewayOperationError"></a>

A single failed operation against a resource that a gateway manages.

## Contents
<a name="API_GatewayOperationError_Contents"></a>

 ** code **   <a name="ECS-Type-GatewayOperationError-code"></a>
The error code returned by the failed operation, passed through from the downstream service, such as `AccessDenied`.
Type: String
Required: No

 ** message **   <a name="ECS-Type-GatewayOperationError-message"></a>
The detailed error message.
Type: String
Required: No

 ** operation **   <a name="ECS-Type-GatewayOperationError-operation"></a>
The IAM-style action identifier of the operation that failed, such as `elasticloadbalancing:ModifyLoadBalancerAttributes`.
Type: String
Required: No

## See Also
<a name="API_GatewayOperationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayOperationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayOperationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayOperationError)
