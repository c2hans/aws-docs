---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyIpPools.html
---

# ModifyIpPools
<a name="API_ModifyIpPools"></a>

[Application Load Balancers] Modify the IP pool associated to a load balancer.

## Request Parameters
<a name="API_ModifyIpPools_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** IpamPools **
The IPAM pools to be modified.
Type: [IpamPools](API_IpamPools.md) object
Required: No

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: Yes

 **RemoveIpamPools.member.N**
Remove the IP pools in use by the load balancer.
Type: Array of strings
Valid Values: `ipv4`
Required: No

## Response Elements
<a name="API_ModifyIpPools_ResponseElements"></a>

The following element is returned by the service.

 ** IpamPools **
The IPAM pool ID.
Type: [IpamPools](API_IpamPools.md) object

## Errors
<a name="API_ModifyIpPools_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## See Also
<a name="API_ModifyIpPools_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyIpPools)
