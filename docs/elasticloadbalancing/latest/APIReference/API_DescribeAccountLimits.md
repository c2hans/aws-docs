---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeAccountLimits.html
---

# DescribeAccountLimits
<a name="API_DescribeAccountLimits"></a>

Describes the current Elastic Load Balancing resource limits for your AWS account.

For more information, see the following:
+  [Quotas for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html)
+  [Quotas for your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html)
+  [Quotas for your Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/quotas-limits.html)

## Request Parameters
<a name="API_DescribeAccountLimits_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

## Response Elements
<a name="API_DescribeAccountLimits_ResponseElements"></a>

The following elements are returned by the service.

 **Limits.member.N**
Information about the limits.
Type: Array of [Limit](API_Limit.md) objects

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

## Errors
<a name="API_DescribeAccountLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeAccountLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeAccountLimits)
