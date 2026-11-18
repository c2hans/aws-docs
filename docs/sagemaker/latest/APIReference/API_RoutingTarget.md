---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RoutingTarget.html
---

# RoutingTarget
<a name="API_RoutingTarget"></a>

A model that an inference router serves, and the destinations that can serve it. When you invoke the router, you name the routing target, and the router sends the request to one of its destinations.

Every destination in a routing target must serve the same model, with the same request and response format.

## Contents
<a name="API_RoutingTarget_Contents"></a>

 ** Destinations **   <a name="sagemaker-Type-RoutingTarget-Destinations"></a>
The endpoints and inference components that serve the routing target. Each destination can appear only once in a routing target.
In an asynchronous routing target, every destination must be an asynchronous inference endpoint. In a real-time routing target, no destination can be one. SageMaker AI checks an endpoint in another account with your credentials, so both your IAM policy and the endpoint policy must allow `sagemaker:DescribeEndpoint`. If an endpoint can't be checked, for example because it isn't found or can't be read in time, it's accepted, and requests to it fail if it's the wrong mode.
Type: Array of [Destination](API_Destination.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** Name **   <a name="sagemaker-Type-RoutingTarget-Name"></a>
The name of the routing target. Callers specify this name in the `RoutingTargetName` parameter when they invoke the inference router. The name must be unique within the router.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** AsyncInferenceConfig **   <a name="sagemaker-Type-RoutingTarget-AsyncInferenceConfig"></a>
The asynchronous inference settings of the routing target. Specify this setting to make the routing target asynchronous. If you omit it, the routing target serves real-time requests.
Asynchronous routing targets aren't available in all AWS Regions. For information about asynchronous routing targets and Region availability, see [Send asynchronous requests through an inference router](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html).
Because `UpdateInferenceRouter` replaces all routing targets, include this setting in every update of an asynchronous routing target.
For information about asynchronous routing targets, see [Send asynchronous requests through an inference router](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-router-async.html).
Type: [RoutingTargetAsyncInferenceConfig](API_RoutingTargetAsyncInferenceConfig.md) object
Required: No

 ** RoutingPreference **   <a name="sagemaker-Type-RoutingTarget-RoutingPreference"></a>
How the inference router chooses among the routing target's destinations. The default is `LocalRegionFirst`.
LocalRegionFirst
The router uses destinations in its own Region first. When the request leaves the Region, the router spreads it across healthy destinations in other Regions.
InstancePoolOrder
The router prefers destinations by instance type first and by Region second. Every destination must be an endpoint that lists the same two or more instance types, each with a different priority, in the same priority order. This value is supported only for asynchronous routing targets.
With either value, the router uses destinations whose health or capacity is reduced after the others, but doesn't exclude them.
Type: String
Valid Values: `LocalRegionFirst | InstancePoolOrder`
Required: No

## See Also
<a name="API_RoutingTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RoutingTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RoutingTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RoutingTarget)
