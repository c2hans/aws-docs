---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DeleteLoadBalancerListeners.html
---

# DeleteLoadBalancerListeners
<a name="API_DeleteLoadBalancerListeners"></a>

Deletes the specified listeners from the specified load balancer.

## Request Parameters
<a name="API_DeleteLoadBalancerListeners_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

 **LoadBalancerPorts.member.N**
The client port numbers of the listeners.
Type: Array of integers
Required: Yes

## Errors
<a name="API_DeleteLoadBalancerListeners_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## See Also
<a name="API_DeleteLoadBalancerListeners_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DeleteLoadBalancerListeners)
