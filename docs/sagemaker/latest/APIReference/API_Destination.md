---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

An endpoint or inference component that serves a routing target.

## Contents
<a name="API_Destination_Contents"></a>

 ** ResourceArn **   <a name="sagemaker-Type-Destination-ResourceArn"></a>
The Amazon Resource Name (ARN) of the endpoint or inference component. The destination can be in any account, and in any AWS Region in the same partition as the inference router. To use a destination in another account, its owner must allow your account to invoke it through your router, in an endpoint policy.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z-]*:sagemaker:[a-z0-9-]+:[0-9]{12}:(endpoint|inference-component)/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** RoutingStatus **   <a name="sagemaker-Type-Destination-RoutingStatus"></a>
Whether the inference router can send requests to the destination, as checked when you called `DescribeInferenceRouter`. This value isn't the destination's own status. SageMaker AI ignores this field in `CreateInferenceRouter` and `UpdateInferenceRouter` requests.
Routable
The destination is serving and the router can send it requests. A routable destination can still be overloaded.
Unroutable
The destination can't serve requests. For example, it's being created or has failed, or it has no capacity and no way to get any. A destination in your account that doesn't exist is also `Unroutable`.
Unknown
SageMaker AI couldn't check the destination, for example because you aren't allowed to describe it or the check timed out. The destination might still be serving.
Type: String
Valid Values: `Routable | Unroutable | Unknown`
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Destination)
